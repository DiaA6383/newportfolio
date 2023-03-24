#!/bin/bash

# Generate a random string for the content field
content=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13)

# Send a POST request to create a new timeline post
curl -d "name=John&email=john@example.com&content=$content" -X POST http://localhost:5000/api/timeline_post

curl http://localhost:5000/api/timeline_post
{"timeline_posts":[]}

curl -X POST http://localhost:5000/api/timeline_post -d 'name=Wei&email=wei.he@mlh.io&content=Just learned how to run a docker container!' '{"content":"Just Learned how to run a docker container!","created_at":"Fri, 20 May 2022 04:57:35 GMT","email":"wei.he@mlh.io","id":1,"name":"Wei"}'

# Send a GET request to retrieve all timeline posts and check if the random content string is in the response
if curl -s http://localhost:5000/api/timeline_post | grep -q "$content"; then
    echo "Timeline post successfully added"
else
    echo "Error: Timeline post not added"
fi

echo -e "\nTesting POST endpoint...\n"

