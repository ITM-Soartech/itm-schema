# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.probe_responses import ProbeResponses

class TestProbeResponses(unittest.TestCase):
    """ProbeResponses unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProbeResponses:
        """Test ProbeResponses
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProbeResponses`
        """
        model = ProbeResponses()
        if include_optional:
            return ProbeResponses(
                character_id = '',
                probe_id = '',
                minimal = '',
                delayed = '',
                immediate = '',
                expectant = ''
            )
        else:
            return ProbeResponses(
                character_id = '',
                probe_id = '',
                minimal = '',
                delayed = '',
                immediate = '',
                expectant = '',
        )
        """

    def testProbeResponses(self):
        """Test ProbeResponses"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
