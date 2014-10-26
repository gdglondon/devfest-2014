#!/bin/bash

# Build pages
jekyll build

# deploy to App Engine
appcfg.py update .
