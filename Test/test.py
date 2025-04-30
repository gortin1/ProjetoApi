import requests
import unittest


class TestStringMethods(unittest.TestCase):

    def test_001_adiciona_professor(self):
        requests.post('http://localhost:5000/professores', json= {
            'nome' : 'Gabriel', 
            'idade': 20, 
            'materia': 'Portugues', 
            'observacoes': 'Aula de Segunda'
        })

        requests.post('http://localhost:5000/professores', json= {
            'nome' : 'Marcella', 
            'idade': 18, 
            'materia': 'API', 
            'observacoes': 'Aula de Quarta'
        })
        
        professores =  requests.get('http://localhost:5000/professores')
        lista_retornada = professores.json()

        adicao1 = False
        adicao2 = False
        
        for professor in lista_retornada:
            if professor['nome'] == 'Gabriel':
                adicao1 = True
            if professor['nome'] == 'Marcella':
                adicao2 = True
            
        if not adicao1 or not adicao2: 
            self.fail('Professor não foi adicionado.')


    def test_002_lista_de_professores(self):
        professores = requests.get('http://localhost:5000/professores')
        
        if professores.status_code == 404:
            self.fail("O link está com erro | Não há professores no server")
            
        try:
            obj_retornado = professores.json()
        except:
            self.fail("Não foi retornado um json")
            
        self.assertIsInstance(obj_retornado, list)


    def test_003_professor_por_id(self):
        requests.post('http://localhost:5000/professores', json= {
            'nome' : 'Carol', 
            'idade': 35, 
            'materia': 'Historia', 
            'observacoes': 'Aula de Sexta'
        })

        professor_id = requests.get('http://localhost:5000/professores/3')
        dict_retornado = professor_id.json()
        self.assertEqual(type(dict_retornado), dict)
        self.assertIn('nome', dict_retornado)
        self.assertEqual(dict_retornado['nome'],'Carol')


    def test_004_edita_professor(self):
        requests.post('http://localhost:5000/professores', json= {
            'nome' : 'Nicolas', 
            'idade': 41, 
            'materia': 'Geografia', 
            'observacoes': 'Aula de Quinta'
        })

        professor_id_antes = requests.get('http://localhost:5000/professores/4')
        self.assertEqual(professor_id_antes.json()['nome'],'Nicolas')
        
        requests.put('http://localhost:5000/professores/4', json= {
            'nome' : 'Nicolas Lima', 
            'idade': 41, 
            'materia': 'DevOps', 
            'observacoes': 'Aula de Quinta'
        })
        
        professor_id_depois = requests.get('http://localhost:5000/professores/4')
        self.assertEqual(professor_id_depois.json()['nome'], 'Nicolas Lima')
        self.assertEqual(professor_id_depois.json()['id'], 4)

   
    def test_005_deleta_professor(self):
        requests.post('http://localhost:5000/professores', json= {
            'nome' : 'Carlos', 
            'idade': 26, 
            'materia': 'Filosofia', 
            'observacoes': 'Aula de Segunda'
        })

        requests.post('http://localhost:5000/professores', json= {
            'nome' : 'Caio', 
            'idade': 29, 
            'materia': 'Mobile', 
            'observacoes': 'Aula de Terça'
        })

        requests.post('http://localhost:5000/professores', json= {
            'nome' : 'Geovane', 
            'idade': 27, 
            'materia': 'Matematica', 
            'observacoes': 'Aula de Sexta'
        })
        
        requests.delete('http://localhost:5000/professores/5')

        professores = requests.get('http://localhost:5000/professores')
        lista_retornada = professores.json()
        
        self.assertNotIn('Carlos', [professor['nome'] for professor in lista_retornada])

        requests.delete('http://localhost:5000/professores/7')

        professores2 = requests.get('http://localhost:5000/professores')
        lista_retornada2 = professores2.json()

        self.assertNotIn('Geovane', [professor['nome'] for professor in lista_retornada2])
        
#----------------------------------------------------------------------------

    def test_006_adiciona_turma(self):
        requests.post("http://localhost:5000/turmas", json={
            'descricao' : 'Turma 1', 
            'professor_id' : 1,
            'ativo' : True
        })

        requests.post("http://localhost:5000/turmas", json={
            'descricao' : 'Turma 2', 
            'professor_id' : 1,
            'ativo' : True
        })

        requests.post("http://localhost:5000/turmas", json={
            'descricao' : 'Turma 3', 
            'professor_id' : 1,
            'ativo' : False
        })

        turmas = requests.get("http://localhost:5000/turmas")
        lista_retornada = turmas.json()

        Turma1 = False
        Turma2 = False
        Turma3 = False

        for turma in lista_retornada:
            if turma['descricao'] == "Turma 1":
                Turma1 = True
            if turma['descricao'] == "Turma 2":
                Turma2 = True
            if turma['descricao'] == "Turma 3":
                Turma3 = True

        if not Turma1 or not Turma2 or not Turma3:
            self.fail("Turma não foi adicionada.")


    def test_007_lista_de_turmas(self):
        turmas = requests.get("http://localhost:5000/turmas")
        
        if turmas.status_code == 404:
            self.fail("Link não está funcionando/Não ha turmas")
            
        try:
            obj_retornado = turmas.json()
        except:
            self.fail("Objeto não é um json")
            
        self.assertIsInstance(obj_retornado, list)
        
            
    def test_008_turma_por_id(self):
        requests.post("http://localhost:5000/turmas", json={
            'descricao' : 'Turma Id', 
            'professor_id' : 1,
            'ativo' : True
        })
        
        turma_id = requests.get('http://localhost:5000/turmas/4')
        dict_retornado = turma_id.json()
        self.assertEqual(type(dict_retornado), dict)
        self.assertIn('descricao', dict_retornado)
        self.assertEqual(dict_retornado['descricao'],'Turma Id')
        
    
              
    def test_009_edita_turma(self):
        requests.post("http://localhost:5000/turmas", json={
            'descricao' : 'Portugues', 
            'professor_id' : 2,
            'ativo' : True
        })
        
        turma_id_antes = requests.get('http://localhost:5000/turmas/5')
        self.assertEqual(turma_id_antes.json()['descricao'],'Portugues')
        
        requests.put("http://localhost:5000/turmas/5", json={
            'descricao' : 'Matematica', 
            'professor_id' : 2,
            'ativo' : True
        })

        turma_id_depois = requests.get('http://localhost:5000/turmas/5')
        self.assertEqual(turma_id_depois.json()['descricao'],'Matematica')
        self.assertEqual(turma_id_depois.json()['id'], 5)


    def test_010_deleta_turma(self):
        requests.post("http://localhost:5000/turmas", json={
            'descricao' : 'Analise e Desenvolvimento de Sistemas', 
            'professor_id' : 1,
            'ativo' : True
        })

        requests.post("http://localhost:5000/turmas", json={
            'descricao' : 'Ciencia da Computacao', 
            'professor_id' : 2,
            'ativo' : True
        })

        requests.post("http://localhost:5000/turmas", json={
            'descricao' : 'Sistemas de Informação', 
            'professor_id' : 1,
            'ativo' : False
        })

        requests.delete('http://localhost:5000/turmas/6')
        
        turmas = requests.get('http://localhost:5000/turmas')
        lista_retornada = turmas.json()
       
        self.assertNotIn('Analise e Desenvolvimento de Sistemas', [turma['descricao'] for turma in lista_retornada])
            
        requests.delete('http://localhost:5000/turmas/8')
        
        turmas2 = requests.get('http://localhost:5000/turmas')
        lista_retornada2 = turmas2.json()

        self.assertNotIn('Sistemas de Informação', [turma['descricao'] for turma in lista_retornada2])

#----------------------------------------------------------------------------

    def test_011_adiciona_aluno(self):
        requests.post('http://localhost:5000/alunos', json={
            'nome': 'Ronaldo', 
            'idade' : 20,
            'turma_id' : 2,
            'data_nascimento' : '2005-10-15',
            'nota_primeiro_semestre' : 8.0,
            'nota_segundo_semestre' : 9.0
        })

        requests.post('http://localhost:5000/alunos', json={
            'nome': 'Marcola', 
            'idade' : 25,
            'turma_id' : 1,
            'data_nascimento' : '2003-10-15',
            'nota_primeiro_semestre' : 7.0,
            'nota_segundo_semestre' : 5.0
        })
        
        alunos =  requests.get('http://localhost:5000/alunos')
        lista_alunos = alunos.json()
        adicao1 = False
        adicao2 = False
        
        for aluno in lista_alunos:
            if aluno['nome'] == 'Ronaldo':
                adicao1 = True
            if aluno['nome'] == 'Marcola':
                adicao2 = True
            
        if not adicao1 or not adicao2: 
            self.fail('Aluno não foi adicionado.')

 
    def test_012_lista_de_alunos(self):
        alunos = requests.get('http://localhost:5000/alunos')
        
        if alunos.status_code == 404:
            self.fail("O link está com erro | Não há alunos no server")
        
        try:
            obj_retornado = alunos.json()
        except:
            self.fail("Não foi retornado um json")
            
        self.assertIsInstance(obj_retornado, list)


    def test_013_aluno_por_id(self):
        aluno_id = requests.get('http://localhost:5000/alunos/1')
        dict_retornado = aluno_id.json()
        self.assertEqual(type(dict_retornado), dict)
        self.assertIn('nome', dict_retornado)
        self.assertEqual(dict_retornado['nome'], 'Ronaldo')


    def test_014_edita_aluno(self):
        requests.post('http://localhost:5000/alunos', json={ 
            'nome': 'Camila', 
            'idade' : 20,
            'turma_id' : 1,
            'data_nascimento' : '2005-02-06',
            'nota_primeiro_semestre' : 10.0,
            'nota_segundo_semestre' : 9.0
        })
        
        aluno_id_antes = requests.get('http://localhost:5000/alunos/3')
        self.assertEqual(aluno_id_antes.json()['nome'], "Camila")

        requests.put('http://localhost:5000/alunos/3', json={ 
            'nome': 'Camila Ribeiro', 
            'idade' : 22,
            'turma_id' : 2,
            'data_nascimento' : '2005-03-06',
            'nota_primeiro_semestre' : 10.0,
            'nota_segundo_semestre' : 8.0
        })
        
        aluno_id_depois = requests.get('http://localhost:5000/alunos/3')
        self.assertEqual(aluno_id_depois.json()['nome'],'Camila Ribeiro')
        self.assertEqual(aluno_id_depois.json()['id'], 3)
        
    def test_015_deleta_aluno(self):
        requests.post('http://localhost:5000/alunos', json={ 
            'nome': 'Jorginho', 
            'idade' : 22,
            'turma_id' : 2,
            'data_nascimento' : '2005-03-06',
            'nota_primeiro_semestre' : 5.0,
            'nota_segundo_semestre' : 9.0
        })

        requests.post('http://localhost:5000/alunos', json={ 
            'nome': 'Mariazinha', 
            'idade' : 22,
            'turma_id' : 2,
            'data_nascimento' : '2005-03-06',
            'nota_primeiro_semestre' : 6.0,
            'nota_segundo_semestre' : 7.0
        })

        requests.post('http://localhost:5000/alunos', json={ 
            'nome': 'Luan', 
            'idade' : 22,
            'turma_id' : 2,
            'data_nascimento' : '2005-03-06',
            'nota_primeiro_semestre' : 7.0,
            'nota_segundo_semestre' : 10.0
        })
        
        requests.delete('http://localhost:5000/alunos/4')

        alunos = requests.get('http://localhost:5000/alunos')
        lista_retornada = alunos.json()

        self.assertNotIn('Jorginho', [aluno['nome'] for aluno in lista_retornada])

        requests.delete('http://localhost:5000/alunos/6')

        alunos2 = requests.get('http://localhost:5000/alunos')
        lista_retornada2 = alunos2.json()

        self.assertNotIn('Luan', [aluno['nome'] for aluno in lista_retornada2])

       
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()