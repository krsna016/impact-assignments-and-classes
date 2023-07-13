from flask import Flask
flask = Flask(__name__) # Object of flask

"""To run this just use the URL:http://192.168.29.116:5000"""
@flask.route("/") # Decorator
def hello_world():
    return "<h1>Hello world!</h1>"

"""To run this just use the URL:http://192.168.29.116:5000/123"""
@flask.route("/123") # Decorator
def hello_world_1():
    return "<h1>Hello world 1!</h1>"

"""To run this just use the URL:http://192.168.29.116:5000/abc"""
@flask.route("/abc") # Decorator
def hello_world_2():
    return "<h1>Hello world 2!</h1>"

"""To run this just use the URL:http://192.168.29.116:5000/abc"""
@flask.route("/test")
def test_func():
    return(f"This is my function to run apps -> {5+9}")

if __name__ == "__main__":
    flask.run(host="0.0.0.0")