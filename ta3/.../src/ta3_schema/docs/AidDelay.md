# AidDelay

Properties related to CASEVAC or MEDEVAC

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay** | **float** | CASEVAC or MEDEVAC timer, in minutes | 
**type** | [**AidTypeEnum**](AidTypeEnum.md) |  | [optional] 
**max_transport** | **int** | Maximum number of casualties that can be transported | [optional] 

## Example

```python
from openapi_client.models.aid_delay import AidDelay

# TODO update the JSON string below
json = "{}"
# create an instance of AidDelay from a JSON string
aid_delay_instance = AidDelay.from_json(json)
# print the JSON string representation of the object
print AidDelay.to_json()

# convert the object into a dict
aid_delay_dict = aid_delay_instance.to_dict()
# create an instance of AidDelay from a dict
aid_delay_form_dict = aid_delay.from_dict(aid_delay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


