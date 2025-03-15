from datetime import date
from flask import Flask, jsonify, request

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
    ],

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

@app.route('/aluno', methods = ['GET'])
def getAlunos():
    dados = dicionario["alunos"]
    return jsonify(dados)

@app.route('/aluno/<int:id>', methods = ['GET'])
def getAluno(id):
    alunos = dicionario["alunos"]
    for aluno in alunos:
        if aluno['id'] == id:
            return jsonify(aluno)
        
@app.route('/aluno', methods = ['POST'])
def createAluno():
    try:
        dados = request.json
        if not dados:
            return jsonify({'erro':'ocorreu um erro dados invalidos ou ausentes'}) ,400
        aluno = dicionario["alunos"]
        aluno.append(dados) 
        return jsonify(dados)
    except Exception as e:
        return jsonify({'erro':f'Ocorreu um erro {e}'}), 500

@app.route('/aluno/<int:id>', methods=['PUT'])
def updateAluno(id):
    alunos = dicionario["alunos"]
    for aluno in alunos:
        if aluno['id'] == id:
            dados = request.json
            aluno['nome'] = dados['nome']
            aluno['idade'] = dados['idade']
            aluno['turma_id'] = dados['turma_id']
            aluno['data_nascimento'] = dados['data_nascimento']
            aluno['nota_primeiro_semestre'] = dados['nota_primeiro_semestre']
            aluno['nota_segundo_semestre'] = dados['nota_segundo_semestre']
            aluno['media_final'] = dados['media_final']
            return jsonify(dados)
        
@app.route('/aluno/<int:id>', methods=['DELETE'])
def deleteAluno(id):
    alunos = dicionario["alunos"]
    for aluno in alunos:
        if aluno['id'] == id:
            index = alunos.index(aluno)
            alunos.pop(index)
            return jsonify(aluno)
     
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
        
        
@app.route('/professor/<int:id>', methods=['DELETE'])
def deleteProfessor(id):
    professores = dicionario["professores"]
    for professor in professores:
        if professor['id'] == id:
            index = professores.index(professor)
            professores.pop(index)
            return jsonify(professor)
        
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