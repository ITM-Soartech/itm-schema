from pathlib import Path
from itm_schema_tests.test_utils import load_file
import os

def test_load_scenarios(scenarios_dir):
    # parse through each scenario in the data folder
    scenarios = []
    for filename in os.listdir(scenarios_dir):
        filepath = os.path.join(scenarios_dir, filename)
        if os.path.isdir(filepath):
            scenarios.append(load_file(Path(os.path.join(Path(filepath), Path("scenario.yaml")))))

    for scenario in scenarios:
        print(scenario["id"])
