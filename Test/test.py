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
        r = requests.post('http://localhost:5000/aluno', json={'nome': 'Ronaldo', 'id':1})
        r = requests.post('http://localhost:5000/aluno', json={'nome': 'Marcola', 'id':2})
        
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
        r = requests.post('http://localhost:5000/aluno', json={'nome':"noemi", 'id':23})
        
        resposta = requests.get('http://localhost:5000/aluno/23')
        dict_retornado = resposta.json()
        self.assertEqual(type(dict_retornado), dict)
        self.assertIn('nome', dict_retornado)
        self.assertEqual(dict_retornado['nome'],'noemi')
   
    def test_003_deletar_aluno(self):
        requests.post('http://localhost:5000/aluno', json={'nome':'Jorginho', 'id':23})
        requests.post('http://localhost:5000/aluno', json={'nome':'Mariazinha', 'id':24})
        requests.post('http://localhost:5000/aluno', json={'nome':'Luan', 'id':25})
        
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
