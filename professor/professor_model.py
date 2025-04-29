<<<<<<< HEAD
dados = {
    "professores": [
        {
            "id": 1, 
            "nome": "Gabriel", 
            "idade": 20, 
            "materia": "Portugues", 
            "observacoes": "Aula de Segunda"
        },

        {
            "id": 2, 
            "nome": "Nicolas", 
            "idade": 22, 
            "materia": "Portugues", 
            "observacoes": "Aula de Terça"
        }
    ],
}
     
class ProfessorNaoEncontrado(Exception):
    pass
     
def listar_professores():
    return dados["professores"]

def professor_por_id(id):
    professores = dados["professores"]
    for professor in professores:
        if professor["id"] == id:
            return professor
    raise ProfessorNaoEncontrado()
        
def adicionar_professor(professor):
    dados["professores"].append(professor)

def atualizar_professor(id, novos_dados):
    professor = professor_por_id(id)
    professor.update(novos_dados)
                
def excluir_professor(id):
    professor = professor_por_id(id)
    dados["professores"].remove(professor)
=======
from config import db

class Professor(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable = False)
    idade = db.Column(db.Integer, nullable = False)
    materia = db.Column(db.String(100), nullable = False)
    observacoes = db.Column(db.Text, nullable = False)

    turmas = db.relationship('Turma', back_populates='professor')

    def __init__(
        self, 
        nome,  
        idade,
        materia,
        observacoes
        ):

        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

    def to_dict(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "idade" : self.idade,
            "materia" : self.materia,
            "observacoes" : self.observacoes
        }

class ProfessorNaoEncontrado(Exception):
    pass
     

def listar_professores():
    professores = Professor.query.all()
    print(professores)
    return [professor.to_dict() for professor in professores]


def professor_por_id(id):
    professor = Professor.query.get(id)

    if not professor:
        raise ProfessorNaoEncontrado(f"Professor não encontrado.")
    return professor.to_dict()


def adicionar_professor(novos_dados):
    novo_professor = Professor(
        nome = novos_dados['nome'],
        idade = int(novos_dados['idade']),
        materia = novos_dados['materia'],
        observacoes = novos_dados['observacoes']
    )

    db.session.add(novo_professor)
    db.session.commit()
    return {"message" : "Professor adicionado com sucesso!"}, 201


def atualizar_professor(id, novos_dados):
    professor = Professor.query.get(id)
    if not professor:
        raise ProfessorNaoEncontrado(f"Professor não encontrado.")
    
    professor.nome = novos_dados['nome']
    professor.idade = novos_dados['idade']
    professor.materia = novos_dados['materia']
    professor.observacoes = novos_dados['observacoes']
    
    db.session.commit()
    return {"message": "Professor atualizado com sucesso!"}, 200

               
def excluir_professor(id):
    professor = Professor.query.get(id)
    if not professor:
        raise ProfessorNaoEncontrado(f"Professor não encontrado.")

    db.session.delete(professor)
    db.session.commit()
    return {"message": "Professor excluído com sucesso!"}, 200
>>>>>>> b539fc8f01d5657d876f10005467c94b4c3f46c3
