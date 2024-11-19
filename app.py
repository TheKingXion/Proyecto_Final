from flask import Flask, render_template, request
from diccionarios import ES, ENG, FR, ITA, POR

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

@app.route('/dictionary-usage', methods=['GET'])
def dictionary_usage():
    idioma = request.args.get('idioma', 'en')  # Cambiado a 'en' por defecto para usar el diccionario en inglés
    diccionario = diccionarios.get(idioma, diccionarios["en"])  # Usa el diccionario en inglés por defecto
    return render_template('dictionary_usage.html', datos=diccionario, idioma=idioma)

@app.route('/terms/<letter>')
def terms(letter):
    idioma = request.args.get('idioma', 'en')  # Obtén el idioma de la URL (o usa 'en' por defecto)
    diccionario = diccionarios.get(idioma, diccionarios["en"])  # Obtén el diccionario correspondiente
    letter = letter.lower()
    terms = diccionario.get(letter, {})
    return render_template('terms.html', terms=terms, letter=letter.upper())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)