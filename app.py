from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/developers')
def developers():
    return render_template('developers.html')

@app.route('/select-language')
def select_language():
    return render_template('select_language.html')

@app.route('/dictionary-usage')
def dictionary_usage():
    return render_template('dictionary_usage.html')

if __name__ == '__main__':
    app.run(debug=True)