#!/bin/bash

# Actualizar el repositorio local
echo "Actualizando el repositorio local..."
git pull origin main

# Verificar si hubo conflictos durante el pull
if [ $? -ne 0 ]; then
  echo "Error durante 'git pull'. Revisa los conflictos de merge e intenta nuevamente."
  exit 1
fi

# Mostrar el estado actual de Git
echo "Estado actual de Git:"
git status --short

# Añadir cambios al staging
echo "Añadiendo cambios al staging..."
git add .

# Pedir mensaje de commit
echo "Introduce el mensaje del commit:"
read mensaje_commit

# Realizar el commit
git commit -m "$mensaje_commit"
if [ $? -ne 0 ]; then
  echo "Error al realizar el commit. Verifica si hay cambios para commitear."
  exit 1
fi

# Empujar los cambios al repositorio remoto
echo "Enviando cambios al repositorio remoto..."
git push origin main
if [ $? -ne 0 ]; then
  echo "Error al hacer 'git push'. Verifica tu conexión o permisos."
  exit 1
fi

# Mostrar los últimos commits
echo "Últimos commits:"
git log --oneline --max-count=5

echo "Operación de Git completada con éxito."
