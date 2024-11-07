#!/bin/bash

git pull origin main

echo "Estado actual de Git:"
git status --short

git add .

echo "Introduce el mensaje del commit:"
read mensaje_commit

git commit -m "$mensaje_commit"

git push origin main

echo "Últimos commits:"
git log --oneline --max-count=5

echo "Operación de Git completada con éxito."
