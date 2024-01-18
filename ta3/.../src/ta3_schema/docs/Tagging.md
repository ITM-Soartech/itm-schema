# Tagging

Scene-level tagging configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether tagging is enabled for the scene | [optional] 
**repeatable** | **bool** | Whether probe responses should be sent each time a new tag is applied | [optional] 
**probe_responses** | [**List[ProbeResponses]**](ProbeResponses.md) | A list of probe responses to send TA1 for each character-tag combination | [optional] 
**reference** | **int** | Re-use the tagging configuration from the specified scene index | [optional] 

## Example

```python
from openapi_client.models.tagging import Tagging

# TODO update the JSON string below
json = "{}"
# create an instance of Tagging from a JSON string
tagging_instance = Tagging.from_json(json)
# print the JSON string representation of the object
print Tagging.to_json()

# convert the object into a dict
tagging_dict = tagging_instance.to_dict()
# create an instance of Tagging from a dict
tagging_form_dict = tagging.from_dict(tagging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


