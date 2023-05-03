import numpy as np
from agente import Agente

jogo = Agente(4)
jogo.wumpus()
jogo.ouro()
jogo.buraco()

tamnho_matriz = jogo.tamanho
pontos = 0
jogo_ligado = True


def verificar_morte_wumpus(posicao):
    """Retorna se houve ou não a morte do wumpus."""
    if posicao is not False:
        if jogo.matriz[posicao] == 2:
            jogo.matriz[posicao] = 0
            jogo.quant_wumpus -= 1
            global pontos
            pontos += 100
            jogo.flecha = False
            return True
        else:
            jogo.flecha = False
            return False
    else:
        return direcao_atirar()


def direcao_atirar():
    """Atira para umas das direções NORTE, SUL, LESTE e OESTE."""
    diracao = np.random.randint(4)
    if diracao == 0:
        return verificar_morte_wumpus(jogo.atirar_norte())
    elif diracao == 1:
        return verificar_morte_wumpus(jogo.atirar_sul())
    elif diracao == 2:
        return verificar_morte_wumpus(jogo.atirar_leste())
    elif diracao == 3:
        return verificar_morte_wumpus(jogo.atirar_oeste())


def existe_outro_agente(nova_posicao):
    """Cofere se há outro agente na casa em que o caçador está."""
    posicao_cacador = jogo.posicao_cacador
    if nova_posicao is not False:
        agente = jogo.matriz[nova_posicao]
        if agente == 2 or agente == 4:
            global jogo_ligado
            jogo_ligado = False
        elif agente == 3:
            global pontos
            pontos += 50
            jogo.quant_ouro -= 1
            jogo.mover(posicao_cacador, nova_posicao)
        else:
            jogo.mover(posicao_cacador, nova_posicao)
    else:
        mover_para()


def mover_para():
    """ Movimenta o Caçador na Matrix"""
    direcao = np.random.randint(4)
    posicao_cacador = jogo.posicao_cacador
    if direcao == 0:
        existe_outro_agente(jogo.norte(posicao_cacador))
    elif direcao == 1:
        existe_outro_agente(jogo.sul(posicao_cacador))
    elif direcao == 2:
        existe_outro_agente(jogo.leste(posicao_cacador))
    elif direcao == 3:
        existe_outro_agente(jogo.oeste(posicao_cacador))


# Se o wumpus está proximo
sensacao = [i for i in jogo.percepcao_ambiente() if i == 2]
print(jogo.matriz)

while jogo_ligado:
    if jogo.quant_wumpus == 0 and jogo.quant_ouro == 0:
        print("Você Ganhou!")
        break

    try:
        if sensacao[0] == 2:
            if direcao_atirar() and jogo.flecha:
                mover_para()
                print(jogo.matriz)
            else:
                # Wumpus não morreu, mesmo assim mover
                mover_para()
                print()
                print(jogo.matriz)
        else:
            mover_para()
            print()
            print(jogo.matriz)
    except IndexError:
        mover_para()
        print()
        print(jogo.matriz)

print("Pontuação:", pontos)
print("Quantidade Ouro:", jogo.quant_ouro)
print("Quantidade Wumpus:", jogo.quant_wumpus)
print("Estado do Jogo:", jogo_ligado)
