from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' #set a secret key for security purposes
# our index route will handle rendering our form


@app.route('/')
def index():

    return render_template("index.html")

@app.route('/save', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/result")

# adding this method
@app.route("/result")
def show_user():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)

