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

class TurmaNaoEncontrada(Exception):
    pass

def listar_turmas():
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