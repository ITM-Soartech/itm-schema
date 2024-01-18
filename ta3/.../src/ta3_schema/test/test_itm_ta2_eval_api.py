# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.itm_ta2_eval_api import ItmTa2EvalApi


class TestItmTa2EvalApi(unittest.TestCase):
    """ItmTa2EvalApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ItmTa2EvalApi()

    def tearDown(self) -> None:
        pass

    def test_get_alignment_target(self) -> None:
        """Test case for get_alignment_target

        Retrieve alignment target for the scenario
        """
        pass

    def test_get_available_actions(self) -> None:
        """Test case for get_available_actions

        Get a list of currently available ADM actions
        """
        pass

    def test_get_scenario_state(self) -> None:
        """Test case for get_scenario_state

        Retrieve scenario state
        """
        pass

    def test_get_session_alignment(self) -> None:
        """Test case for get_session_alignment

        Retrieve session alignment from TA1
        """
        pass

    def test_start_scenario(self) -> None:
        """Test case for start_scenario

        Get the next scenario
        """
        pass

    def test_start_session(self) -> None:
        """Test case for start_session

        Start a new session
        """
        pass

    def test_take_action(self) -> None:
        """Test case for take_action

        Take an action within a scenario
        """
        pass


if __name__ == '__main__':
    unittest.main()
