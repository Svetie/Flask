from flask import Flask, render_template  # added render_template!
app = Flask(__name__)


# http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def eight():
    lines=8
    squares=8
    print('eight by eight')
    return render_template('index.html', lines=lines, squares=squares)
# http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<lines>')
def four(lines):
    squares=8
    return render_template('index.html', lines=int(lines), squares=squares)
@app.route('/<lines>/<squares>')
def colorChange(lines, squares):
    return render_template('index.html', lines=int(lines), squares=int(squares))
if __name__=="__main__":
    app.run(debug=True)