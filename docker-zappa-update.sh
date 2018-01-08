#!/bin/bash
docker run -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_DEFAULT_REGION=us-east-1 -v $(pwd):/var/task --rm mcrowson/zappa-builder bash -c "virtualenv docker_env && source docker_env/bin/activate && pip install -r requirements.txt && zappa update dev && rm -rf docker_env"
