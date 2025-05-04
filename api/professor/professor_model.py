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