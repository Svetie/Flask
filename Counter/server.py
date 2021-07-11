from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret' #set a secret key for security purposes
# our index route will handle rendering our form

@app.route('/')
def index():
    # request.session['counter'] = 0 #Set the value
    # counter = request.session.get('counter', 0) #Read the value else read a default one
    # counter =  session.get('counter', None)
    if 'counter' in session:
        print('key exists!')
        print(session['counter'])
        print(session)
        counter=int(session['counter'])
        counter = int(counter) + 1
        session['counter'] = str(counter)
        print(session['counter'])
    else:
        print("key 'key_name' does NOT exist")
        session['counter'] = '1'

    return render_template("index.html", counter=session['counter'])

@app.route('/destroy_session', methods=['GET'])
def destroy():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

