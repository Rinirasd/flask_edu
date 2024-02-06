from flask import Flask, render_template

app = Flask(__name__)

@app.route("/cats/")
def index() :
    cat_name = "Persik"
    return render_template("cats.html", cat_name = cat_name)


app.run(debug=True)
