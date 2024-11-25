from por import diccionario_por
import json


# Ordenar el diccionario alfabéticamente por las claves principales
diccionario_ordenado = {k: v for k, v in sorted(diccionario_por.items())}

# Escribir el diccionario ordenado en un archivo JSON
with open('diccionario_ordenado.json', 'w', encoding='utf-8') as archivo:
    json.dump(diccionario_ordenado, archivo, ensure_ascii=False, indent=4)

print("Diccionario ordenado escrito en 'diccionario_ordenado.json'")
