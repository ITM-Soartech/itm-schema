# Injury

An injury on a character.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**InjuryTypeEnum**](InjuryTypeEnum.md) |  | 
**location** | [**InjuryLocationEnum**](InjuryLocationEnum.md) |  | 
**severity** | **float** | A numerical indication of the severity of the injury from low (0.0) to high (1.0) | [optional] 
**status** | [**InjuryStatusEnum**](InjuryStatusEnum.md) |  | 

## Example

```python
from openapi_client.models.injury import Injury

# TODO update the JSON string below
json = "{}"
# create an instance of Injury from a JSON string
injury_instance = Injury.from_json(json)
# print the JSON string representation of the object
print Injury.to_json()

# convert the object into a dict
injury_dict = injury_instance.to_dict()
# create an instance of Injury from a dict
injury_form_dict = injury.from_dict(injury_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


