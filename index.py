from flask import Flask, render_template, request
import forms

app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

# Routes to Render Something
@app.route('/', methods = ['GET','POST'])
def home():
    sendDate= forms.sendDate(request.form)
    if request.method == 'POST':
        print (sendDate.usuario.data)
    return render_template("home.html",form = sendDate)

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
