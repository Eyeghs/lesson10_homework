# Сперва импортируем Flask

from flask import Flask
from utils import get_all, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route("/")
def all_candidates():
    candidates = get_all()
    formatted_candidates = []

    for candidate in candidates:
        formatted_candidate = f"""
        <pre>
        Имя кандидата - {candidate.name}
        Позиция кандидата - {candidate.postition}
        Нвыки - {candidate.skills}
        </pre>
        """
        formatted_candidates.append(formatted_candidate)

    return "\n".join(formatted_candidates)


@app.route("/candidates/<int:x>")
def candidate_by_pk(x):
    get_candidate = get_by_pk(x)
    url = "https://ioe.hse.ru/data/2016/03/16/1138806118/img.jpg"
    formatted_candidate = f"""
        <img src= {url}>

        <pre>
        Имя кандидата - {get_candidate.name}
        Позиция кандидата - {get_candidate.postition}
        Нвыки - {get_candidate.skills}
        </pre>
        """
    return formatted_candidate

@app.route("/skills/<x>")
def candidate_by_skill(x):
    get_candidate = get_by_skill(x)
    formatted_candidates = []
    for candidate in get_candidate:
        formatted_candidate = f"""
            <pre>
            Имя кандидата - {candidate.name}
            Позиция кандидата - {candidate.postition}
            Нвыки - {candidate.skills}
            </pre>
            """
        formatted_candidates.append(formatted_candidate)
    return "\n".join(formatted_candidates)


if __name__ == "__main__":
    app.run()