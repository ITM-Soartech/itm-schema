# Scenario

a triage scenario requiring decisions by a medic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | a globally unique id for the scenario | 
**name** | **str** | human-readable scenario name, not necessarily unique | 
**session_complete** | **bool** | set to true if the session is complete; that is, there are no more scenarios | [optional] 
**state** | [**State**](State.md) |  | 
**scenes** | [**List[Scene]**](Scene.md) | A list of specification for all scenes in the scenario | [optional] 

## Example

```python
from openapi_client.models.scenario import Scenario

# TODO update the JSON string below
json = "{}"
# create an instance of Scenario from a JSON string
scenario_instance = Scenario.from_json(json)
# print the JSON string representation of the object
print Scenario.to_json()

# convert the object into a dict
scenario_dict = scenario_instance.to_dict()
# create an instance of Scenario from a dict
scenario_form_dict = scenario.from_dict(scenario_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


