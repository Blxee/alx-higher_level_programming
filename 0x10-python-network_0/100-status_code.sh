#!/bin/bash
# 7. Only status code
curl -sIw "%{http_code}" -o /dev/null -X GET $1
