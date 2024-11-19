from flask import Flask, render_template
from diccionarios import es, eng, fr, ita, por
import requests

app = Flask(__name__)

diccionarios = {
    "es": es.diccionario,
    "en": eng.diccionario,
    "fr": fr.diccionario,
    "it": ita.diccionario,
    "pt": por.diccionario,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/developers')
def developers():
    return render_template('developers.html')

@app.route('/select-language')
def select_language():
    return render_template('select_language.html')

@app.route('/dictionary-usage', methods=['GET', 'POST'])
def dictionary_usage():
    # Captura el idioma seleccionado (por defecto español)
    idioma = request.args.get('idioma', 'es')
    # Obtén el diccionario correspondiente
    diccionario = diccionarios.get(idioma, diccionarios["es"])
    # Renderiza la plantilla y pasa los datos
    return render_template('dictionary_usage.html', datos=diccionario, idioma=idioma)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)