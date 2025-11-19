from flask import Flask, request, render_template
from password_utils import generate_new_passwords

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    passwords = None
    length = 12
    strength = "strong"
    if request.method == "POST":
        try:
            length = int(request.form.get("length", 12))
        except ValueError:
            length = 12
        strength = request.form.get("strength","strong")
        passwords = generate_new_passwords(3, length=length, strength=strength)
    return render_template("index.html", passwords=passwords, length=length, strength=strength)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

