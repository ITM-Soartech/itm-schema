# ConditionsCharacterVitalsInner

The minimum vitals of the specified character

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character_id** | **str** | The ID of the character in question | [optional] 
**vitals** | [**Vitals**](Vitals.md) |  | [optional] 

## Example

```python
from openapi_client.models.conditions_character_vitals_inner import ConditionsCharacterVitalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionsCharacterVitalsInner from a JSON string
conditions_character_vitals_inner_instance = ConditionsCharacterVitalsInner.from_json(json)
# print the JSON string representation of the object
print ConditionsCharacterVitalsInner.to_json()

# convert the object into a dict
conditions_character_vitals_inner_dict = conditions_character_vitals_inner_instance.to_dict()
# create an instance of ConditionsCharacterVitalsInner from a dict
conditions_character_vitals_inner_form_dict = conditions_character_vitals_inner.from_dict(conditions_character_vitals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


