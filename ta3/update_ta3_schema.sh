#! /bin/bash

current_schema_url='https://raw.githubusercontent.com/NextCenturyCorporation/itm-scenario-validator/main/api_files/api.yaml'
script_dir=$(dirname $0) # directory containing this script
infile="${script_dir}/current_schema.yaml" # path to ta3 OpenAPI schema yaml
wget -O ${infile} ${current_schema_url} # download latest schema yaml
outdir="${script_dir}/../src/ta3_schema/" # path to put updated code for models 
tmpdir='tmp' # temporary directory for intermediate post-processing

# run openapi generator to get python client code + pydantic models
docker run --rm \
	-u ${UID} \
    -v $PWD:/local openapitools/openapi-generator-cli generate \
    -i /local/${infile} \
    -g python \
    -o /local/${tmpdir}

# we only want the schema for the pydantic models, not the code
# for the api client / boiler plate code for python project
# (setup.py, pyproject.toml, etc)
# extract 
models_dir=${tmpdir}/openapi_client/models
for f in $(ls -1 ${models_dir} | grep '\.py$'); do
	sed -i 's/openapi_client.models//' ${models_dir}/${f};
done

# clear old models so the new ones can replace them
if [ -d ${outdir} ]; then
	rm -rf ${outdir}
fi

# move new models into src directory
mv ${models_dir} ${outdir}

# remove temporary directory and schema yaml file
rm -rf ${tmpdir} ${infile}
