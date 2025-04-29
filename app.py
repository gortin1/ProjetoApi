import os
from config import app, db
from aluno.aluno_route import alunos_blueprint
from professor.professor_route import professores_blueprint
from turma.turma_route import turmas_blueprint
<<<<<<< HEAD


=======
>>>>>>> b539fc8f01d5657d876f10005467c94b4c3f46c3
              
app.register_blueprint(alunos_blueprint)
app.register_blueprint(professores_blueprint)
app.register_blueprint(turmas_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])