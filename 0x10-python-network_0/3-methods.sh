#!/bin/bash
# Use curl to send an OPTIONS request to the specified URL and display allowed methods
curl -s -I -X OPTIONS "$1" | grep -i 'allow' | awk '{print $2}'
