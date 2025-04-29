<<<<<<< HEAD
dados = {
    "turmas": [
        {
            "id" : 1,
            "descricao": "Turma 3A",
            "professor_id" : 1,
            "ativo" : True
        },

        {
            "id" : 2,
            "descricao": "Turma 3B",
            "professor_id" : 2,
            "ativo" : True
        }
    ],
}
=======
from config import db
from professor.professor_model import Professor

class Turma(db.Model):
    __tablename__ = "turmas"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable = False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable = False) 
    ativo = db.Column(db.Boolean, nullable = False)

    professor = db.relationship('Professor', back_populates='turmas')
    alunos = db.relationship('Aluno', back_populates='turma')

    def __init__(
        self, 
        descricao,  
        professor_id,
        ativo
        ):

        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo
    
    def to_dict(self):
        return {
            "id" : self.id,
            "descricao" : self.descricao,
            "professor_id" : self.professor_id,
            "ativo" : self.ativo
        }
>>>>>>> b539fc8f01d5657d876f10005467c94b4c3f46c3

class TurmaNaoEncontrada(Exception):
    pass

def listar_turmas():
<<<<<<< HEAD
    return dados["turmas"]

def turma_por_id(id):
    turmas = dados["turmas"]
    for turma in turmas:
        if turma["id"] == id:
            return turma
    raise TurmaNaoEncontrada()
        
def adicionar_turma(turma):
    dados["turmas"].append(turma)

def atualizar_turma(id, novos_dados):
    turma = turma_por_id(id)
    turma.update(novos_dados)
                
def excluir_turma(id):
    turma = turma_por_id(id)
    dados["turmas"].remove(turma)
=======
    turmas = Turma.query.all()
    print(turmas)
    return [turma.to_dict() for turma in turmas]


def turma_por_id(id):
    turma = Turma.query.get(id)

    if not turma:
        raise TurmaNaoEncontrada(f"Turma não encontrada.")
    return turma.to_dict()
        

def adicionar_turma(novos_dados):
    nova_turma = Turma(
        descricao = novos_dados['descricao'],
        professor_id = int(novos_dados['professor_id']),
        ativo = novos_dados['ativo']
    )

    db.session.add(nova_turma)
    db.session.commit()
    return {"message" : "Turma adicionada com sucesso!"}, 201


def atualizar_turma(id, novos_dados):
    turma = Turma.query.get(id)
    if not turma:
        raise TurmaNaoEncontrada(f"Turma não encontrada.")
    
    turma.descricao = novos_dados['descricao']
    turma.professor_id = novos_dados['professor_id']
    turma.ativo = novos_dados['ativo']
    
    db.session.commit()
    return {"message": "Turma atualizada com sucesso!"}, 200
                

def excluir_turma(id):
    turma = Turma.query.get(id)
    if not turma:
        raise TurmaNaoEncontrada(f"Turma não encontrada.")

    db.session.delete(turma)
    db.session.commit()
    return {"message": "Turma excluída com sucesso!"}, 200
>>>>>>> b539fc8f01d5657d876f10005467c94b4c3f46c3
