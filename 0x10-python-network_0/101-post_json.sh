#!/bin/bash
# 8. cURL a JSON file
curl -sX POST -d "$(cat $2)" -H "Content-Type: application/json" "$1"
