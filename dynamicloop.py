from flask import Flask,render_template
app=Flask(__name__)
@app.route('/shop/<user>')
def home(user):
    fruit_list=['mango','pineapple','strawbeery','guava']
    return render_template('inherit.html',fruits=fruit_list,user=user)

if __name__ == "__main__":
    app.run(debug=True)
