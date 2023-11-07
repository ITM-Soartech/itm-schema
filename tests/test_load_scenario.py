from pathlib import Path
from .test_utils import load_file
import os
import unittest

def test_load_scenarios(scenarios_dir):
    # parse through each scenario in the data folder
    scenarios = []
    for filename in os.listdir(scenarios_dir):
        filepath = os.path.join(scenarios_dir, filename)
        if os.path.isdir(filepath):
            scenarios.append(load_file(Path(os.path.join(Path(filepath), Path("scenario.yaml")))))

    for scenario in scenarios:
        print(scenario["id"])


class Test(unittest.TestCase):
    def test_load_scenarios(self):
        scenarios_dir = Path(os.path.dirname(__file__)) / '../demo/scenarios'
        test_load_scenarios(scenarios_dir)
