from my_app import db

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    nick = db.Column(db.String(100))
    time = db.Column(db.String(100))
    role = db.Column(db.String(100))
    abatimentos = db.Column(db.String(100))
    assistencias = db.Column(db.Float(asdecimal=True))
    mortes = db.Column(db.Float(asdecimal=True))
    partidas = db.Column(db.Float(asdecimal=True))
    vitorias = db.Column(db.Float(asdecimal=True))
    kda = db.Column(db.Float(asdecimal=True))
    vd = db.Column(db.Float(asdecimal=True))


    def __init__(self,nome,nick,time,role,abatimentos, assistencias, mortes, partidas, vitorias):
        self.nome = nome
        self.nick = nick
        self.time = time
        self.role = role
        self.abatimentos = abatimentos
        self.assistencias = assistencias
        self.mortes = mortes
        self.partidas = partidas
        self.vitorias = vitorias
        if mortes == 0:
            self.kda = abatimentos+assistencias
        else:
            self.kda = (abatimentos+assistencias)/mortes
        self.vd = (vitorias/partidas)*100

    def __repr__(self):
        return 'Serie {0}'.format(self.id)