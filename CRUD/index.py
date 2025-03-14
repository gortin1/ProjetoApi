from flask import Flask, jsonify, request

app = Flask("__name__")

dicionario = {
    "alunos": [{"id":1,"nome":"teste"}],
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
        if aluno['id'] == id:
            return jsonify(aluno)
        else:
            return jsonify("Aluno não encontrado!")
        

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
        else:
            return jsonify("Aluno não encontrado!")
        
@app.route('/alunos/<int:id>', methods=['DELETE'])
def deleteAluno(id):
    alunos = dicionario["alunos"]
    for aluno in alunos:
        if aluno['id'] == id:
            index = alunos.index(aluno)
            alunos.pop(index)
            return jsonify(aluno)
        else:
            return jsonify("Aluno não encontrado!")
     
@app.route('/professor')
def getProfessores():
    dados = dicionario["professores"]
    return jsonify(dados)

@app.route('/professor/<int:id>')
def getProfessor(id):
    professor = dicionario["professores"]
    for professores in professor:
        if professores['id'] == id:
            return jsonify(professor)
        else:
            return jsonify("Professor não encontrado!!")
        
@app.route('/postProfessor')
def createProfessor():
    dados = request.json
    professor = dicionario["professores"]
    professor.append(dados)
    return jsonify(dados)

@app.route('/professor/<int:id>', methods = ['PUT'])
def updateProfessor(id):
    professor = dicionario["professores"]
    for professores in professor:
        if professores['id'] == id:
            dados = request.json
            professores['nome','idade','materia','observações']= dados['nome','idade','materia','observações']
            return jsonify(dados)
        else:
            return jsonify("Professor não encontrado!!")
        
@app.route('/professor/<int:id>', methods=['DELETE'])
def deleteProfessor(id):
    professores = dicionario["professores"]
    for professor in professores:
        if professor['id'] == id:
            index = professores.index(professor)
            professores.pop(index)
            return jsonify(professor)
        else:
            return jsonify("Professor não encontrado")
               
if __name__ == '__main__':
    app.run(debug=True)