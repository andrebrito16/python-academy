class Carrinho:
  def __init__(self):
    self.dicionario = dict()
  
  def adiciona(self, nome_produto, preco):
    self.dicionario[nome_produto] = self.dicionario.get(nome_produto, 0) + preco

  def total_do_produto(self, nome_produto):
    return self.dicionario[nome_produto]

c = Carrinho()
c.adiciona('banana', 5)
total_banana = c.total_do_produto('banana')
print(total_banana)  # Vai imprimir 5
c.adiciona('abacate', 7)
c.adiciona('banana', 4)
total_banana = c.total_do_produto('banana')
print(total_banana)  # Vai imprimir 9