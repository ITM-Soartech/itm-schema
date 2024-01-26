# Scene

the specification for a scene in the scenario

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The order the scene appears in the scenario | 
**state** | [**State**](State.md) |  | [optional] 
**end_scenario_allowed** | **bool** | Whether ADMs can end the scenario during this scene | 
**probe_config** | [**List[ProbeConfig]**](ProbeConfig.md) | TA1-provided probe configuration, ignored by TA3 | [optional] 
**tagging** | [**Tagging**](Tagging.md) |  | [optional] 
**action_mapping** | [**List[Action]**](Action.md) | List of actions with details of how those actions map to probe responses | 
**restricted_actions** | [**List[ActionTypeEnum]**](ActionTypeEnum.md) | List of actions that will be excluded from get_available_actions | [optional] 
**transition_semantics** | [**SemanticTypeEnum**](SemanticTypeEnum.md) |  | [optional] 
**transitions** | [**Conditions**](Conditions.md) |  | [optional] 

## Example

```python
from openapi_client.models.scene import Scene

# TODO update the JSON string below
json = "{}"
# create an instance of Scene from a JSON string
scene_instance = Scene.from_json(json)
# print the JSON string representation of the object
print Scene.to_json()

# convert the object into a dict
scene_dict = scene_instance.to_dict()
# create an instance of Scene from a dict
scene_form_dict = scene.from_dict(scene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


