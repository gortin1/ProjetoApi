import requests
import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_000_alunos_retorna_lista(self):
        r = requests.get('http://localhost:5000/aluno')
        
        if r.status_code == 404:
            self.fail("O link está com erro/Não há alunos no server")
        
        try:
            obj_retornado = r.json
        except:
            self.fail("Não foi retornado um json")
        
        
        self.assertEqual(type(obj_retornado),type([]))
   
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
        
        resposta = requests.get('http://localhost:5000/aluno')
        dict_retornado = resposta.json()
        self.assertEqual(type(dict_retornado), dict)
        self.assertIn('nome', dict_retornado)
        self.assertEqual(dict_retornado['nome'],'noemi')
   
    def test_003_deletar_aluno(self):
        r_lista = requests.get('http://localhost:5000/alunos')
        lista_retornada = r_lista.json()
    
        self.assertEqual(len(lista_retornada),3)
        
        requests.delete('http://localhost:5000/alunos/28')
        
        r_lista2 = requests.get('http://localhost:5000/alunos')
        lista_retornada2 = r_lista2.json()
        self.assertEqual(len(lista_retornada2),2)
        acheiMarta = False
        acheiCicero = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'marta':
                acheiMarta=True
            if aluno['nome'] == 'cicero':
                acheiCicero=True
        if not acheiMarta or not acheiCicero:
            self.fail("voce parece ter deletado o aluno errado!")

        requests.delete('http://localhost:5000/alunos/27')

        r_lista3 = requests.get('http://localhost:5000/alunos')
        lista_retornada3 = r_lista3.json()
        
        self.assertEqual(len(lista_retornada3),1) 

        if lista_retornada3[0]['nome'] == 'cicero':
            pass
        else:
            self.fail("voce parece ter deletado o aluno errado!")

