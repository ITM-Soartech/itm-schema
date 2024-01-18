# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.action import Action

class TestAction(unittest.TestCase):
    """Action unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Action:
        """Test Action
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Action`
        """
        model = Action()
        if include_optional:
            return Action(
                action_id = 'action_01',
                action_type = 'APPLY_TREATMENT',
                unstructured = 'Check Mike's pulse.',
                repeatable = True,
                character_id = '',
                parameters = [{"treatment":"Tourniquet"},{"location":"right forearm"}],
                probe_id = '',
                choice = '',
                justification = 'Character is the VIP of the scenario',
                kdma_association = [{"Mission":0.8}],
                condition_semantics = 'and',
                conditions = openapi_client.models.conditions.Conditions(
                    elapsed_time_lt = 5, 
                    elapsed_time_gt = 5, 
                    actions = [
                        [
                            ''
                            ]
                        ], 
                    probes = ["adept-september-demo-probe-1"], 
                    probe_responses = ["adept-september-demo-probe-1-choice2"], 
                    character_vitals = [
                        openapi_client.models.conditions_character_vitals_inner.Conditions_character_vitals_inner(
                            character_id = '', 
                            vitals = openapi_client.models.vitals.Vitals(
                                conscious = True, 
                                avpu = 'ALERT', 
                                ambulatory = True, 
                                mental_status = 'AGONY', 
                                breathing = 'NORMAL', 
                                hrpmin = 0, 
                                spo2 = 0.0, ), )
                        ], 
                    supplies = [{"type":"Tourniquet","quantity":1,"reusable":false}], )
            )
        else:
            return Action(
                action_id = 'action_01',
                action_type = 'APPLY_TREATMENT',
                unstructured = 'Check Mike's pulse.',
        )
        """

    def testAction(self):
        """Test Action"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
