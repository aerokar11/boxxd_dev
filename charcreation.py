import datetime
playerLocation = DE
YYYY = 2025
MM = 4
DD = 5

class charakter:
    def __init__(self, bwid, name, surname, nickname, gender, bday, yyyy, mm, dd, sexuality, personality):
        self.bwid = int(bwid)
        self.name = str(name)
        self.surname = str(surname)
        self.nickname = str(nickname)
        self.gender = str(gender)
        self.bday = datetime.date(yyyy, mm, dd)
        self.sexuality = str(sexuality)
        self.personality = str(personality)

    def checkAdult(bday, playerLocation):
        # get location
        # get age of adulthood in that country
        currentAge = datetime.date.
        if playerLocation = DE and age = 18