# Импортируем json и класс candidate
import json
from candidate import Candidate


def load_candidates(filename):
    """Функция, которая загрузит данные из файла"""
    with open(filename, "r", encoding="utf8") as json_file:
        data = json.load(json_file)
    return data


def get_all(data):
    """Функция, которая покажет всех кандидатов"""
    arr = []
    for i in data:
        candidate = Candidate(i['pk'], i['name'], i['picture'], i['position'], i['skills'].lower())
        arr.append(candidate)
    return arr


def get_by_pk(pk, data):
    """Функция, которая вернет кандидата по pk"""
    for candidate in data:
        if pk == candidate.pk:
            return candidate


def get_by_skill(skill_name, data):
    """Функция, которая вернет кандидатов по навыку"""
    skill_list = []
    for skill in data:
        if skill_name in skill.skills:
            skill_list.append(skill)
    return skill_list
