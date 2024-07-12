# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from itm_schema.base_model import UnValidatedBaseModel as BaseModel
from pydantic import ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from .avpu_level_enum import AvpuLevelEnum
from .blood_oxygen_enum import BloodOxygenEnum
from .breathing_level_enum import BreathingLevelEnum
from .heart_rate_enum import HeartRateEnum
from .mental_status_enum import MentalStatusEnum
from typing import Optional, Set
from typing_extensions import Self

class Vitals(BaseModel):
    """
    Vital levels and other indications of health
    """ # noqa: E501
    avpu: Optional[AvpuLevelEnum] = None
    ambulatory: Optional[StrictBool] = Field(default=None, description="whether or not the character can walk")
    mental_status: Optional[MentalStatusEnum] = None
    breathing: Optional[BreathingLevelEnum] = None
    heart_rate: Optional[HeartRateEnum] = None
    spo2: Optional[BloodOxygenEnum] = None
    __properties: ClassVar[List[str]] = ["avpu", "ambulatory", "mental_status", "breathing", "heart_rate", "spo2"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Vitals from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Vitals from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avpu": obj.get("avpu"),
            "ambulatory": obj.get("ambulatory"),
            "mental_status": obj.get("mental_status"),
            "breathing": obj.get("breathing"),
            "heart_rate": obj.get("heart_rate"),
            "spo2": obj.get("spo2")
        })
        return _obj


