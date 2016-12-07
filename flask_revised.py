from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/response/')
def response_test():
    response = make_response(render_template('index.html', username='Leop0ld'))
    response.headers['X-Parachutes'] = 'parachutes are cool'
    return response


if __name__ == '__main__':
    app.run()
