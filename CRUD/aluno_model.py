from datetime import date

dados = {
    "alunos": [
        {
            "id": 1, 
            "nome": "Camila", 
            "idade": 20, 
            "turma_id": 1, 
            "data_nascimento": date(2025,3,14),
            "nota_primeiro_semestre": 10.0,
            "nota_segundo_semestre": 9.0,
            "media_final": 9.5
        },

        {
            "id": 2, 
            "nome": "Fernando", 
            "idade": 24, 
            "turma_id": 2, 
            "data_nascimento": date(2025,3,14),
            "nota_primeiro_semestre": 10.0,
            "nota_segundo_semestre": 8.0,
            "media_final": 9.0
        }
    ]
}

class AlunoNaoEncontrado(Exception):
    pass
     
def listar_alunos():
    return dados["alunos"]

def aluno_por_id(id):
    alunos = dados["alunos"]
    for aluno in alunos:
        if aluno["id"] == id:
            return aluno
    raise AlunoNaoEncontrado()
        
def adicionar_aluno(aluno):
    dados["alunos"].append(aluno)

def atualizar_aluno(id, novos_dados):
    aluno = aluno_por_id(id)
    aluno.update(novos_dados)
                
def excluir_aluno(id):
    aluno = aluno_por_id(id)
    dados["alunos"].remove(aluno)