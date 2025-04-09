from flask import Flask, jsonify, request
import aluno_model
import professor_model
import turma_model

app = Flask(__name__)

@app.route('/aluno', methods = ['GET'])
def alunos():
    print("Lista de todos os alunos")
    return aluno_model.listar_alunos()


@app.route('/aluno/<int:id>', methods = ['GET'])
def alunos_por_id(id):
    try:
        return aluno_model.aluno_por_id(id)
    except aluno_model.AlunoNaoEncontrado:
        return ({'Erro':'Aluno não encontrado'}, 400)
        

@app.route('/aluno', methods = ['POST'])
def criar_aluno():
    dados = request.json
    dados['id'] = int (dados['id'])
    aluno_model.adicionar_aluno(dados)
    return aluno_model.listar_alunos() 


@app.route('/aluno/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    try:
        dados = request.json
        aluno_model.atualizar_aluno(id, dados)
        return jsonify({'mensagem': 'Aluno atualizado com sucesso'}), 200
    except aluno_model.AlunoNaoEncontrado:
        return ({'Erro':'Aluno não encontrado'}, 400)
        

@app.route('/aluno/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    try:
        aluno_model.excluir_aluno(id)
        return {'mensagem': 'Aluno deletado.'}, 200 
    except aluno_model.AlunoNaoEncontrado:
        return ({'Erro':'Aluno não encontrado'}, 400)


@app.route('/professor', methods = ['GET'])
def professores():
    print("Lista de todos os professores")
    return professor_model.listar_professores()


@app.route('/professor/<int:id>', methods = ['GET'])
def professor_por_id(id):
    try:
        return professor_model.professor_por_id(id)
    except professor_model.ProfessorNaoEncontrado:
        return ({'Erro':'Professor não encontrado'}, 400)
        

@app.route('/professor', methods = ['POST'])
def criar_professor():
    dados = request.json
    dados['id'] = int (dados['id'])
    professor_model.adicionar_professor(dados)
    return professor_model.listar_professores()


@app.route('/professor/<int:id>', methods = ['PUT'])
def atualizar_professor(id):
    try:
        dados = request.json
        professor_model.atualizar_professor(id, dados)
        return jsonify({'mensagem': 'Professor atualizado com sucesso'}), 200
    except professor_model.ProfessorNaoEncontrado:
        return ({'Erro':'Professor não encontrado'}, 400)


@app.route('/professor/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    try:
        professor_model.excluir_professor(id)
        return {'mensagem': 'Professor deletado.'}, 200
    except professor_model.ProfessorNaoEncontrado:
        return ({'Erro':'Professor não encontrado'}, 400)
    

   
@app.route('/turma', methods=['GET'])
def turmas():
    print("Lista de todos as turmas")
    return turma_model.listar_turmas()


@app.route('/turma/<int:id>', methods=['GET'])
def turma_por_id(id):
    try:
        return turma_model.turma_por_id(id)
    except turma_model.TurmaNaoEncontrada:
        return ({'Erro':'Turma não encontrada'}, 400)
        

@app.route('/turma', methods=['POST'] )
def criar_turma():
    dados = request.json
    dados['id'] = int (dados['id'])
    turma_model.adicionar_turma(dados)
    return turma_model.listar_turmas() 


@app.route('/turma/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    try:
        dados = request.json
        turma_model.atualizar_turma(id, dados)
        return jsonify({'mensagem': 'Turma atualizada com sucesso'}), 200
    except turma_model.TurmaNaoEncontrada:
        return ({'Erro':'Turma não encontrada'}, 400)
        
           
@app.route('/turma/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    try:
        turma_model.excluir_turma(id)
        return {'mensagem': 'Turma deletada.'}, 200
    except turma_model.TurmaNaoEncontrada:
        return ({'Erro':'Turma não encontrada'}, 400)
               

if __name__ == '__main__':
    app.run(debug=True)