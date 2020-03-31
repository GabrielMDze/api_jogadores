import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.console.models import Console
from my_app import api, db

console = Blueprint('console',__name__)

parser = reqparse.RequestParser()
parser.add_argument('nome',type=str)
parser.add_argument('nick',type=str)
parser.add_argument('time',type=str)
parser.add_argument('role',type=str)
parser.add_argument('abatimentos',type=int)
parser.add_argument('assistencias',type=int)
parser.add_argument('mortes',type=int)
parser.add_argument('partidas',type=int)
parser.add_argument('vitorias',type=int)
parser.add_argument('kda',type=float)
parser.add_argument('vd',type=float)


@console.route("/")
@console.route("/home")
def home():
    return "Jogadores"

class ConsoleAPI(Resource):
    def get(self,id=None,page=1):
        if not id:
            consoles = Console.query.paginate(page,10).items
        else:
            consoles = [Console.query.get(id)]
        if not consoles:
            abort(404)
        res = {}
        for con in consoles:
            res[con.id] = {
                'Nome do Jogador' : con.nome,
                'Nickname' : con.nick,
                'Time' : con.time,
                'posição' : con.role,
                'Abatimentos' : str(con.abatimentos),
                'Assistencias' : str(con.assistencias),
                'Mortes' : str(con.mortes),
                'Partidas' : str(con.partidas),
                'Vitorias' : str(con.vitorias),
                'KDA' : str(con.kda),
                'TaxaVitoria' : str(con.vd)
            }
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        nome = args['nome']
        nick = args['nick']
        time = args['time']
        role = args['role']
        abatimentos = args['abatimentos']
        assistencias = args['assistencias']
        mortes = args['mortes']
        partidas = args['partidas']
        vitorias = args['vitorias']
        con = Console(nome,nick,time,role,abatimentos, assistencias, mortes, partidas, vitorias)
        db.session.add(con)
        db.session.commit()
        res = {}
        res[con.id] = {
                'Nome do Jogador' : con.nome,
                'Nickname' : con.nick,
                'Time' : con.time,
                'posição' : con.role,
                'Abatimentos' : str(con.abatimentos),
                'Assistencias' : str(con.assistencias),
                'Mortes' : str(con.mortes),
                'Partidas' : str(con.partidas),
                'Vitorias' : str(con.vitorias),
                'KDA' : str(con.kda),
                'TaxaVitoria' : str(con.vd)
        }
        return json.dumps(res)

    def delete(self, id):
        con = Console.query.get(id)
        db.session.delete(con)
        db.session.commit()
        res = {'id':id}
        return json.dumps(res)

    def put(self,id):
        con = Console.query.get(id)
        args = parser.parse_args()
        nome = args['nome']
        nick = args['nick']
        time = args['time']
        role = args['role']
        abatimentos = args['abatimentos']
        assistencias = args['assistencias']
        mortes = args['mortes']
        partidas = args['partidas']
        vitorias = args['vitorias']
        con.nome = nome
        con.nick = nick
        con.time = time
        con.role = role
        con.abatimentos = abatimentos
        con.assistencias = assistencias
        con.mortes = mortes
        con.partidas = partidas
        con.vitorias = vitorias
        con.kda = (abatimentos+assistencias)/mortes
        con.vd = vitorias/partidas*100
        db.session.commit()
        res = {}
        res[con.id] = {
                'Nome do Jogador' : con.nome,
                'Nickname' : con.nick,
                'Time' : con.time,
                'posição' : con.role,
                'Abatimentos' : str(con.abatimentos),
                'Assistencias' : str(con.assistencias),
                'Mortes' : str(con.mortes),
                'Partidas' : str(con.partidas),
                'Vitorias' : str(con.vitorias),
                'KDA' : str(con.kda),
                'TaxaVitoria' : str(con.vd)
        }
        return json.dumps(res)

api.add_resource(
    ConsoleAPI,
    '/api/console',
    '/api/console/<int:id>',
    '/api/console/<int:id>/<int:page>'
)