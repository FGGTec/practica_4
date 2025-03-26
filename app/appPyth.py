from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/inicio/")
def i():
    return render_template("public/index.html")
@app.route("/sobre_mi/")
def sm():
    return render_template("public/about.html")
@app.route("/portafolio/")
def p():
    return render_template("public/portfolio.html")
@app.route("/blog/")
def b():
    return render_template("public/blog.html")
@app.route("/contacto/")
def c():
    return render_template("public/contact.html")