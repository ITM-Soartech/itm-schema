# ThreatState

Description of the current threat to the characters, including the medic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | Natural language, plain text description of environmental threats | 
**threats** | [**List[Threat]**](Threat.md) | A list of pairs of threat types with a numeric severity indicator | 

## Example

```python
from openapi_client.models.threat_state import ThreatState

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatState from a JSON string
threat_state_instance = ThreatState.from_json(json)
# print the JSON string representation of the object
print ThreatState.to_json()

# convert the object into a dict
threat_state_dict = threat_state_instance.to_dict()
# create an instance of ThreatState from a dict
threat_state_form_dict = threat_state.from_dict(threat_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


