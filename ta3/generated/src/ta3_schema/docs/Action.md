# Action

Details for how a given action maps to a probe response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | A unique action ID within the scenario | 
**action_type** | [**ActionTypeEnum**](ActionTypeEnum.md) |  | 
**unstructured** | **str** | Natural language, plain text description of the action | 
**repeatable** | **bool** | Whether or not this action should remain after it&#39;s selected by an ADM | [optional] [default to False]
**character_id** | **str** | The ID of the character being acted upon | [optional] 
**parameters** | **Dict[str, str]** | key-value pairs containing additional [action-specific parameters](https://github.com/NextCenturyCorporation/itm-evaluation-client?tab&#x3D;readme-ov-file#available-actions) | [optional] 
**probe_id** | **str** | A valid probe_id from the appropriate TA1 | [optional] 
**choice** | **str** | A valid choice for the specified probe_id | [optional] 
**justification** | **str** | A justification of the action taken | [optional] 
**kdma_association** | **Dict[str, float]** | KDMA associations for this choice, if provided by TA1 | [optional] 
**condition_semantics** | [**SemanticTypeEnum**](SemanticTypeEnum.md) |  | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 

## Example

```python
from openapi_client.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print Action.to_json()

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_form_dict = action.from_dict(action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


