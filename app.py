from datetime import date
from flask import Flask, jsonify, request
from alunos.alunos_route import alunos_blueprint

app = Flask("__name__")

dicionario = {
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
    ]
}

app.register_blueprint(alunos_blueprint)

@app.route('/professor', methods = ['GET'])
def getProfessores():
    dados = dicionario["professores"]
    return jsonify(dados)

@app.route('/professor/<int:id>', methods = ['GET'])
def getProfessor(id):
    professores = dicionario["professores"]
    for professor in professores:
        if professor['id'] == id:
            return jsonify(professor)
    return jsonify({'Erro': f'Ocorreu um erro: Professor não encontrado'})
        
@app.route('/professor', methods = ['POST'])
def createProfessor():
    try:
        dados = request.json
        if not dados:
            return jsonify({'erro':'dados invalidos ou ausentes'}), 400
        professores = dicionario["professores"]
        professores.append(dados)
        return jsonify(dados)
    except Exception as e:
        return jsonify({'erro': f'ocorreu um erro: {str(e)}'}), 500
        
@app.route('/professor/<int:id>', methods = ['PUT'])
def updateProfessor(id):
    professores = dicionario["professores"]
    for professor in professores:
        if professor['id'] == id:
            dados = request.json
            professor['nome'] = dados['nome']
            professor['idade'] = dados['idade']
            professor['materia'] = dados['materia']
            professor['observacoes'] = dados['observacoes']
            return jsonify(dados)
        
    return jsonify({'Erro': f'Ocorreu um erro: Professor não encontrado'})
        
@app.route('/professor/<int:id>', methods = ['PATCH'])
def PatchUpdateProfessor(id):
    professores = dicionario['professores']
    dados = request.json
    for professor in professores:
        if professor['id'] == id:
            for chave in dados.keys():
                professor[chave] = dados[chave]
            
            if dados.keys():
                return jsonify(professor)
        
    if not dados.keys():    
        return jsonify({'Erro': f'Ocorreu um erro: Nenhum parametro foi alterado'})
    
    return jsonify({'Erro': f'Ocorreu um erro: Professor não encontrado'})
        
@app.route('/professor/<int:id>', methods=['DELETE'])
def deleteProfessor(id):
    professores = dicionario["professores"]
    for professor in professores:
        if professor['id'] == id:
            index = professores.index(professor)
            professores.pop(index)
            return jsonify(professor)
    return jsonify({'Erro': f'Ocorreu um erro: Professor não encontrado'})
        
@app.route('/turma', methods=['GET'])
def getTurmas():
    dados = dicionario["turmas"]
    return jsonify(dados)

@app.route('/turma/<int:id>', methods=['GET'])
def getTurma(id):
    turmas = dicionario["turmas"]
    for turma in turmas:
        if turma['id'] == id:
            return jsonify(turma)
        
@app.route('/turma', methods=['POST'] )
def createTurma():
    try: 
        dados = request.json
        if not dados:
            return jsonify({'erro':'dados invalidos ou ausentes'}), 400
        
        turma = dicionario["turmas"]
        turma.append(dados)
        return jsonify(dados)
    except Exception as e:
        return jsonify({'erro': f'ocorreu um erro: {str(e)}'}), 500

@app.route('/turma/<int:id>', methods=['PUT'])
def updateTurma(id):
    turmas = dicionario['turmas']
    for turma in turmas:
        if turma['id'] == id:
            dados = request.json
            turma['descricao'] = dados['descricao']
            turma['professor_id'] = dados['professor_id']
            turma['ativo'] = dados['ativo']
            return jsonify(dados)
        
@app.route('/turma/<int:id>', methods=['PATCH'])
def PatchUpdateTurma(id):
    turmas = dicionario['turmas']
    dados = request.json
    for turma in turmas:
        if turma['id'] == id:
            for chave in dados.keys():
                turma[chave] = dados[chave]
                
            if dados.keys():
                return jsonify(turma)
            
    if not dados.keys():    
        return jsonify({'Erro': f'Ocorreu um erro: Nenhum parametro foi alterado'})
    
    return jsonify({'Erro': f'Ocorreu um erro: Professor não encontrado'})
                
                
@app.route('/turma/<int:id>', methods=['DELETE'])
def deleteTurma(id):
    turmas = dicionario['turmas']
    for turma in turmas:
        if turma['id'] == id:
            index = turmas.index(turma)
            turmas.pop(index)
            return jsonify(turma)
               
if __name__ == '__main__':
    app.run(debug=True)