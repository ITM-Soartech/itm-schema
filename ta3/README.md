# Generate models from TA3 Schema
Requires Docker.
To run:
  - Download the newest version of the ta3 OpenAPI specification
  - Move it to `./current_schema.yaml`
  - Run `./ta3/update_ta3_schema.sh`

This will generate new models and put them in `itm_schema/src/ta3_schema`.
