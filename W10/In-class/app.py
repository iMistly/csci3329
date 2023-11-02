from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/type')
def type():
    return "stinky cheese"

@app.route('/hello/<name>')
def hello(name):
    listOfNames = [name, "billy", "ben"]
    return render_template('greet.html', name = name, nameList = listOfNames)

if (__name__ == "__main__"):
    app.run(debug=True)