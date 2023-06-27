from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola Mundo!'

@app.route('/dojo')
def dojo():
    return '¡Dojo!'

@app.route('/say/<string:name>')
def say_name(name):
    return '¡Hola, {}!'.format(name)

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    return word * num

@app.errorhandler(404)
def page_not_found(error):
    return '¡Lo siento! No hay respuesta. Inténtalo otra vez.'

if __name__ == '__main__':
    app.run(debug=True)
