#!/bin/bash
# 1. cURL to the end
code="$(curl -sIX GET $1 | head -1 | cut -d' ' -f2)"
if (( code == 200 ))
then
  curl -sX GET $1
fi
