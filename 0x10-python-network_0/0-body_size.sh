#!/bin/bash
#  a Bash script that displays the size of the body of an HTTP response
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
