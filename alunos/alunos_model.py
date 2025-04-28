from datetime import date
from config import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    turma_id = db.Column(db.Integer)
    data_nascimento = db.Column(db.Integer)
    nota1 = db.Column(db.Float)
    nota2 = db.Column(db.Float)
    media_final = db.Column(db.Float)

    def __init__(self, nome, idade, turma_id, data_nascimento, nota1, nota2, media_final):
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota1 = nota1
        self.nota2 = nota2
        self.media_final = media_final

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma_id': self.turma_id,
            'data_nascimento': self.data_nascimento,
            'nota1': self.nota1,
            'nota2': self.nota2,
            'media_final': self.media_final
        }

class AlunoNaoEncontrado(Exception):
    pass
     
def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def aluno_por_id(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        raise AlunoNaoEncontrado
    print(aluno.to_dict())
    return aluno.to_dict()
        
def adicionar_aluno(aluno):
    novo_aluno = Aluno(**aluno)
    db.session.add(novo_aluno)
    db.session.commit()
        
def atualizar_aluno(id, novos_dados):
    aluno = Aluno.query.get(id)
    if not aluno:
        raise AlunoNaoEncontrado
    for chave in novos_dados.keys():
        aluno[chave] = novos_dados[chave]
    db.session.commit()
                
def excluir_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()
    
def excluir_tudo():
    aluno = Aluno.query.all()
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    