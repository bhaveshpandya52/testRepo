from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello World"

if __name__ == '__main__':
   app.run(port="7889")
   #app.run(debug = True)