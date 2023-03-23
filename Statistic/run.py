from flask import Flask,render_template
app=Flask(__name__,template_folder='templates')
app.debug = True

@app.route("/")
def helloworld():
    return "<p>Hello, World!</p>"
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/image")
def image():
    return render_template('image.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8080)