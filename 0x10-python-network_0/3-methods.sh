#!/bin/bash
# 3. cURL only methods
curl -sIX OPTIONS $1 | grep 'Allow:' | cut -d' ' -f2-
