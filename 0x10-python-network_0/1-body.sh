#!/bin/bash
# a script that displays body of a 200 status code response
curl -s "$1" -X GET -L
