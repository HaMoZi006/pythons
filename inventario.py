from produto import Produto

class Inventario():
    def __init__(self) -> None:
        self.inventario: dict = {}
        self.dinheiro: float = 0

    
    def comprar(self, produto: Produto, qtde: float):
        if self.dinheiro >= qtde * produto.get_preco():
            if produto.nome in self.inventario.keys():
                self.inventario[produto.nome] += qtde
            else:
                self.inventario[produto.nome] = qtde
            
            print(f"voce comprou {qtde}x {produto.nome}")
            self.dinheiro -= qtde * produto.get_preco()
        else:
            raise Exception("O jogador não possui dinheiro suficiente para comprar o item")


    def add_dinheiro(self, dinheiro):
        self.dinheiro += dinheiro