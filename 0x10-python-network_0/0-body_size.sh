#!/bin/bash
# Get the size of file 
curl -s "$1" | wc -c
