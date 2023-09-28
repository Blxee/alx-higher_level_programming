#!/bin/bash
# 1. cURL to the end
(( $(curl -sIX GET $1 | head -1 | cut -d' ' -f2) == 200 )) && curl -sX GET $1
