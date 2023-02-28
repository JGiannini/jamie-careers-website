from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello, Jamie!!!"


if __name__ == '__main__':
  app.run(host='0.0.0.0',
          debug=True)  #Lets us run it locally on local host 0.0.0.0

