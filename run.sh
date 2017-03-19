export LOCAL_ROOT=$(pwd)
docker run --network=host -v $LOCAL_ROOT:/var/notebook technoatom/python:latest
