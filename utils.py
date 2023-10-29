import json


class candidate:
    def __init__(self, name, position, skills):
        self.name = name
        self.postition = position
        self.skills = skills


def load_candidates():
    # Открыть файл в режиме чтения
    with open('candidates.json', 'r') as json_file:
        # Загрузить данные из JSON файла
        data = json.load(json_file)
    # Теперь переменная "data" содержит данные из JSON файла
    return data


def get_all():
    all_candidates = []
    candidates = load_candidates()
    for candidate_data in candidates:
        candidate_class = candidate(candidate_data["pk"], candidate_data["position"], candidate_data["skills"])
        all_candidates.append(candidate_class)
    return all_candidates


def get_by_pk(pk):
    candidates = load_candidates()
    for candidate_data in candidates:
        if candidate_data["pk"] == pk:
            candidate_class = candidate(candidate_data["pk"], candidate_data["position"], candidate_data["skills"])
    return candidate_class


def get_by_skill(skill_name):
    candidates = load_candidates()
    candidates_by_skill = []
    for candidate_data in candidates:
        if skill_name in candidate_data["skills"] or skill_name.title() in candidate_data["skills"]:
            candidate_class = candidate(candidate_data["pk"], candidate_data["position"], candidate_data["skills"])
            candidates_by_skill.append(candidate_class)
    return candidates_by_skill
