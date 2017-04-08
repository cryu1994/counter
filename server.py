from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ME'

@app.route("/")
def index():
    if not "counter" in session:
        session["counter"] = 1
    else:
        session["counter"] += 2
    return render_template('index.html', counter = session["counter"])
@app.route('/count', methods=["POST"])
def count():

    return redirect('index.html')
app.run(debug=True)
