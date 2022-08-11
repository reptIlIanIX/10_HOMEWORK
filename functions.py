import requests


def load_candidates():
    response = requests.get('https://jsonkeeper.com/b/CPZN')
    profile = response.json()
    return profile


def get_all():
    for item in load_candidates():
        print(item['name'])


def get_by_pk(pk):
    for item in load_candidates():
        if pk == item['pk']:
            return f'<img src="{item["picture"]}"\n\n' \
                   f'<pre>\nИмя кандидата {item["name"]}\nПозиция кандидата {item["position"]}\nНавыки через запятую {item["skills"]}</pre>'


def get_by_skill(skill_name):
    for item in load_candidates():
        if skill_name in item['skills']:
            return f'<pre>\nИмя кандидата {item["name"]}\nПозиция кандидата {item["position"]}\nНавыки через запятую {item["skills"]}</pre>'



