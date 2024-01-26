# Threat

threats in the environment that could affect decision-making

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threat_type** | **str** | the type or nature of the threat, may become a controlled vocabulary | 
**severity** | **float** | how severe/imminent the threat is, from 0 (no threat) to 1 (max severity) | 

## Example

```python
from openapi_client.models.threat import Threat

# TODO update the JSON string below
json = "{}"
# create an instance of Threat from a JSON string
threat_instance = Threat.from_json(json)
# print the JSON string representation of the object
print Threat.to_json()

# convert the object into a dict
threat_dict = threat_instance.to_dict()
# create an instance of Threat from a dict
threat_form_dict = threat.from_dict(threat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


