from flask import flask, render_template

app = flask.Flask (__name__)

@app.route('/')
def hello_world():
    return render_template('calculate.html')

if __name__ == '__main__':

    app.run(host='61.42.176.8', port='5000')