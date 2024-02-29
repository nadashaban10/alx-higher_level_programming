#!/bin/bash
# Get the size of file
# -s make it in silence
# using pipe to take the pre output to next- wc to count 
curl -s "$1" | wc -c
