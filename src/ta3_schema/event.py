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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from .event_type_enum import EventTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class Event(BaseModel):
    """
    a unit of structured communication from scenario to ADM
    """ # noqa: E501
    unstructured: StrictStr = Field(description="Natural language, plain text description of the event")
    type: EventTypeEnum
    source: Optional[StrictStr] = Field(default=None, description="The 'subject' of the event; can be a character `id` or an `EntityTypeEnum`")
    object: Optional[StrictStr] = Field(default=None, description="The 'object' of the event; can be a character `id` or an `EntityTypeEnum`")
    when: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="indicates when (in minutes) the event happened (negative value) or is expected to happen (positive value); omit if zero (event happens now)")
    action_id: Optional[StrictStr] = Field(default=None, description="An action ID from among the available actions")
    relevant_state: Optional[List[StrictStr]] = Field(default=None, description="An array of relevant state for the Event")
    __properties: ClassVar[List[str]] = ["unstructured", "type", "source", "object", "when", "action_id", "relevant_state"]

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
        """Create an instance of Event from a JSON string"""
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
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "unstructured": obj.get("unstructured"),
            "type": obj.get("type"),
            "source": obj.get("source"),
            "object": obj.get("object"),
            "when": obj.get("when"),
            "action_id": obj.get("action_id"),
            "relevant_state": obj.get("relevant_state")
        })
        return _obj


