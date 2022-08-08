# Создаем клас Candidate с иноформацией о кандидате
class Candidate:
    def __init__(self, pk, name, picture, position, skills):
        self.pk = pk
        self.name = name
        self.picture = picture
        self.position = position
        self.skills = skills

    def __repr__(self):
        return f'{self.name} \n {self.position} \n {self.skills}'
