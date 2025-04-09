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