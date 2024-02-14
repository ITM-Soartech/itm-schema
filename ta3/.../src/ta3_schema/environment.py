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

from pydantic import BaseModel
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.decision_environment import DecisionEnvironment
from openapi_client.models.sim_environment import SimEnvironment
from typing import Optional, Set
from typing_extensions import Self

class Environment(BaseModel):
    """
    Environmental parameters that impact either decision-making, the simulation environment, or both
    """ # noqa: E501
    sim_environment: SimEnvironment
    decision_environment: Optional[DecisionEnvironment] = None
    __properties: ClassVar[List[str]] = ["sim_environment", "decision_environment"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Environment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sim_environment
        if self.sim_environment:
            _dict['sim_environment'] = self.sim_environment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of decision_environment
        if self.decision_environment:
            _dict['decision_environment'] = self.decision_environment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Environment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sim_environment": SimEnvironment.from_dict(obj["sim_environment"]) if obj.get("sim_environment") is not None else None,
            "decision_environment": DecisionEnvironment.from_dict(obj["decision_environment"]) if obj.get("decision_environment") is not None else None
        })
        return _obj


