# Импортируем flask
from flask import Flask

# Импортируем функции из файла utility
from utility import get_all, load_candidates, get_by_pk, get_by_skill

FILENAME = "candidates.json"
app = Flask(__name__)
data = get_all(load_candidates(FILENAME))


# Создаем представление для route главная страница.
@app.route('/')
def index():
    str_ = '<pre>''\n'
    for i in data:
        str_ += f"{i} \n \n"
    str_ += '</pre>'
    return str_


# Создайте представление для route кандидаты.
@app.route('/candidates/<int:pk>')
def get_candidate(pk):
    user = get_by_pk(pk, data)
    if user:
        str_ = f'<img src="{user.picture}">'
        str_ += f'<pre> \n {user} \n </pre>'
    else:
        str_ = "NOT FOUND"
    return str_


# Создайте представление для поиска навыков.
@app.route('/skills/<x>')
def get_skills(x):
    x = x.lower()
    users = get_by_skill(x, data)
    if users:
        str_ = '<pre>'
        for i in users:
            str_ += f'{i} \n \n'
        str_ += '</pre>'
    else:
        str_ = "NOT FOUND"
    return str_


if __name__ == '__main__':
    app.run(port=5000)
