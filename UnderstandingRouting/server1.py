
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# 1 say hello world
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
# 2 localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def say_dojo():
    return 'Dojo!'
# 3 print hi plus name
@app.route('/say/<name>')
def hi_name(name):
    return 'Hi ' + name
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    return word * int(num)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)