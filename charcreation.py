import datetime
class charakter:
    def __init__(self, bwid, vorname, nachname, nickname, gender, geb, sexuality, personality):
        self.bwid = int(bwid)
        self.vorname = str(vorname)
        self.nachname = str(nachname)
        self.nickname = str(nickname)
        self.gender = str(gender)
        self.geb = datetime.datetime(YYYY, MM, DD)
        self.sexuality = str(sexuality)
        self.personality = str(personality)
