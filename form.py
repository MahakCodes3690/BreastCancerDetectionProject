from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/')
def home():
      return render_template("submissionform.html")
@app.route('/submit',methods=['POST'])
def result():
    name=request.form['name']
    email=request.form['email']
    message=request.form['message']
    return render_template('resultform.html',name=name,email=email,message=message)

if __name__=="__main__":
  app.run(debug=True)