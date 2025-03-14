from flask import Flask, jsonify, request

app = Flask("__name__")

dicionario = {
    "alunos": [{"id":1,"nome":"teste"},
               {"id":2,"nome":"teste2"}],
    "professores":[{"id":1,"nome":"carlos","idade":20,"materia":"portugues","observações":"Muita coisa pra adicionar"}],
    "turmas":[{}]
}

@app.get('/alunos')
def getAlunos():
    dados = dicionario["alunos"]
    return jsonify(dados)

@app.get('/alunos/<int:id>')
def getIdAluno(id):
    alunos = dicionario["alunos"]
    for aluno in alunos:
        print(aluno)
        print(alunos)
        if aluno['id'] == id:
            return jsonify(alunos)
        

@app.post('/postalunos')
def createAluno():
    dados = request.json
    aluno = dicionario["alunos"]
    aluno.append(dados) 
    return jsonify(dados)

@app.route('/alunos/<int:id>', methods=['PUT'])
def updateAluno(id):
    alunos = dicionario["alunos"]
    for aluno in alunos:
        if aluno['id'] == id:
            dados = request.json
            aluno['nome'] = dados['nome']
            return jsonify(dados)
        
@app.route('/alunos/<int:id>', methods=['DELETE'])
def deleteAluno(id):
    alunos = dicionario["alunos"]
    for aluno in alunos:
        if aluno['id'] == id:
            index = alunos.index(aluno)
            alunos.pop(index)
            return jsonify(aluno)
     
@app.get('/professor')
def getProfessores():
    dados = dicionario["professores"]
    return jsonify(dados)

@app.get('/professor/<int:id>')
def getProfessor(id):
    professores = dicionario["professores"]
    for professor in professores:
        if professor['id'] == id:
            return jsonify(professor)
        
@app.post('/postprofessor')
def createProfessor():
    dados = request.json
    professor = dicionario["professores"]
    professor.append(dados)
    return jsonify(dados)

@app.route('/professor/<int:id>', methods = ['PUT'])
def updateProfessor(id):
    professores = dicionario["professores"]
    for professor in professores:
        if professor['id'] == id:
            dados = request.json
            professor['nome']= dados['nome']
            professor['idade'] = dados['idade']
            professor['materia'] = dados['materia']
            professor['observações'] = dados['observações']
            return jsonify(dados)
        
@app.route('/professor/<int:id>', methods=['DELETE'])
def deleteProfessor(id):
    professores = dicionario["professores"]
    for professor in professores:
        if professor['id'] == id:
            index = professores.index(professor)
            professores.pop(index)
            return jsonify(professor)
               
if __name__ == '__main__':
    app.run(debug=True)