from flask import Flask
from flask import request

flask = Flask(__name__) # Object of flask

"""To run this just use the URL:http://192.168.29.116:5000/test/test1"""
"""To run this just use the URL with inputted data:http://192.168.29.116:5000/test/test1?x=Anurag+Pareek"""
@flask.route("/test/test1") # Decorator
def test():
    data = request.args.get('x')
    return f"This is data input from my URL: {data}"

if __name__ == "__main__":
    flask.run(host="0.0.0.0")