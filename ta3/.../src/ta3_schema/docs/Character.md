# Character

a character in the scene, including injured patients, civilians, medics, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique character ID throughout the scenario | 
**name** | **str** | display name, as in a dashboard | 
**unstructured** | **str** | Natural language, plain text description of the character | 
**unstructured_postassess** | **str** | unstructured description updated after character assessment | [optional] 
**rapport** | **float** | A measure of closeness or affinity towards the player/medic; 0 represents strong dislike, 10 represents very close relationships like family | [optional] 
**demographics** | [**Demographics**](Demographics.md) |  | 
**injuries** | [**List[Injury]**](Injury.md) | A list of Injuries for the character | [optional] 
**vitals** | [**Vitals**](Vitals.md) |  | [optional] 
**visited** | **bool** | whether or not this character has been visited by the ADM in the current scenario | [optional] [default to False]

## Example

```python
from openapi_client.models.character import Character

# TODO update the JSON string below
json = "{}"
# create an instance of Character from a JSON string
character_instance = Character.from_json(json)
# print the JSON string representation of the object
print Character.to_json()

# convert the object into a dict
character_dict = character_instance.to_dict()
# create an instance of Character from a dict
character_form_dict = character.from_dict(character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


