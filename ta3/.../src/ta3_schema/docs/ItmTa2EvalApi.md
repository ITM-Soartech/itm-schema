# openapi_client.ItmTa2EvalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alignment_target**](ItmTa2EvalApi.md#get_alignment_target) | **GET** /ta2/getAlignmentTarget | Retrieve alignment target for the scenario
[**get_available_actions**](ItmTa2EvalApi.md#get_available_actions) | **GET** /ta2/{scenario_id}/getAvailableActions | Get a list of currently available ADM actions
[**get_scenario_state**](ItmTa2EvalApi.md#get_scenario_state) | **GET** /ta2/{scenario_id}/getState | Retrieve scenario state
[**get_session_alignment**](ItmTa2EvalApi.md#get_session_alignment) | **GET** /ta2/getSessionAlignment | Retrieve session alignment from TA1
[**start_scenario**](ItmTa2EvalApi.md#start_scenario) | **GET** /ta2/scenario | Get the next scenario
[**start_session**](ItmTa2EvalApi.md#start_session) | **GET** /ta2/startSession | Start a new session
[**take_action**](ItmTa2EvalApi.md#take_action) | **POST** /ta2/takeAction | Take an action within a scenario


# **get_alignment_target**
> AlignmentTarget get_alignment_target(session_id, scenario_id)

Retrieve alignment target for the scenario

Retrieve alignment target for the scenario with the specified id

### Example


```python
import openapi_client
from openapi_client.models.alignment_target import AlignmentTarget
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItmTa2EvalApi(api_client)
    session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
    scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve alignment target

    try:
        # Retrieve alignment target for the scenario
        api_response = api_instance.get_alignment_target(session_id, scenario_id)
        print("The response of ItmTa2EvalApi->get_alignment_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItmTa2EvalApi->get_alignment_target: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **scenario_id** | **str**| The ID of the scenario for which to retrieve alignment target | 

### Return type

[**AlignmentTarget**](AlignmentTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation, alignment target returned |  -  |
**400** | Scenario Complete or Invalid Session ID |  -  |
**404** | Scenario ID not found |  -  |
**500** | An exception occurred on the server; see returned error string. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_actions**
> List[Action] get_available_actions(session_id, scenario_id)

Get a list of currently available ADM actions

Retrieve a list of currently available actions in the scenario with the specified id

### Example


```python
import openapi_client
from openapi_client.models.action import Action
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItmTa2EvalApi(api_client)
    session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
    scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve available actions

    try:
        # Get a list of currently available ADM actions
        api_response = api_instance.get_available_actions(session_id, scenario_id)
        print("The response of ItmTa2EvalApi->get_available_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItmTa2EvalApi->get_available_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **scenario_id** | **str**| The ID of the scenario for which to retrieve available actions | 

### Return type

[**List[Action]**](Action.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation; array of possible Actions returned |  -  |
**400** | Scenario Complete or Invalid Session ID |  -  |
**404** | Scenario ID not found |  -  |
**500** | An exception occurred on the server; see returned error string. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_state**
> State get_scenario_state(session_id, scenario_id)

Retrieve scenario state

Retrieve state of the scenario with the specified id

### Example


```python
import openapi_client
from openapi_client.models.state import State
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItmTa2EvalApi(api_client)
    session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
    scenario_id = 'scenario_id_example' # str | the ID of the scenario for which to retrieve status

    try:
        # Retrieve scenario state
        api_response = api_instance.get_scenario_state(session_id, scenario_id)
        print("The response of ItmTa2EvalApi->get_scenario_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItmTa2EvalApi->get_scenario_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **scenario_id** | **str**| the ID of the scenario for which to retrieve status | 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation, scenario state returned |  -  |
**400** | Invalid Session ID |  -  |
**404** | Scenario ID not found |  -  |
**500** | An exception occurred on the server; see returned error string. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_alignment**
> AlignmentResults get_session_alignment(session_id, target_id)

Retrieve session alignment from TA1

Retrieve the current session alignment for the session with the specified id

### Example


```python
import openapi_client
from openapi_client.models.alignment_results import AlignmentResults
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItmTa2EvalApi(api_client)
    session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
    target_id = 'target_id_example' # str | alignment target id

    try:
        # Retrieve session alignment from TA1
        api_response = api_instance.get_session_alignment(session_id, target_id)
        print("The response of ItmTa2EvalApi->get_session_alignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItmTa2EvalApi->get_session_alignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **target_id** | **str**| alignment target id | 

### Return type

[**AlignmentResults**](AlignmentResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Session ID not found |  -  |
**403** | Session alignment can only be requested during a training session |  -  |
**500** | An exception occurred on the server; see returned error string. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_scenario**
> Scenario start_scenario(session_id, scenario_id=scenario_id)

Get the next scenario

Get the next scenario in a session with the specified ADM name, returning a Scenario object and unique id

### Example


```python
import openapi_client
from openapi_client.models.scenario import Scenario
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItmTa2EvalApi(api_client)
    session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
    scenario_id = 'scenario_id_example' # str | a scenario id to start, used internally by TA3 (optional)

    try:
        # Get the next scenario
        api_response = api_instance.start_scenario(session_id, scenario_id=scenario_id)
        print("The response of ItmTa2EvalApi->start_scenario:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItmTa2EvalApi->start_scenario: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **scenario_id** | **str**| a scenario id to start, used internally by TA3 | [optional] 

### Return type

[**Scenario**](Scenario.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation; scenario data returned, or session_complete is True |  -  |
**400** | Invalid Session ID or there is already an active scenario |  -  |
**403** | Specifying a scenario ID is unauthorized |  -  |
**404** | Scenario ID not found |  -  |
**500** | An exception occurred on the server; see returned error string. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_session**
> str start_session(adm_name, session_type, kdma_training=kdma_training, max_scenarios=max_scenarios)

Start a new session

Get unique session id for grouping answers from a collection of scenarios together

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItmTa2EvalApi(api_client)
    adm_name = 'adm_name_example' # str | A self-assigned ADM name.  Can add authentication later.
    session_type = 'eval' # str | the type of session to start (`eval` or a TA1 name)
    kdma_training = False # bool | whether or not this is a training session with TA2 (optional) (default to False)
    max_scenarios = 56 # int | the maximum number of scenarios requested, not supported in `eval` sessions (optional)

    try:
        # Start a new session
        api_response = api_instance.start_session(adm_name, session_type, kdma_training=kdma_training, max_scenarios=max_scenarios)
        print("The response of ItmTa2EvalApi->start_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItmTa2EvalApi->start_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm_name** | **str**| A self-assigned ADM name.  Can add authentication later. | 
 **session_type** | **str**| the type of session to start (&#x60;eval&#x60; or a TA1 name) | 
 **kdma_training** | **bool**| whether or not this is a training session with TA2 | [optional] [default to False]
 **max_scenarios** | **int**| the maximum number of scenarios requested, not supported in &#x60;eval&#x60; sessions | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid session type or max_scenarios |  -  |
**500** | An exception occurred on the server; see returned error string. |  -  |
**503** | The server is not ready to start a session |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **take_action**
> State take_action(session_id, action=action)

Take an action within a scenario

Take the specified Action within a scenario

### Example


```python
import openapi_client
from openapi_client.models.action import Action
from openapi_client.models.state import State
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItmTa2EvalApi(api_client)
    session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
    action = openapi_client.Action() # Action | Encapsulation of an action taken by a DM in the context of the scenario (optional)

    try:
        # Take an action within a scenario
        api_response = api_instance.take_action(session_id, action=action)
        print("The response of ItmTa2EvalApi->take_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItmTa2EvalApi->take_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **action** | [**Action**](Action.md)| Encapsulation of an action taken by a DM in the context of the scenario | [optional] 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation, scenario state returned |  -  |
**400** | Invalid action or Session ID |  -  |
**500** | An exception occurred on the server; see returned error string. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
