#!/bin/bash
# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Use curl to send a GET request to the specified URL and display the body only for 200 status code
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [ "$response" -eq 200 ]; then
    curl -s "$url"
else
    echo "Error: HTTP Status Code $response"
fi
