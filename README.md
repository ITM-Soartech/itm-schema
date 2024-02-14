Central location for pydantic schema that can be included in other projects without including unneccesary code.

Might mean that some tests will need to be done outside of this directory when working with project specific code.

Demo folder contains data to validate schema.

## Installing

Note: It is recommended that you use python >= 3.10.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

To install the package and dependencies:


```bash
cd itm-schema
pip install -e .
```

Then import the package as normal

```
$ python -q
>>> import itm_schema
>>> from itm_schema.ml_pipeline import KDMAMeasurement
>>> KDMAMeasurement
<class 'itm_schema.ml_pipeline.KDMAMeasurement'>
```

# Updating scenario schema
We have adopted the TA3 schema for scenario objects (scenario, scene, action, supplies, etc.) TA3 provides an OpenAPI yaml specification for this schema, which can be used to generate pydantic classes for each object in the schema. To update the schema, download the newest version of the ta3 OpenAPI specification, move it to `ta3/current_schema.yaml`, and run `bash ta3/update_ta3_schema.sh`. This will generate new models and put them in `src/ta3_schema`.