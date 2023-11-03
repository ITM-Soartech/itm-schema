import requests
import json
from src.itm_schema import pydantic_schema as ps, stats_pydantic_schema as sps
from argparse import ArgumentParser
from typing import Optional
from random import Random

parser = ArgumentParser(prog='ITM test script')
parser.add_argument('-p', '--port', action='store', dest='port', default=8084,
                    type=int, help='port to connect to')
parser.add_argument('--user', action='store', dest='user', default='default_user',
                    help='username to be associated with session')
parser.add_argument('--seed', action='store', dest='seed', default=None,
                    type=Optional[int],
                    help='random seed to use for response to probe choices')
parser.add_argument('--reset-db', action='store_true', dest='reset_db')
parser.add_argument('--db-conn', action='store', default='mongodb://localhost:27017')

args = parser.parse_args()
print(args.reset_db)

if args.reset_db:
    import asyncio
    from itm_app.backend.mongo_db import reset_db

    asyncio.run(reset_db(args.db_conn))

# rng used to randomly select 
# fixed seed will ensure deterministic behavior
rng = Random(args.seed)

# base url for api
base = 'http://localhost:{}/api/v1/'.format(args.port)

# stats url has different endpoint for getting probe which contains
# additional information about displaying information in ui
base_stats = 'http://localhost:{}/api/stats/v1/'.format(args.port)

response = requests.get(base + 'scenarios')
if response.status_code == 200:
    scenarios = json.loads(response.content)
elif response.status_code >= 500:
    raise (Exception('Server error'))
print(scenarios)

# run through data collect scenarios
scenario_ids = [x for x in scenarios if x.startswith('data-collect-scenario-')]

scenario_ids.remove("data-collect-scenario-4")  # REMOVE ME--DEBUGGING
# scenario_ids = ["data-collect-scenario-5"] # REMOVE ME--DEBUGGING

print('\n', 'starting session')
response = requests.post(base + f'new_session?user_id={args.user}')
session_id = 'N/A'
if response.status_code == 200:
    session_id = json.loads(response.content)
elif response.status_code >= 500:
    raise (Exception('Server error'))
print('\t', f'status: {response.status_code}, session_id={session_id}',
      '\n')

print('getting available scenarios')
response = requests.get(base + 'scenarios')
if response.status_code >= 500:
    raise (Exception('Server error'))
print('\t', 'status: {}, scenarios: {}'.format(
    response.status_code, ', '.join(json.loads(
        response.content))), '\n')

for scenario_id in scenario_ids:
    print('choosing scenario: {}'.format(scenario_id))
    print('\t', 'initializing scenario data')
    response = requests.get(base + f'scenario/{scenario_id}?session_id={session_id}')
    if response.status_code >= 500:
        raise (Exception('Server error'))
    print('\t', f'status: {response.status_code}', '\n')

    print('getting first probe')
    get_request = f'current-probe?session_id={session_id}&scenario_id={scenario_id}'
    response = requests.get(base_stats + get_request)
    if response.status_code >= 500:
        raise (Exception('Server error'))
    print('\t', f'status: {response.status_code}, ')

    max_iter = 1e3
    curr_iter = 0
    max_iter_exceeded = False
    while response.status_code == 200:

        probe = sps.StatsProbe.parse_raw(response.content)
        print('\t', f'current probe id: {probe.id}')

        probe_response_choice = rng.choice([option.id for option in probe.options])

        print(f'submitting response to probe {probe.id}: {probe_response_choice}')
        probe_response = ps.ProbeResponse(
            session_id=session_id,
            response=ps.Response(scenario_id=scenario_id,
                                 probe_id=probe.id,
                                 choice=probe_response_choice))
        response = requests.post(base + 'response', data=probe_response.json())
        if response.status_code >= 500:
            raise (Exception('Server error'))
        print('\t', f'status: {response.status_code}', '\n')

        print('getting next probe')
        response = requests.get(base_stats + get_request)
        if response.status_code >= 500:
            raise (Exception('Server error'))
        print('\t', f'status: {response.status_code}', '\n')

        curr_iter += 1
        if curr_iter > max_iter:
            max_iter_exceeded = True
            break

    if max_iter_exceeded:
        print('max iterations exceeded')

    print(f'end of scenario (session_id={session_id}, scenario_id={scenario_id})', '\n')

print('', 'test complete', '', sep='\n')
