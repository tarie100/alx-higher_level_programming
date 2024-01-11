#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
read -p
response = $(curl -s -o /dev/null -w "%{size_download}" "$url")
echo "Size of the response body: $response bytes"
