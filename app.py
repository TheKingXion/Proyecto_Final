from flask import Flask, render_template, request, jsonify
import json
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

@app.route('/suggest-term')
def suggest_term_page():
    return render_template('suggest-term.html')

@app.route('/api/suggest-term', methods=['POST'])
def suggest_term():
    data = request.json
    
    # Guardar la sugerencia en un archivo
    with open('sugerencias.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')
    
    return jsonify({"message": "Sugerencia guardada con éxito"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)