#!/usr/bin/env bash

# Turn on bash job control
#set -m


# Start Starlette Server
uvicorn main:app 

# Bring back primary process
#fg %1

