#!/bin/bash

# Generate a random string for the content field
content=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13)

# Send a POST request to create a new timeline post
curl -d "name=John&email=john@example.com&content=$content" -X POST http://localhost:5000/api/timeline_post

# Send a GET request to retrieve all timeline posts and check if the random content string is in the response
if curl -s http://localhost:5000/api/timeline_post | grep -q "$content"; then
    echo "Timeline post successfully added"
else
    echo "Error: Timeline post not added"
fi

echo -e "\nTesting POST endpoint...\n"

