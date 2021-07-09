from flask import Flask, render_template  # added render_template!
app = Flask(__name__)

@app.route('/play')
def index():
    print('inside index url')
    return render_template('index.html')
@app.route('/play/<number>')
def repeat(number):
    return render_template('index.html', times=int(number))
@app.route('/play/<number>/<color>')
def colorChange(number, color):
    return render_template('index.html', times=int(number), color=color)
if __name__=="__main__":
    app.run(debug=True)