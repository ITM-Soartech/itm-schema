# Skills

A skill possessed by a character at a certain level of proficiency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill_type** | [**SkillTypeEnum**](SkillTypeEnum.md) |  | 
**level** | **float** | the level of expertise (from 0-10) the character has in the skill | 

## Example

```python
from openapi_client.models.skills import Skills

# TODO update the JSON string below
json = "{}"
# create an instance of Skills from a JSON string
skills_instance = Skills.from_json(json)
# print the JSON string representation of the object
print Skills.to_json()

# convert the object into a dict
skills_dict = skills_instance.to_dict()
# create an instance of Skills from a dict
skills_form_dict = skills.from_dict(skills_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

