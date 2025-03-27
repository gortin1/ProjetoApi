import requests
import unittest
from datetime import date


class TestStringMethods(unittest.TestCase):
    
    def test_000_alunos_retorna_lista(self):
        r = requests.get('http://localhost:5000/aluno')
        
        if r.status_code == 404:
            self.fail("O link está com erro/Não há alunos no server")
        
        try:
            obj_retornado = r.json()
        except:
            self.fail("Não foi retornado um json")
            
        self.assertIsInstance(obj_retornado, list)
   
    def test_001_adicionar_aluno(self):
        requests.post('http://localhost:5000/aluno', json={'nome': 'Ronaldo', 'id':3, 'turma_id' : 2})
        requests.post('http://localhost:5000/aluno', json={'nome': 'Marcola', 'id':4, 'turma_id' : 1})
        
        r_lista =  requests.get('http://localhost:5000/aluno')
        lista_retornada = r_lista.json()
        adicao1 = False
        adicao2 = False
        
        for aluno in lista_retornada:
            if aluno['nome'] == 'Ronaldo':
                adicao1 = True
            if aluno['nome'] == 'Marcola':
                adicao2 = True
            
        if not adicao1 or not adicao2: 
            self.fail('Aluno não apareceu na lista de alunos')

    def test_002_request_id_aluno(self):
        r = requests.post('http://localhost:5000/aluno', json={'nome':"noemi", 'id':21, 'turma_id' : 2})
        
        resposta = requests.get('http://localhost:5000/aluno/21')
        dict_retornado = resposta.json()
        self.assertEqual(type(dict_retornado), dict)
        self.assertIn('nome', dict_retornado)
        self.assertEqual(dict_retornado['nome'],'noemi')
   
    def test_003_deletar_aluno(self):
        requests.post('http://localhost:5000/aluno', json={'nome':'Jorginho', 'id':23, 'turma_id' : 2})
        requests.post('http://localhost:5000/aluno', json={'nome':'Mariazinha', 'id':24, 'turma_id' : 2})
        requests.post('http://localhost:5000/aluno', json={'nome':'Luan', 'id':25, 'turma_id' : 2})
        
        requests.delete('http://localhost:5000/aluno/24')
        r_lista = requests.get('http://localhost:5000/aluno')
        lista_retornada = r_lista.json()
        adicao1 = False
        adicao2 = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'Jorginho':
                adicao1 = True
            if aluno['nome'] == 'Luan':
                adicao2 = True
        if not adicao1 or not adicao2:
            self.fail("Deletou o aluno errado")

        requests.delete('http://localhost:5000/aluno/25')

        r_lista2 = requests.get('http://localhost:5000/aluno')
        lista_retornada2 = r_lista2.json()

        for aluno in lista_retornada2:
            if aluno['nome'] == 'Jorginho':
                pass
        if aluno['nome'] != 'Jorginho':
             self.fail("Aluno errado deletado")

    def test_004_edita_aluno(self):
        requests.post('http://localhost:5000/aluno',json={"id": 1, 
            "nome": "Camila", 
             "idade": 20, 
             "turma_id": 1, 
             "data_nascimento":"2025,3,14",
             "nota_primeiro_semestre": 10.0,
             "nota_segundo_semestre": 9.0,
             "media_final": 9.5})
        
        r_lista_antes = requests.get('http://localhost:5000/aluno/1')
        self.assertEqual(r_lista_antes.json()['nome'],"Camila")
        
        requests.put('http://localhost:5000/aluno/1', json={"nome": "Camila Teste", 
             "idade": 21, 
             "turma_id": 1, 
             "data_nascimento":"2025,3,14",
             "nota_primeiro_semestre": 10.0,
             "nota_segundo_semestre": 9.0,
             "media_final": 9.5})
        
        r_lista_depois = requests.get('http://localhost:5000/aluno/1')
        self.assertEqual(r_lista_depois.json()['nome'],'Camila Teste')
        self.assertEqual(r_lista_depois.json()['id'],1)
        
    def test_005_edita_aluno_patch(self):
        requests.post('http://localhost:5000/aluno',json={"id": 44, 
            "nome": "Aldair", 
            "idade": 22, 
            "turma_id": 1, 
            "data_nascimento":"2025,3,14",
            "nota_primeiro_semestre": 10.0,
            "nota_segundo_semestre": 9.0,
            "media_final": 9.5})
        
        r_lista_antes = requests.get('http://localhost:5000/aluno/44')
        self.assertEqual(r_lista_antes.json()['nome'],"Aldair")
        
        requests.patch('http://localhost:5000/aluno/44', json={"nome": "Aldair Teste", 
            "idade": 21, 
            "turma_id": 1, 
        })
        r_lista_depois = requests.get('http://localhost:5000/aluno/44')
        self.assertEqual(r_lista_depois.json()['nome'],'Aldair Teste')
        self.assertEqual(r_lista_depois.json()['id'],44)

#----------------------------------------------------------------------------

    def test_004_professor_retorna_lista(self):
        r = requests.get('http://localhost:5000/professor')
        
        if r.status_code == 404:
            self.fail("O link está com erro/Não há professores no server")
        
        try:
            obj_retornado = r.json()
        except:
            self.fail("Não foi retornado um json")
            
        self.assertIsInstance(obj_retornado, list)
   
    def test_006_adicionar_professor(self):
        requests.post('http://localhost:5000/professor', json= {"id": 1, "nome": "Gabriel", "idade": 20, "materia": "Portugues", "observacoes": "Aula de Segunda"})
        requests.post('http://localhost:5000/professor', json= {"id": 2, "nome": "Marcella", "idade": 18, "materia": "Api", "observacoes": "Aula de quarta"})
        
        r_lista =  requests.get('http://localhost:5000/professor')
        lista_retornada = r_lista.json()
        adicao1 = False
        adicao2 = False
        
        for aluno in lista_retornada:
            if aluno['nome'] == 'Gabriel':
                adicao1 = True
            if aluno['nome'] == 'Marcella':
                adicao2 = True
            
        if not adicao1 or not adicao2: 
                self.fail('Professores não apareceu na lista')

    def test_007_request_id_professor(self):
        requests.post('http://localhost:5000/professor', json= {"id": 5, "nome": "Carol", "idade": 17, "materia": "Historia", "observacoes": "Aula de Sexta"})
        
        resposta = requests.get('http://localhost:5000/professor/5')
        dict_retornado = resposta.json()
        self.assertEqual(type(dict_retornado), dict)
        self.assertIn('nome', dict_retornado)
        self.assertEqual(dict_retornado['nome'],'Carol')
   
    def test_008_deletar_professor(self):
        requests.post('http://localhost:5000/professor', json={'id':50, 'nome':'Carlos', 'idade': 22, 'materia': "Geografia", 'observacoes': "Aula de recuperação"})
        requests.post('http://localhost:5000/professor', json={'id':51, 'nome':'Caio', 'idade': 25, 'materia': "Mobile", 'observacoes': "Aula de Quarta"})
        requests.post('http://localhost:5000/professor', json={'id':53, 'nome':'Geovane', 'idade': 27, 'materia': "Matematica", 'observacoes': "Aula de Quinta"})
        
        requests.delete('http://localhost:5000/professor/51')
        r_lista = requests.get('http://localhost:5000/professor')
        lista_retornada = r_lista.json()
        adicao1 = False
        adicao2 = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'Carlos':
                adicao1 = True
            if aluno['nome'] == 'Geovane':
                adicao2 = True
        if not adicao1 or not adicao2:
            self.fail("Deletou o professor errado")

        requests.delete('http://localhost:5000/professor/50')

        r_lista2 = requests.get('http://localhost:5000/professor')
        lista_retornada2 = r_lista2.json()

        for aluno in lista_retornada2:
            if aluno['nome'] == 'Geovane':
                pass
        if aluno['nome'] != 'Geovane':
             self.fail("Professor errado deletado")

    def test_009_edita_professor(self):
        requests.post('http://localhost:5000/professor', json={'id':18, 'nome':'Nicolas', 'idade': 19, 'materia': "Matematica", 'observacoes': "Aula de Quinta"})

        r_lista_antes_professor = requests.get('http://localhost:5000/professor/18')
        self.assertEqual(r_lista_antes_professor.json()['nome'],'Nicolas')
        
        requests.put('http://localhost:5000/professor/18', json={'nome':'Nicolas Lima', 'idade': 19, 'materia': "full stack", 'observacoes': "Aula de Quinta"})
        
        r_lista_depois_professor = requests.get('http://localhost:5000/professor/18')
        self.assertEqual(r_lista_depois_professor.json()['nome'],'Nicolas Lima')
        self.assertEqual(r_lista_depois_professor.json()['id'],18)
        
    def test_009_edita_professor_patch(self):
        requests.post('http://localhost:5000/professor', json={'id':28, 'nome':'Miguel', 'idade': 13, 'materia': "DevOps", 'observacoes': "Aula de Segunda"})

        r_lista_antes_professor = requests.get('http://localhost:5000/professor/28')
        self.assertEqual(r_lista_antes_professor.json()['nome'],'Miguel')
        
        requests.patch('http://localhost:5000/professor/28', json={'nome':'Miguel Lima', 'idade': 13, 'materia': "Espanhol", 'observacoes': "Aula de domingo"})
        
        r_lista_depois_professor = requests.get('http://localhost:5000/professor/28')
        self.assertEqual(r_lista_depois_professor.json()['nome'],'Miguel Lima')
        self.assertEqual(r_lista_depois_professor.json()['id'],28)
    
    def test_010_turma(self):
        r = requests.get("http://localhost:5000/turma")
        
        if r.status_code == 404:
            self.fail("Link não está funcionando/Não ha turmas")
            
        try:
            obj_retornado = r.json()
        except:
            self.fail("Objeto não é um json")
            
        self.assertIsInstance(obj_retornado, list)
        
    def test_011_adicionar_turma(self):
        r= requests.post("http://localhost:5000/turma", json={'descricao':'Turma 1', 'id':3, "professor_id": 1})
        r_lista = requests.get("http://localhost:5000/turma")
        retornada = r_lista.json()
        Turma = False
        for turmas in retornada:
            if turmas['descricao'] == "Turma 1":
                Turma = True
        if not Turma:
            self.fail("A turma não foi adicionada corretamente")
            
    def test_012_turma_id(self):
        r = requests.post("http://localhost:5000/turma", json={'descricao':'turma 2','id': 4, "professor_id": 1})
        
        resposta = requests.get('http://localhost:5000/turma/4')
        dict_retornado = resposta.json()
        self.assertEqual(type(dict_retornado), dict)
        self.assertIn('descricao', dict_retornado)
        self.assertEqual(dict_retornado['descricao'],'turma 2')
        
    def test_013_remover_turma(self):
        requests.post('http://localhost:5000/turma', json={'descricao':'turma Ads', 'id':10, "professor_id": 1})
        requests.post('http://localhost:5000/turma', json={'descricao':'turma bd', 'id':11, "professor_id": 1})
        requests.post('http://localhost:5000/turma', json={'descricao':'turma ci', 'id':12, "professor_id": 1})
        
        requests.delete('http://localhost:5000/turma/10')
        
        r_lista = requests.get('http://localhost:5000/turma')
        lista_retornada = r_lista.json()
        validate1 = False
        validate2 = False
        validate3 = False
        
        for turma in lista_retornada:
            if turma['descricao'] == 'turma bd':
                validate1 = True
            if turma['descricao'] == 'turma ci':
                validate2 = True
        if not validate1 or not validate2:
            self.fail("Deletou a turma errada")
            
        requests.delete('http://localhost:5000/turma/11')
        
        r_lista2 = requests.get('http://localhost:5000/turma')
        lista_retornada2 = r_lista2.json()
        for turma in lista_retornada2:
            if turma['descricao'] == 'turma ci':
                validate3 = True
        if not validate3:
            self.fail('Deletou a turma errada')
              
    def test_014_mudar_turma(self):
        requests.post('http://localhost:5000/turma', json={'descricao':'turma de portugues','id':14, "professor_id": 1, "ativo" : True})
        r_lista_before = requests.get('http://localhost:5000/turma/14')
        self.assertEqual(r_lista_before.json()['descricao'],'turma de portugues')
        
        requests.put('http://localhost:5000/turma/14',json={'descricao':'turma de matematica', "professor_id": 1,"ativo" : True})
        r_lista_after = requests.get('http://localhost:5000/turma/14')
        self.assertEqual(r_lista_after.json()['descricao'],'turma de matematica')
        self.assertEqual(r_lista_after.json()['id'],14)
        
    def test_014_mudar_turma_path(self):
        requests.post('http://localhost:5000/turma', json={'descricao':'turma de java','id':64, "professor_id": 1, "ativo" : True})
        r_lista_before = requests.get('http://localhost:5000/turma/64')
        self.assertEqual(r_lista_before.json()['descricao'],'turma de java')
        
        requests.patch('http://localhost:5000/turma/64',json={'descricao':'turma de python', "professor_id": 1})
        r_lista_after = requests.get('http://localhost:5000/turma/64')
        self.assertEqual(r_lista_after.json()['descricao'],'turma de python')
        self.assertEqual(r_lista_after.json()['id'],64)
        
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()