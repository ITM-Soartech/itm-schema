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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from .action_type_enum import ActionTypeEnum
from .conditions import Conditions
from .semantic_type_enum import SemanticTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class Action(BaseModel):
    """
    Details for how a given action maps to a probe response
    """ # noqa: E501
    action_id: StrictStr = Field(description="A unique action ID within the scenario")
    action_type: ActionTypeEnum
    unstructured: StrictStr = Field(description="Natural language, plain text description of the action")
    repeatable: Optional[StrictBool] = Field(default=False, description="Whether or not this action should remain after it's selected by an ADM")
    character_id: Optional[StrictStr] = Field(default=None, description="The ID of the character being acted upon")
    parameters: Optional[Dict[str, StrictStr]] = Field(default=None, description="key-value pairs containing additional [action-specific parameters](https://github.com/NextCenturyCorporation/itm-evaluation-client?tab=readme-ov-file#available-actions)")
    probe_id: Optional[StrictStr] = Field(default=None, description="A valid probe_id from the appropriate TA1")
    choice: Optional[StrictStr] = Field(default=None, description="A valid choice for the specified probe_id")
    justification: Optional[StrictStr] = Field(default=None, description="A justification of the action taken")
    kdma_association: Optional[Dict[str, Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]]] = Field(default=None, description="KDMA associations for this choice, if provided by TA1")
    condition_semantics: Optional[SemanticTypeEnum] = None
    conditions: Optional[Conditions] = None
    __properties: ClassVar[List[str]] = ["action_id", "action_type", "unstructured", "repeatable", "character_id", "parameters", "probe_id", "choice", "justification", "kdma_association", "condition_semantics", "conditions"]

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
        """Create an instance of Action from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of conditions
        if self.conditions:
            _dict['conditions'] = self.conditions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Action from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action_id": obj.get("action_id"),
            "action_type": obj.get("action_type"),
            "unstructured": obj.get("unstructured"),
            "repeatable": obj.get("repeatable") if obj.get("repeatable") is not None else False,
            "character_id": obj.get("character_id"),
            "parameters": obj.get("parameters"),
            "probe_id": obj.get("probe_id"),
            "choice": obj.get("choice"),
            "justification": obj.get("justification"),
            "kdma_association": obj.get("kdma_association"),
            "condition_semantics": obj.get("condition_semantics"),
            "conditions": Conditions.from_dict(obj["conditions"]) if obj.get("conditions") is not None else None
        })
        return _obj


