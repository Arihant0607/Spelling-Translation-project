from flask import Flask, request, render_template
from Module import *

app = Flask(__name__)

spellcheck = SpellCheck()
trans = Trans()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/spell", methods=["POST", "GET"])
def spelling_check():
    if request.method == "POST":
        text = request.form["text"]
        correct_text = spellcheck.correct_spelling(text)
        return render_template("index.html", corrected_text=correct_text)


@app.route("/grammar", methods=["POST", "GET"])
def grammar_check():
    if request.method == "POST":
        file = request.files["file"]
        file_text = file.read().decode("UTF-8")
        correct_file = spellcheck.correct_spelling(file_text)
        return render_template("index.html", corrected_file=correct_file)


@app.route("/translate", methods=["POST", "GET"])
def translation():
    if request.method == "POST":
        text = request.form["speach"]
        lang = request.form.get("value")
        translate_text = trans.translate_text(text, lang)
        return render_template("index.html", translated_text=translate_text)


if __name__ == "__main__":
    app.run(debug=True)
