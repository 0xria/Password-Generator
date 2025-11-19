import os
from flask import Flask, request, render_template
from password_utils import generate_new_passwords

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    passwords = None
    length = 12 #default length given
    strength = "strong"

    if request.method == "POST":
        strength = request.form.get("strength", "strong")
        passwords = generate_new_passwords(3, length=length, strength=strength)

    return render_template("index.html", passwords=passwords)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
