import requests
import unittest

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
        r = requests.post('http://localhost:5000/aluno', json={'nome': 'Ronaldo', 'id':4})
        r = requests.post('http://localhost:5000/aluno', json={'nome': 'Marcola', 'id':5})
        
        r_lista =  requests.get('http://localhost:5000/aluno')
        lista_retornada = r_lista.json()
        adicao1 = False
        adicao2 = False
        
        for aluno in lista_retornada:
            if aluno['nome'] == 'Ronaldo':
                adicao1 = True
            if aluno['nome'] == 'Marcola':
                adicao2 = True
            
        if not adicao1: 
            self.fail('Aluno adicionado: "Ronaldo" não apareceu na lista de alunos')
        if not adicao2:
            self.fail('Aluno adicionado: "Marcola" não apareceu na lista de alunos')

    def test_002_request_id_aluno(self):
        r = requests.post('http://localhost:5000/aluno', json={'nome':"noemi", 'id':26})
        
        resposta = requests.get('http://localhost:5000/aluno/26')
        dict_retornado = resposta.json()
        self.assertEqual(type(dict_retornado), dict)
        self.assertIn('nome', dict_retornado)
        self.assertEqual(dict_retornado['nome'],'noemi')
   
    def test_003_deletar_aluno(self):
        requests.post('http://localhost:5000/aluno', json={'nome':'Jorginho', 'id':23})
        requests.post('http://localhost:5000/aluno', json={'nome':'Mariazinha', 'id':24})
        requests.post('http://localhost:5000/aluno', json={'nome':'Luan', 'id':25})
        
        requests.delete('http://localhost:5000/aluno/24')
        requests.delete('http://localhost:5000/aluno/1')
        requests.delete('http://localhost:5000/aluno/2')
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

        if lista_retornada2[0]['nome'] == 'Jorginho':
            pass
        else:
            self.fail("Aluno errado deletado")

    def test_004_edita_aluno(self):
        requests.post('http://localhost:5000/aluno',json={'nome':'Marquinhos','id':14})
        r_lista_antes = requests.get('http://localhost:5000/aluno/14')
        self.assertEqual(r_lista_antes.json()['nome'],'Marquinhos')
        
        requests.put('http://localhost:5000/aluno/14', json={'nome':'Marcos Almeida'})
        
        r_lista_depois = requests.get('http://localhost:5000/aluno/14')
        self.assertEqual(r_lista_depois.json()['nome'],'Marcos Almeida')
        self.assertEqual(r_lista_depois.json()['id'],14)
    
    def test_200_turma(self):
        r = requests.get("http://localhost:5000/turma")
        
        if r.status_code == 404:
            self.fail("Link não está funcionando/Não ha turmas")
            
        try:
            obj_retornado = r.json()
        except:
            self.fail("Objeto não é um json")
            
        self.assertIsInstance(obj_retornado, list)
        
    def test_201_adicionar_turma(self):
        r= requests.post("http://localhost:5000/turma", json={'nome':'Turma 1', 'id':2})
        r_lista = requests.get("http://localhost:5000/turma")
        retornada = r_lista.json()
        Turma = False
        for turmas in retornada:
            if turmas == "Turma 1":
                Turma = True
        if not Turma:
            self.fail("A turma não foi adicionada corretamente")
            
    def test_202_turma_id(self):
        r = requests.post("http://localhost:5000/turma", json={'nome':'turma 2','id':4})
        
        resposta = requests.get('http://localhost:5000/turma/4')
        dict_retornado = resposta.json()
        self.assertEqual(type(dict_retornado), dict)
        self.assertIn('nome', dict_retornado)
        self.assertEqual(dict_retornado['nome'],'turma 2')
        
    def test_203_remover_turma(self):
        requests.post('http://localhost:5000/turma', json={'nome':'turma Ads', 'id':10})
        requests.post('http://localhost:5000/turma', json={'nome':'turma bd', 'id':11})
        requests.post('http://localhost:5000/turma', json={'nome':'turma ci', 'id':12})
        
        requests.delete('http://localhost:5000/turma/10')
        requests.delete('http://localhost:5000/turma/2')
        requests.delete('http://localhost:5000/turma/1')
        
        r_lista = requests.get('http://localhost:5000/turma')
        lista_retornada = r_lista.json()
        validate1 = False
        validate2 = False
        
        for turma in lista_retornada:
            if turma['nome'] == 'turma bd':
                validate1 = True
            if turma['nome'] == 'turma ci':
                validate2 = True
        if not validate1 or not validate2:
            self.fail("Deletou a turma errada")
            
        requests.delete('http://localhost:5000/turma/11')
        
        r_lista2 = requests.get('http://localhost:5000/turma')
        lista_retornada2 = r_lista2.json
        if lista_retornada2[0]['nome'] == 'turma ci':
            pass
        else:
            self.fail('Deletou a turma errada')
            
    def test_204_mudar_turma(self):
        requests.post('http://localhost:5000/turma', json={'nome':'turma de portugues','id':3})
        r_lista_before = requests.get('http://localhost:5000/turma/3')
        self.assertEqual(r_lista_before.json()['nome'],'turma de portugues')
        
        requests.put('http://localhost:5000/turma',json={'nome':'turma de matematica'})
        r_lista_after = requests.get('http://localhost:5000/turma14')
        self.assertEqual(r_lista_after.json()['nome'],'turma de matematica')
        self.assertEqual(r_lista_after.json()['id'],3)
        
        

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()