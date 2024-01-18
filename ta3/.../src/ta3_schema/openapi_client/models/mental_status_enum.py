# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MentalStatusEnum(str, Enum):
    """
    Character mental status, which impacts interaction in the sim environment
    """

    """
    allowed enum values
    """
    AGONY = 'AGONY'
    CALM = 'CALM'
    CONFUSED = 'CONFUSED'
    UPSET = 'UPSET'
    UNRESPONSIVE = 'UNRESPONSIVE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MentalStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


