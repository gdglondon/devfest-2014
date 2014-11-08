#!/bin/bash

# Build pages
jekyll build

# Generate api.json
./api.py

# deploy to App Engine
appcfg.py update .
