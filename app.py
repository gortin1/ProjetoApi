import os
from config import app
from aluno.aluno_route import alunos_blueprint
from professor.professor_route import professores_blueprint
from turma.turma_route import turmas_blueprint


              
app.register_blueprint(alunos_blueprint)
app.register_blueprint(professores_blueprint)
app.register_blueprint(turmas_blueprint)

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])