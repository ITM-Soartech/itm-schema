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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from .scene import Scene
from .state import State
from typing import Optional, Set
from typing_extensions import Self

class Scenario(BaseModel):
    """
    a triage scenario requiring decisions by a medic
    """ # noqa: E501
    id: StrictStr = Field(description="a globally unique id for the scenario")
    name: StrictStr = Field(description="human-readable scenario name, not necessarily unique")
    first_scene: Optional[StrictStr] = Field(default=None, description="indicates the first/opening scene ID in the scenario")
    session_complete: Optional[StrictBool] = Field(default=None, description="set to true if the session is complete; that is, there are no more scenarios")
    state: State
    scenes: Optional[List[Scene]] = Field(default=None, description="A list of specification for all scenes in the scenario")
    __properties: ClassVar[List[str]] = ["id", "name", "first_scene", "session_complete", "state", "scenes"]

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
        """Create an instance of Scenario from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in scenes (list)
        _items = []
        if self.scenes:
            for _item in self.scenes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['scenes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Scenario from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "first_scene": obj.get("first_scene"),
            "session_complete": obj.get("session_complete"),
            "state": State.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "scenes": [Scene.from_dict(_item) for _item in obj["scenes"]] if obj.get("scenes") is not None else None
        })
        return _obj


