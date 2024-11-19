from flask import Flask, render_template
from diccionarios import ES, ENG, FR, ITA, POR
import requests

app = Flask(__name__)

diccionarios = {
    "es": ES.diccionario_es,
    "en": ENG.diccionario_eng,
    #"fr": FR.diccionario_fr,
    "it": ITA.diccionario_ita,
    "pt": POR.diccionario_por,
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

@app.route('/dictionary-usage', methods=['GET'])
def dictionary_usage():
    idioma = request.args.get('idioma', 'es')  # Obtén el idioma de la URL (o usa 'es' por defecto)
    diccionario = diccionarios.get(idioma, diccionarios["es"])  # Obtén el diccionario correspondiente
    return render_template('dictionary_usage.html', datos=diccionario, idioma=idioma)  # Pasa los datos al HTML


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)