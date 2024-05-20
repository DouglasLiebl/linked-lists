class Aluno:
    def __init__(self, nome, matricula, media):
        self.nome = nome
        self.matricula = matricula
        self.media = media
        self.proximo = None

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nMatricula: {self.matricula} \nMedia: {self.media}")

    
class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, nome, matricula, media):
        novo = Aluno(nome, matricula, media)
        novo.proximo = self.primeiro
        self.primeiro = novo
    
    def mostrar(self):
        if self.primeiro == None:
            print("A lista está vazia")
            return None

        atual =  self.primeiro
        while atual != None:
            atual.mostrar_dados()
            atual = atual.proximo

    
    def pesquisa(self, matricula):
        if self.primeiro == None:
            print("A lista está vazia")
            return None
    
        atual = self.primeiro
        while atual.matricula != matricula:
            if atual.proximo == None:
                return None
            else:
                atual = atual.proximo

        return atual.mostrar_dados()
    
    def excluir_posicao(self, matricula):
        if self.primeiro == None:
            print("A lista está vazia")
            return None
        
        atual = self.primeiro
        anterior = self.primeiro
        while atual.matricula != matricula:
            if atual.proximo != matricula:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        
        return atual.mostrar_dados()
    

print("Insere inicio:")
lista = ListaEncadeada()
lista.insere_inicio("Test", 123456, 7)
lista.mostrar()

print("\nExcluir por matricula:")
lista.excluir_posicao(123456)
lista.mostrar()

print("\nListar todos alunos:")
lista.insere_inicio("Test", 123456, 7)
lista.insere_inicio("Test", 1234567, 7)
lista.mostrar()

print("\nPesquisar por matricula:")
lista.pesquisa(123456)

