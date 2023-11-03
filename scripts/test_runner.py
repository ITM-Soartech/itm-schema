from itm_schema_tests.test_load_scenario import test_load_scenarios


def full_test_suite(scenarios_dir):
    test_load_scenarios(scenarios_dir)


if __name__ == "__main__":
    scenarios_dir = "../demo/scenarios/"
    full_test_suite(scenarios_dir)