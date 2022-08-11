from flask import Flask, jsonify
from functions import load_candidates, get_all, get_by_pk, get_by_skill

answers = ''
for item in load_candidates():
    answers += f"<pre>Имя кандидата {item['name']}\nПозиция кандидата {item['position']}\nНавыки через запятую {item['skills']}</pre>"
app = Flask(__name__)


@app.route("/")
def page_index():
    return answers


@app.route("/candidates/<int:uid>")
def candidates_index(uid):
    profile = ""
    profile += f"<pre>{get_by_pk(uid)}</pre>"
    return profile


@app.route("/skills/<uid>")
def skills_index(uid):
    skills = ''
    skills += f"<pre>{get_by_skill(uid.lower())} </pre>"
    return skills


app.run()
