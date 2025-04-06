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

class alunoNaoEncontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    lista_alunos = dados['alunos']
    for dicionario in lista_alunos:
        if dicionario['id'] == id_aluno:
            return dicionario
    raise alunoNaoEncontrado

def listar_aluno():
    return dados["alunos"]

def adicionar_aluno(aluno):
    dados["alunos"].append(aluno)

def atualizar_aluno(id_aluno,novo_dado):
    aluno = aluno_por_id(id_aluno)
    aluno.update(novo_dado)

def excluir_aluno(id_aluno):
    aluno = aluno_por_id(id_aluno)
    dados['alunos'].remove(aluno)

