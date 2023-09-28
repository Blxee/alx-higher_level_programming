#!/bin/bash
# 7. Only status code
curl -sIX GET $1 | head -1 | cut -d' ' -f2
