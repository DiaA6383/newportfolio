#!/bin/bash

cd newportoflio/
# Fetch latest changes from main branch and reset to latest commit
git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build