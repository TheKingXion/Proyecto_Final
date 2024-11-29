from por import diccionario_por
import json

# Función recursiva para ordenar el diccionario alfabéticamente
def ordenar_diccionario(diccionario):
    # Ordenar las claves del diccionario
    diccionario_ordenado = {}
    for clave in sorted(diccionario.keys()):
        valor = diccionario[clave]
        # Si el valor es un diccionario, aplicar la ordenación recursivamente
        if isinstance(valor, dict):
            diccionario_ordenado[clave] = ordenar_diccionario(valor)
        else:
            diccionario_ordenado[clave] = valor
    return diccionario_ordenado

# Ordenar el diccionario
diccionario_ordenado = ordenar_diccionario(diccionario_por)

# Escribir el diccionario ordenado en un archivo JSON
with open('diccionario_ordenado.json', 'w', encoding='utf-8') as archivo:
    json.dump(diccionario_ordenado, archivo, ensure_ascii=False, indent=4)

print("Diccionario ordenado escrito en 'diccionario_ordenado.json'")

