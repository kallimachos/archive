from bottle import route, run, template

@route('/hello')
def hello():
    return "<h1>Hello World!</h1>"

@route('/hello/<name>')
def index(name):
    return template('hello_name', name=name)

run(host='0.0.0.0', port=8080)