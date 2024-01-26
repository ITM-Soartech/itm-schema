# Vitals

Vital levels and other indications of health

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conscious** | **bool** | whether or not the character appears to be conscious | [optional] 
**avpu** | [**AvpuLevelEnum**](AvpuLevelEnum.md) |  | [optional] 
**ambulatory** | **bool** | whether or not the character can walk | [optional] 
**mental_status** | [**MentalStatusEnum**](MentalStatusEnum.md) |  | [optional] 
**breathing** | [**BreathingLevelEnum**](BreathingLevelEnum.md) |  | [optional] 
**hrpmin** | **int** | heart rate in beats per minute | [optional] 
**spo2** | **float** | blood oxygen level (percentage) | [optional] 

## Example

```python
from openapi_client.models.vitals import Vitals

# TODO update the JSON string below
json = "{}"
# create an instance of Vitals from a JSON string
vitals_instance = Vitals.from_json(json)
# print the JSON string representation of the object
print Vitals.to_json()

# convert the object into a dict
vitals_dict = vitals_instance.to_dict()
# create an instance of Vitals from a dict
vitals_form_dict = vitals.from_dict(vitals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


