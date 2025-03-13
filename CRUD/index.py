from flask import Flask, jsonify, request

app = Flask("__name__")

dicionario = {
    "alunos": [{"id":1,"nome":"teste"}],
    "professores":[{}],
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

if __name__ == '__main__':
    app.run(debug=True)