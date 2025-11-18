from flask import Flask
app=Flask(__name__)

@app.route('/index/<name>')
def home(name):
   return "my name is "+name

if __name__=="__main__":
    app.run(debug=True)