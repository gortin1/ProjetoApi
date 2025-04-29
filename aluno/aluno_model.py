from datetime import date, datetime
from config import db
from turma.turma_model import Turma

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable = False)
    idade = db.Column(db.Integer, nullable = False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable = False) 
    data_nascimento = db.Column(db.Date, nullable = False)
    nota_primeiro_semestre = db.Column(db.Float, nullable = False) 
    nota_segundo_semestre = db.Column(db.Float, nullable = False)
    media_final = db.Column(db.Float, nullable = False)

    turma = db.relationship('Turma', back_populates='alunos')

    def __init__(
        self, 
        nome,  
        turma_id, 
        data_nascimento, 
        nota_primeiro_semestre, 
        nota_segundo_semestre
        ):

        self.nome = nome
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = self.calcularMediaFinal()
        self.idade = self.calcularIdade()
    
    def calcularMediaFinal(self):
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

    def calcularIdade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def to_dict(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "idade" : self.idade,
            "turma_id" : self.turma_id,
            "data_nascimento" : self.data_nascimento.isoformat(),
            "nota_primeiro_semestre" : self.nota_primeiro_semestre,
            "nota_segundo_semestre" : self.nota_segundo_semestre,
            "media_final" : self.media_final
        }

class AlunoNaoEncontrado(Exception):
    pass

def listar_alunos():
    alunos = Aluno.query.all()
    print(alunos)
    return [aluno.to_dict() for aluno in alunos]


def aluno_por_id(id):
    aluno = Aluno.query.get(id)

    if not aluno:
        raise AlunoNaoEncontrado(f"Aluno não encontrado.")
    return aluno.to_dict()
        

def adicionar_aluno(novos_dados):
    turma = Turma.query.get(novos_dados['turma_id'])
    if (turma is None):
        return {"message" : "Turma não existe"}, 404

    novo_aluno = Aluno(
        nome = novos_dados['nome'],
        data_nascimento = datetime.strptime(novos_dados['data_nascimento'], "%Y-%m-%d").date(),
        turma_id = int(novos_dados['turma_id']),
        nota_primeiro_semestre = float(novos_dados['nota_primeiro_semestre']),
        nota_segundo_semestre = float(novos_dados['nota_segundo_semestre']),
    )

    db.session.add(novo_aluno)
    db.session.commit()
    return {"message": "Aluno adicionado com sucesso!"}, 200

    
def atualizar_aluno(id, novos_dados):
    aluno = Aluno.query.get(id)
    if not aluno:
        raise AlunoNaoEncontrado(f"Aluno não encontrado.")

    try:
        data_nascimento = datetime.strptime(novos_dados['data_nascimento'], "%Y-%m-%d").date()
    except ValueError:
        return {"message": "Formato de data inválido. Use YYYY-MM-DD."}, 400
    
    aluno.nome = novos_dados['nome']
    aluno.turma_id = novos_dados['turma_id']
    aluno.data_nascimento = data_nascimento
    aluno.nota_primeiro_semestre = novos_dados['nota_primeiro_semestre']
    aluno.nota_segundo_semestre = novos_dados['nota_segundo_semestre']
    aluno.media_final = aluno.calcularMediaFinal()
    aluno.idade = aluno.calcularIdade()
    
    db.session.commit()
    return {"message": "Aluno atualizado com sucesso!"}, 200


def excluir_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        raise AlunoNaoEncontrado(f"Aluno não encontrado.")

    db.session.delete(aluno)
    db.session.commit()
    return {"message": "Aluno excluído com sucesso!"}, 200