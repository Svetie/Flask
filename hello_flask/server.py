# This will be our "server" file where we will set up all of our routes to handle requests
# must do this for every route that you want to add to our application.
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
    # if the client requests localhost:5000/, the hello_world function will run.
@app.route('/success')
def success():
    return "success"
    # if the client requests localhost:5000/success, the success function will run.
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
                            # http://localhost:5000/hello/svetlana
def hello(name):
    print(name)
    return "Hello, " + name
@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

# run application from command prompt:
# (hello_flask) hello_flask $ python server.py

# Now if you navigate to localhost:5000/ in your browser, you should see the message "Hello World!"

# We imported the Flask class. You will need this line in every application you build with Flask.
# We made an instance of the Flask class called "app". You will need this line in every application you build with Flask.
# We set up a routing rule using the "@" decorator with the route method: @app.route("/route_string"). The routing rule is associated with the function immediately following it.
# Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.