# ProbeResponses

tag-specific probe responses (choices) for a tagged character

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character_id** | **str** | A valid character ID from the scene | 
**probe_id** | **str** | A valid probe_id from the appropriate TA1 | 
**minimal** | **str** | The probe response to send for a MINIMAL tag | 
**delayed** | **str** | The probe response to send for a DELAYED tag | 
**immediate** | **str** | The probe response to send for a IMMEDIATE tag | 
**expectant** | **str** | The probe response to send for a EXPECTANT tag | 

## Example

```python
from openapi_client.models.probe_responses import ProbeResponses

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeResponses from a JSON string
probe_responses_instance = ProbeResponses.from_json(json)
# print the JSON string representation of the object
print ProbeResponses.to_json()

# convert the object into a dict
probe_responses_dict = probe_responses_instance.to_dict()
# create an instance of ProbeResponses from a dict
probe_responses_form_dict = probe_responses.from_dict(probe_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


