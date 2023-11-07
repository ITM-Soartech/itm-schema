Central location for pydantic schema that can be included in other projects without including unneccesary code.

Might mean that some tests will need to be done outside of this directory when working with project specific code.

Demo folder contains data to validate schema.

## Installing

Note: It is recommended that you use a python3.10 virtual environment:

```bash
python3.10 -m venv env
source env/bin/activate
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

## Running Tests

To run tests, install the package (see above) then run unittest discover

```bash
cd itm-schema
python -m unittest discover
```
