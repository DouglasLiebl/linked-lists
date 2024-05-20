class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.proximo = None

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nPreco: {self.preco} \nEstoque: {self.estoque}")


class ListaEncadeadaExtremidadeDupla:

  def __init__(self):
    self.primeiro = None
    self.ultimo = None

  def __lista_vazia(self):
    return self.primeiro == None


  def insere_inicio(self, nome, preco, estoque):
    novo = Produto(nome, preco, estoque)
    if self.__lista_vazia():
      self.ultimo = novo
    novo.proximo = self.primeiro
    self.primeiro = novo

  def insere_final(self, nome, preco, estoque):
    novo = Produto(nome, preco, estoque)
    if self.__lista_vazia():
      self.primeiro = novo
    else:
      self.ultimo.proximo = novo
    self.ultimo = novo


  def excluir_inicio(self):
    if self.__lista_vazia():
      print('A lista está vazia')
      return

    temp = self.primeiro
    if self.primeiro.proximo == None:
      self.ultimo = None
    self.primeiro = self.primeiro.proximo
    return temp.valor
  
  def pesquisa(self, nome):
    if self.primeiro == None:
        print("A lista está vazia")
        return None

    atual = self.primeiro
    while atual.nome != nome:
        if atual.proximo == None:
            return None
        else:
            atual = atual.proximo

    return atual.mostrar_dados()
  
  def excluir_posicao(self, nome):
    if self.primeiro == None:
        print("A lista está vazia")
        return None
    
    atual = self.primeiro
    anterior = self.primeiro
    while atual.nome != nome:
        if atual.proximo.nome != nome:
            return None
        else:
            anterior = atual
            atual = atual.proximo
    
    if atual == self.primeiro:
        self.primeiro = self.primeiro.proximo
    else:
        anterior.proximo = atual.proximo
    
    return atual.mostrar_dados()

  def mostrar(self):
    if self.__lista_vazia():
      print('A lista está vazia')
      return
    atual = self.primeiro
    while atual != None:
      atual.mostrar_dados()
      atual = atual.proximo

print("Insere no inicio:")
lista = ListaEncadeadaExtremidadeDupla()
lista.insere_inicio("product1", 100, 2)
lista.insere_inicio("product2", 100, 2)
lista.mostrar()

print("\nInsere no final:")
lista.insere_final("product3", 100, 2)
lista.mostrar()


print("\nExcluir nome:")
lista.excluir_posicao("product1")

print("\nPrint com item Removido:")
lista.mostrar()

print("\nBuscar por nome: (product3)")
lista.pesquisa("product3")

print("\nMostrar toda lista:")
lista.insere_final("product1", 100, 2)
lista.mostrar()
