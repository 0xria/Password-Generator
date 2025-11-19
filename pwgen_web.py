# pwgen_web.py
from flask import Flask, request, render_template_string
from password_utils import generate_new_passwords

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>Password Generator</title>
<h2>Password Generator</h2>
<form method="post">
  Length: <input type="number" name="length" value="{{length}}" min="1"> &nbsp;
  Strength:
  <select name="strength">
    <option value="weak" {% if strength=='weak' %}selected{% endif %}>weak</option>
    <option value="medium" {% if strength=='medium' %}selected{% endif %}>medium</option>
    <option value="strong" {% if strength=='strong' %}selected{% endif %}>strong</option>
  </select>
  <button type="submit">Generate 3</button>
</form>

{% if passwords %}
  <h3>Suggestions</h3>
  <ul>
  {% for p in passwords %}
    <li><code>{{p}}</code></li>
  {% endfor %}
  </ul>
{% endif %}
"""

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
    return render_template_string(TEMPLATE, passwords=passwords, length=length, strength=strength)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
