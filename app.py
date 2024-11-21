from flask import Flask, render_template, request
from diccionarios import es, eng, ita, por

app = Flask(__name__)

diccionarios = {
    "es": es.diccionario_es,
    "en": eng.diccionario_eng,
    "it": ita.diccionario_ita,
    "pt": por.diccionario_por,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/developers')
def developers():
    return render_template('developers.html')

@app.route('/dictionary-usage', methods=['GET'])
def dictionary_usage():
    idioma = request.args.get('idioma', 'es')  # Cambiado a 'es' por defecto
    diccionario = diccionarios.get(idioma, diccionarios["es"])  # Usa el diccionario en español por defecto
    return render_template('dictionary_usage.html', datos=diccionario, idioma=idioma)

@app.route('/terms/<letter>')
def terms(letter):
    idioma = request.args.get('idioma', 'es')  # Obtén el idioma de la URL (o usa 'es' por defecto)
    diccionario = diccionarios.get(idioma, diccionarios["es"])  # Obtén el diccionario correspondiente
    letter = letter.lower()
    terms = diccionario.get(letter, {})
    return render_template('terms.html', terms=terms, letter=letter.upper())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)