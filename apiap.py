from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
  return "API is running"

@app.route('/hello')
def hello():
  return "Hello, this is hello page"

if __name__=="__main__":
  app.run(host="0.0.0.0",port=5000)
