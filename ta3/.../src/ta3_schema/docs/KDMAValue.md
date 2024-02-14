# KDMAValue

a KDMA and its value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kdma** | **str** | KDMA name | 
**value** | **float** | target alignment value | 

## Example

```python
from openapi_client.models.kdma_value import KDMAValue

# TODO update the JSON string below
json = "{}"
# create an instance of KDMAValue from a JSON string
kdma_value_instance = KDMAValue.from_json(json)
# print the JSON string representation of the object
print KDMAValue.to_json()

# convert the object into a dict
kdma_value_dict = kdma_value_instance.to_dict()
# create an instance of KDMAValue from a dict
kdma_value_form_dict = kdma_value.from_dict(kdma_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


