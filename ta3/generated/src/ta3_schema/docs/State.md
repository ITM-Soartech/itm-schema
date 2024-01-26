# State

the current tactical & environmental state of the scenario and of its characters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | Natural language, plain text description of a scene&#39;s state | 
**elapsed_time** | **float** | the elapsed time (in minutes) since the scenario started | [optional] 
**scenario_complete** | **bool** | set to true if the scenario is complete; subsequent calls involving that scenario will return an error code | [optional] 
**mission** | [**Mission**](Mission.md) |  | [optional] 
**environment** | [**Environment**](Environment.md) |  | 
**threat_state** | [**ThreatState**](ThreatState.md) |  | [optional] 
**supplies** | [**List[Supplies]**](Supplies.md) | A list of supplies available to the medic | 
**characters** | [**List[Character]**](Character.md) | A list of characters in the scene, including injured patients, civilians, medics, etc. | 

## Example

```python
from openapi_client.models.state import State

# TODO update the JSON string below
json = "{}"
# create an instance of State from a JSON string
state_instance = State.from_json(json)
# print the JSON string representation of the object
print State.to_json()

# convert the object into a dict
state_dict = state_instance.to_dict()
# create an instance of State from a dict
state_form_dict = state.from_dict(state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


