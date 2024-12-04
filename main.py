import pygame as pg
import time
from lua import Lua
from produto import Produto
from inventario import Inventario

pg.init()

screen = pg.display.set_mode((1280, 720))
cor_letra = (56, 161, 21)
cor_fundo = (11, 11, 11)
cor_seta = (186, 9, 9)

clock = pg.time.Clock()


def menu_compra(lua: Lua, inventario: Inventario, produto: Produto):
    screen.fill(cor_fundo)
    fonte_nome = pg.font.SysFont("couriernew", 60, bold = True)
    fonte_descricao = pg.font.SysFont("couriernew", 30, bold = True)
    fonte_botao1 = pg.font.SysFont("couriernew", 98, bold = False)
    fonte_botao2 = pg.font.Font(None, 58)

    screen.blit(fonte_nome.render(f"{produto.nome} ____ ${produto.preco}", True, cor_letra), (400, 100))
    screen.blit(produto.imagem, (400, 250))
    screen.blit(fonte_descricao.render(produto.descricao, True, cor_letra), (100, 450))
    
    ctdr_seta = 0
    qtde = 0
    pg.display.flip()



    while True:
        pos_x_botoes = 200
        pos_y_botoes = 500

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_RIGHT:
                    ctdr_seta += 1
                if ev.key == pg.K_LEFT:
                    ctdr_seta -= 1
                if ev.key == pg.K_RETURN:
                    match ctdr_seta % 4:
                        case 0:
                            if qtde < 9:
                                qtde += 1
                        case 1:
                            if qtde > 0:
                                qtde -= 1
                        case 2:
                            try:
                                inventario.comprar(produto, qtde)
                                qtde = 0
                            except:
                                print("n deu")
                        case 3:
                            menu_loja(lua, inventario)
                
        pg.draw.rect(screen, cor_fundo, ((948, 19), (200, 65)))
        screen.blit(pg.font.SysFont("couriernew", 24, bold=True).render(f"$$ = {inventario.dinheiro:.2f}", True, cor_letra), (950, 20))



        screen.blit(fonte_botao1.render("o", True, cor_letra), (pos_x_botoes, pos_y_botoes))
        screen.blit(fonte_botao2.render("+", True, cor_letra), (pos_x_botoes + 18, pos_y_botoes + 37))
        pos_x_botoes += 150
        pg.draw.rect(screen, cor_fundo, ((pos_x_botoes - 4, pos_y_botoes - 4), (40, 100)))
        screen.blit(fonte_botao2.render(str(qtde), True, cor_letra), (pos_x_botoes, pos_y_botoes + 40))
        pos_x_botoes += 150
        screen.blit(fonte_botao1.render("o", True, cor_letra), (pos_x_botoes, pos_y_botoes))
        screen.blit(fonte_botao2.render("-", True, cor_letra), (pos_x_botoes + 18, pos_y_botoes + 37))
        aux1 = pos_x_botoes
        aux2 = pos_y_botoes
        pos_x_botoes += 280
        pos_y_botoes += 50
        screen.blit(fonte_descricao.render("Comprar", True, cor_letra), (pos_x_botoes, pos_y_botoes))

        pos_x_botoes += 300
        screen.blit(fonte_descricao.render("Voltar", True, cor_letra), (pos_x_botoes, pos_y_botoes))
 
        pg.display.flip()
        pos_x_botoes = aux1
        pos_y_botoes = aux2

        pos_y_botoes += 100
        pos_x_botoes -= 270
        pg.draw.rect(screen, cor_fundo, ((pos_x_botoes - 100, pos_y_botoes), (1200, 100)))
        pg.draw.polygon(screen, cor_seta, ((pos_x_botoes + (ctdr_seta % 4 * 300), pos_y_botoes), (pos_x_botoes - 15 + (ctdr_seta % 4 * 300), pos_y_botoes + 30), (pos_x_botoes + 15 + (ctdr_seta % 4 * 300), pos_y_botoes + 30)))


def abrir_inventario(lua: Lua, inventario: Inventario):
    screen.fill(cor_fundo)
    pg.display.flip()
    ctdr_seta_vertical = 0
    fonte = pg.font.SysFont("couriernew", 40, bold=True)
    
    
    pos_y_textos_menu = 150
    pos_inicio_seta = pos_y_textos_menu + 10
    pos_y_seta = pos_y_textos_menu
    pos_x_textos_menu = 300
    pos_x_seta = 270
    qtde_textos = 0
    for item in inventario.inventario:
        screen.blit(fonte.render(f"{item} --- {inventario.inventario[item]}", True, cor_letra), (pos_x_textos_menu, pos_y_textos_menu))
        pos_y_textos_menu += 50
        qtde_textos += 1
    screen.blit(fonte.render("Voltar", True, cor_letra), (pos_x_textos_menu, pos_y_textos_menu))
    qtde_textos += 1
    
    pg.display.flip()
    
    while True:
        for ev in pg.event.get():
            pg.display.flip()
            if ev.type == pg.QUIT:
                pg.quit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_DOWN:
                    ctdr_seta_vertical += 1
                if ev.key == pg.K_UP:
                    ctdr_seta_vertical -= 1

            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_RETURN:
                    if ctdr_seta_vertical % qtde_textos == qtde_textos - 1:
                        menu_iniciar(lua, inventario)
        pg.draw.rect(screen, cor_fundo, ((948, 19), (200, 65)))
        screen.blit(pg.font.SysFont("couriernew", 24, bold=True).render(f"$$ = {inventario.dinheiro:.2f}", True, cor_letra), (950, 20))
                            
        

        pos_y_seta = pos_inicio_seta + (ctdr_seta_vertical % qtde_textos * 50)

        pg.draw.rect(screen, cor_fundo, ((265, pos_inicio_seta), (35, 650)))
        pg.draw.polygon(screen, cor_seta, [(pos_x_seta, pos_y_seta), (pos_x_seta, pos_y_seta + 30), (pos_x_seta + 20, pos_y_seta + 15)])
        pg.display.flip()


def menu_loja(lua: Lua, inventario: Inventario):
    screen.fill(cor_fundo)
    pg.display.flip()
    ctdr_seta_vertical = 0

    pos_y_textos_menu = 150
    pos_inicio_seta = pos_y_textos_menu + 10
    pos_y_seta = pos_y_textos_menu
    pos_x_textos_menu = 300
    pos_x_seta = 270

    textos = ["Flashlight", "Jetpack", "Ladders", "Lockpick", "Shovel", "Pro Flashlight", "Cruiser", "Walkie-Talkie", "Voltar ao menu do jogo"]
    renderizar_texto = lambda texto: pg.font.SysFont("couriernew", 40, bold=True).render(texto, True, (56, 161, 21))
    produtos = [Produto(textos[0], "Serve para iluminar o caminho.", 15, 0), 
                Produto(textos[1], "Serve para você poder voar.", 900, 1), 
                Produto(textos[2], "Serve para poder subir em lugares altos.", 60, 2), 
                Produto(textos[3], "Serve para abrir uma porta trancada sem precisar de uma chave.", 20, 3), 
                Produto(textos[4], "Serve para atacar criaturas.", 30, 4), 
                Produto(textos[5], "Ilumina bem mais o caminho e a sua bateria dura por mais tempo.", 25, 5), 
                Produto(textos[6], "É um veículo que te permite ir mais rápido com os seus amigos.", 400, 6), 
                Produto(textos[7], "Serve para poder se comunicar com algum parceiro.", 12, 7)
                ]
    
    textos = list(map(renderizar_texto, textos))
    
    pg.display.flip()
    
    for i, texto in enumerate(textos):
        screen.blit(texto, (pos_x_textos_menu, pos_y_textos_menu))
        pos_y_textos_menu += 50
        # seletores[i].printar_seletor(screen, [pos_x_textos_menu + 550, pos_y_textos_menu + 20 * i])
    
    screen.blit(pg.font.SysFont("couriernew", 24, bold=True).render(f"$$ = {inventario.dinheiro:.2f}", True, cor_letra), (950, 20))


    while True:
        for ev in pg.event.get():
            pg.display.flip()
            if ev.type == pg.QUIT:
                pg.quit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_DOWN:
                    ctdr_seta_vertical += 1
                if ev.key == pg.K_UP:
                    ctdr_seta_vertical -= 1

            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_RETURN:
                    if ctdr_seta_vertical % 9 == 8:
                            menu_iniciar(lua, inventario)
                    else:
                        menu_compra(lua, inventario, produtos[ctdr_seta_vertical % 9])
        

        pos_y_seta = pos_inicio_seta + (ctdr_seta_vertical % 9 * 50)

        pg.draw.rect(screen, cor_fundo, ((265, pos_inicio_seta), (35, 650)))
        pg.draw.polygon(screen, cor_seta, [(pos_x_seta, pos_y_seta), (pos_x_seta, pos_y_seta + 30), (pos_x_seta + 20, pos_y_seta + 15)])


def menu_lua(lua: Lua, inventario: Inventario):
    screen.fill(cor_fundo)
    pg.display.flip()
    ctdr_seta = 0
    fonte = pg.font.SysFont("couriernew", 40, bold=True)
    pos_y_textos_menu = 150
    pos_inicio_seta = pos_y_textos_menu + 10
    pos_y_seta = pos_y_textos_menu
    pos_x_textos_menu = 300
    pos_x_seta = 270

    nome_lua: str = ""
    
    textos = [fonte.render("Experimentation", True, cor_letra),
              fonte.render("Assurance", True, cor_letra),
              fonte.render("Vow", True, cor_letra),
              fonte.render("Offense", True, cor_letra),
              fonte.render("March", True, cor_letra),
              fonte.render("Adamance", True, cor_letra),
              fonte.render("Rend", True, cor_letra),
              fonte.render("Dine", True, cor_letra),
              fonte.render("Titan", True, cor_letra),
              fonte.render("Voltar ao menu principal", True, cor_letra)]
    
    for texto in textos:
        screen.blit(texto, (pos_x_textos_menu, pos_y_textos_menu))
        pos_y_textos_menu += 50

    while True:
        for ev in pg.event.get():
            pg.display.flip()
            if ev.type == pg.QUIT:
                pg.quit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_DOWN:
                    ctdr_seta += 1
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_UP:
                    ctdr_seta -= 1

            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_RETURN:
                    match ctdr_seta % 10:
                        case 0:
                            nome_lua = "Experimentation"
                        case 1:
                            nome_lua = "Assurance"
                        case 2:
                            nome_lua = "Vow"
                        case 3:
                            nome_lua = "Offense"
                        case 4:
                            nome_lua = "March"
                        case 5:
                            nome_lua = "Adamance"
                        case 6:
                            nome_lua = "Rend"
                        case 7:
                            nome_lua = "Dine"
                        case 8:
                            nome_lua = "Titan"
                        case 9:
                            menu_iniciar(lua, inventario)
                    
                    lua.set_lua(nome_lua)
                    
        
        pos_y_seta = pos_inicio_seta + (ctdr_seta % 10 * 50)
        
        pg.draw.rect(screen, cor_fundo, ((265, pos_inicio_seta), (35, 650)))
        pg.draw.polygon(screen, cor_seta, [(pos_x_seta, pos_y_seta), (pos_x_seta, pos_y_seta + 30), (pos_x_seta + 20, pos_y_seta + 15)])


def fazer_scan(lua: Lua, inventario: Inventario):
    screen.fill(cor_fundo)
    pg.display.flip()
    fonte = pg.font.SysFont("couriernew", 42, bold=True)
    screen.blit(fonte.render(f"Lua: {lua.nome_lua}", True, cor_letra), (290, 100))
    screen.blit(fonte.render("Aguarde enquanto o scan é feito.", True, cor_letra), (290, 200))
    pos_x_carregamento = 200

    for _ in range(14): #simular carregamento, printando quadrados na tela
        pg.display.flip()
        pg.draw.rect(screen, cor_letra, ((pos_x_carregamento, 490), (60, 60)))
        pos_x_carregamento += 70
        time.sleep(0.6)

    if lua.status_scan():
        min, max = lua.get_range_scan()
        dinheiro = lua.fazer_scan(max, min)
        inventario.add_dinheiro(dinheiro)

    else:
        mostrar_saida(game_over=True)
    screen.fill(cor_fundo)
    
    screen.blit(fonte.render(f"Dinheiro ganho: {dinheiro}", True, cor_letra), (290, 200))
    screen.blit(fonte.render("Aguarde...", True, cor_letra), (290, 400))
    pg.display.flip()
    time.sleep(2.2)
    print(inventario.dinheiro)
    menu_iniciar(lua, inventario)


def menu_iniciar(lua: Lua, inventario: Inventario) -> None:
    screen.fill(cor_fundo)
    pg.display.flip()
    ctdr_seta = 0
    fonte = pg.font.SysFont("couriernew", 60, bold=True)
    pos_y_textos_menu = 170
    pos_inicio_seta = pos_y_textos_menu + 10
    pos_y_seta = pos_y_textos_menu
    pos_x_textos_menu = 300
    pos_x_seta = 270
    
    textos = [fonte.render("Escolher Lua", True, cor_letra),
              fonte.render("Loja", True, cor_letra),
              fonte.render("Fazer Scan", True, cor_letra),
              fonte.render("Inventário", True, cor_letra),
              fonte.render("Voltar ao menu inicial", True, cor_letra)]
    print(lua)
    for texto in textos:
        screen.blit(texto, (pos_x_textos_menu, pos_y_textos_menu))
        pos_y_textos_menu += 100

    while True:
        pg.display.flip()
        for ev in pg.event.get():
            pg.display.flip()
            if ev.type == pg.QUIT:
                pg.quit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_DOWN:
                    ctdr_seta += 1
                if ev.key == pg.K_UP:
                    ctdr_seta -= 1
                if ev.key == pg.K_RETURN:
                    match ctdr_seta % 45:
                        case 0:
                            menu_lua(lua, inventario)
                        case 1:
                            menu_loja(lua, inventario)
                        case 2:
                            fazer_scan(lua, inventario)
                        case 3:
                            abrir_inventario(lua, inventario)
                        case 4:
                            del lua
                            del inventario
                            main()
                        
        pos_y_seta = pos_inicio_seta + (ctdr_seta % 5 * 100)
        
        pg.draw.rect(screen, cor_fundo, ((265, pos_inicio_seta), (35, 650)))
        pg.draw.polygon(screen, cor_seta, [(pos_x_seta, pos_y_seta), (pos_x_seta, pos_y_seta + 30), (pos_x_seta + 20, pos_y_seta + 15)])


def mostrar_instruçoes() -> None:
    screen.fill(cor_fundo)
    fonte = pg.font.SysFont("couriernew", 24, bold=False)
    fonte_voltar = pg.font.SysFont("couriernew", 48, bold=True)
    textos = [fonte.render("Boas vindas à companhia! Esperamos que você tenha bons momentos",       True, cor_letra),
              fonte.render("trabalhando conosco! O seu trabalho como coletor será de extrema",      True, cor_letra),
              fonte.render("importância para nós.",                                                 True, cor_letra),
              fonte.render("Como você já sabe, a nossa companhia realizou inúmeros trabalhos em ",  True, cor_letra),
              fonte.render("várias luas diferentes. No entanto, ainda existem resquícios do nosso", True, cor_letra),
              fonte.render("trabalho nelas. Por isso, precisamos que alguém colete eles para nós.", True, cor_letra),
              fonte.render("Para isso, siga estas instruções:"                                    , True, cor_letra),
              fonte.render("1- Movimente-se nos menus utilizando as setas e a tecla Enter",         True, cor_letra),
              fonte.render("2 - Comece escolhendo a lua em que você deseja coletar o lixo na ",     True, cor_letra),
              fonte.render('seção: “Luas”.',                                                        True, cor_letra),
              fonte.render("3 - Depois, escolha a função: “Scan”, é nela que você ganhará o seu",   True, cor_letra),
              fonte.render("dinheiro. Porém, cuidado, há uma pequena chance de perder tudo!",       True, cor_letra),
              fonte.render("4 - Compre itens para te ajudar nessa jornada.",                        True, cor_letra),
              fonte.render("5 - Se divirta! ", True, cor_letra)]

    for i, texto in enumerate(textos):
        screen.blit(texto, (200, 80 + i * 40))
    screen.blit(fonte_voltar.render("Voltar", True, cor_letra), (200, ((i + 1) * 40) + 80))

    pos_x_seta = 170
    pos_y_seta = (i+1) * 40 + 80

    pg.draw.polygon(screen, cor_seta, [(pos_x_seta, pos_y_seta + 10), (pos_x_seta, pos_y_seta + 10 + 30), (pos_x_seta + 20, pos_y_seta + 10 + 15)])
    pg.display.flip()
    while True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_RETURN:
                    return


def mostrar_creditos() -> None:
    screen.fill(cor_fundo)
    pg.display.flip()
    fonte_nomes = pg.font.SysFont("couriernew", 50, bold=True)
    fonte_RA = pg.font.SysFont("couriernew", 36, bold=True)
    ctdr_seta = 0
    pos_y_textos_menu = 150
    pos_inicio_seta = pos_y_textos_menu + 10
    pos_y_seta = pos_y_textos_menu
    
    textos = [(fonte_nomes.render("Felipe Ríos dos Santos", True, cor_letra), fonte_RA.render("RA: 22403886", True, cor_letra)),
              (fonte_nomes.render("Ana Luísa Rigotti Leite", True, cor_letra), fonte_RA.render("RA: 22400558", True, cor_letra))]
    
    for texto_nome, texto_ra in textos:
        screen.blit(texto_nome, (300, pos_y_textos_menu))
        pos_y_textos_menu += 50
        screen.blit(texto_ra, (300, pos_y_textos_menu))
        pos_y_textos_menu += 130    
    screen.blit(fonte_nomes.render("Voltar", True, cor_letra), (300, pos_y_textos_menu))
    pg.display.flip()

    
    while True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_DOWN:
                    ctdr_seta += 1
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_UP:
                    ctdr_seta -= 1
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_RETURN:
                    if ctdr_seta % 3 == 2:
                        return
        pos_y_seta = pos_inicio_seta + (ctdr_seta % 3 * 180)
        
        pg.draw.rect(screen, cor_fundo, ((265, pos_inicio_seta), (35, 650)))
        pg.draw.polygon(screen, cor_seta, [(270, pos_y_seta), (270, pos_y_seta + 30), (290, pos_y_seta + 15)])
        pg.display.flip()


def mostrar_saida(game_over = False) -> None:
    fonte = pg.font.SysFont("couriernew", 80, bold= True)
    screen.fill(cor_fundo)
    if game_over:
        screen.blit(fonte.render("GAME   OVER", True, cor_letra), (590, 340))
    else:
        screen.blit(fonte.render("Obrigado por jogar!", True, cor_letra), (190, 340))
    pg.display.flip()
    time.sleep(2)
    pg.quit() # tchau


def main() -> None:
    fonte = pg.font.SysFont("couriernew", 50, bold= True)
    textos =  [fonte.render("Iniciar", True, cor_letra),
            fonte.render("Instruções", True, cor_letra),
            fonte.render("Créditos", True, cor_letra),
            fonte.render("Sair", True, cor_letra)]

    pos_y_textos_menu = 300
    pos_x_seta = 560
    pos_x_textos_menu = 590
    ctdr_seta = 0
    while True:
        screen.fill(cor_fundo)
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                game = False
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_DOWN:
                    ctdr_seta += 1
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_UP:
                    ctdr_seta -= 1

            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_RETURN:
                    match ctdr_seta % 4:
                        case 0:
                            lua_jogo = Lua()
                            inventario = Inventario()
                            print(lua_jogo)
                            menu_iniciar(lua_jogo, inventario)
                        case 1:
                            mostrar_instruçoes()
                        case 2:
                            mostrar_creditos()
                        case 3:
                            mostrar_saida()
                    
        pos_y_seta = pos_y_textos_menu + (ctdr_seta % 4 * 80)

        pg.draw.rect(screen, cor_fundo, ((550, 290), (40, 400)))
        pg.draw.polygon(screen, cor_seta, [(pos_x_seta, pos_y_seta + 10), (pos_x_seta, pos_y_seta + 10 + 30), (pos_x_seta + 20, pos_y_seta + 10 + 15)])
        screen.blit(textos[0], (pos_x_textos_menu, pos_y_textos_menu))
        screen.blit(textos[1], (pos_x_textos_menu, pos_y_textos_menu + 80))
        screen.blit(textos[2], (pos_x_textos_menu, pos_y_textos_menu + 160))
        screen.blit(textos[3], (pos_x_textos_menu, pos_y_textos_menu + 240))


        pg.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()