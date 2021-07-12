from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' #set a secret key for security purposes
# our index route will handle rendering our form


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def check_nimber():
    session['resultClass']=''
    session['text']=''
    rand = random.randint(1, 2)
    print("random number", rand)
    session['random'] = rand
    session['guess'] = request.form['guess']
    print("user input", session['guess'])
    if(int(session['random']) == int(session['guess'])):
        session['resultClass']='right'
    elif(int(session['guess']) < int(session['random'])):
        session['resultClass']='tooLow'
    elif(int(session['guess']) > int(session['random'])):
        session['resultClass']='tooHigh'
    return redirect("/")

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)

