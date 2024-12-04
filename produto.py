import pygame as pg
class Produto():
    def __init__(self, nome: str, descricao: str, preco: int, cod_sprite) -> None:
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.cod_sprite = cod_sprite

        self.imagem = pg.image.load(["img/flashlight.png", "img/jetpack.png", "img/ladder.png", "img/lockpick.png", "img/shovel.png", "img/proflashlight.png", "img/cruiser.png", "img/walkietalkie.png"][cod_sprite])
        self.imagem = pg.transform.scale(self.imagem, (200, 200))       
    
    def get_preco(self) -> float:
        return self.preco
    

    def set_preco(self, preco) -> None:
        self.preco = preco
    

    def __str__(self) -> str:
        return f"{self.nome} por {self.preco:.2f} \n{self.descricao}"