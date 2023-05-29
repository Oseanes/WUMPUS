from numpy import random
from ambiente import Ambiente


# -------Métodos-------
def perceber_ambiente():
    """Verifica quais sensações estão prensente no ambiente e as Retornam."""
    percep = []
    for posicao_adjacente in cacador.posicao_adjacente(tamanho_matriz):
        if posicao_adjacente is not False:
            sensacao_ambiente = matriz[posicao_adjacente].sensacao
            if sensacao_ambiente is not None and sensacao_ambiente != "brilho":
                percep.append(sensacao_ambiente)
    return percep


def perigo(lista_percepcao):
    """Verifica se o caçador precisa ficar em alerta
    Retorna FALSE ou TRUE."""
    if 'fedor' or 'brisa' in lista_percepcao:
        return True


def upload_historico(pos_anterior, tamanho, lista_percepcao, d_historico, ir_para_posicao):
    """Armazena as informações no dicionário. Recebe como parametro:
    pos_anterior: Posição anterior do caçador,
    tamanho: O tamanho da Matriz
    lista_percepcao: precepção daquela posição
    ir_para_posicao: posição eslhida para mover
    d_historico: o dicionário com todas as informações"""

    # Verifica se a posição já foi inserida no histórico
    # Caso não esteja faz a inserção das informações relacionada a essa posição.
    if not (cacador.posicao in d_historico.keys()) or None:
        d_historico[cacador.posicao] = {'posicao_anterior': pos_anterior,
                                        'posicao_adjacente': cacador.posicao_adjacente(tamanho),
                                        'percepcao': lista_percepcao,
                                        'posicao_escolhida': ir_para_posicao}


def atirar(posicao_atirar):
    """Atira e Retorna se houve ou não a morte do wumpus."""
    if posicao_atirar is not False:
        wumpus = matriz[posicao_atirar]
        if wumpus.sensacao == "fedor" and cacador.flecha is True:
            cacador.pontuacao += 1000
            cacador.flecha = False
            cacador.wumpus_morto = True
            jogo.remover_wumpus(posicao_atirar)
            return True
        else:
            cacador.flecha = False
            return False


def posicao_(l_casas_perigosas, l_casas_seguras, l_casas_percorridas, d_historico):
    """Retorna uma posição paseada nas entreadas:
    l_casas_perigosas: Todas as casas que o caçador infere ser perigosas,
    l_casas_seguras: Todas as casas que o caçador infere ser seguras,
    l_casas_percorridas: Todas as casas já percorrida pelo caçador,
    d_historico: Tod histórico com as informações colhidas do ambente onde já esteve """

    percepcao_ambiente = perceber_ambiente()
    casas_adjacentes_cacador = cacador.posicao_adjacente(tamanho_matriz)

    if bool(percepcao_ambiente) is False:
        casas_possiveis = [item for item in casas_adjacentes_cacador if item not in l_casas_percorridas]
        if bool(casas_possiveis) is False:
            i = random.randint(0, len(casas_adjacentes_cacador))
            return casas_adjacentes_cacador[i]
        elif len(casas_possiveis) > 1:
            i = random.randint(0, len(casas_possiveis))
            return casas_possiveis[i]
        else:
            return casas_possiveis[0]
    else:
        casas_possiveis_ = [item for item in casas_adjacentes_cacador if item not in l_casas_perigosas]
        casas_possiveis = casas_possiveis_
        if bool(casas_possiveis):
            casas_possiveis = [item for item in casas_possiveis if item not in l_casas_percorridas]
        if bool(casas_possiveis):
            casas_possiveis = [item for item in casas_possiveis if item in l_casas_seguras]
        if bool(casas_possiveis) is False:
            # A casa 5 passos faz uma escolha aleatória
            if cacador.passos > tamanho_matriz:
                cacador.passos = 0
                #print("----------------------------------")
                i = random.randint(0, len(casas_possiveis_))
                return casas_possiveis_[i]
            else:
                voltar_pos_anterior(cacador.posicao, d_historico)

        else:
            if len(casas_possiveis) > 1:
                i = random.randint(0, len(casas_possiveis))
                return casas_possiveis[i]
            else:
                return casas_possiveis[0]


def voltar_pos_anterior(c_posicao, d_historico):
    """Volta para a posição anterior"""
    if c_posicao != (0, 0):
        posicao_voltar = d_historico[c_posicao]['posicao_anterior']
        jogo.mover(p_cacador=c_posicao, nova_posicao=posicao_voltar)
    else:
        # Vai na direção oposta a inicial
        casas_adjacentes_cacador = cacador.posicao_adjacente(tamanho_matriz)
        i = random.randint(0, len(casas_adjacentes_cacador))
        jogo.mover(p_cacador=c_posicao, nova_posicao=casas_adjacentes_cacador[i])


def procesar_historico(l_casas_percorridas, d_historico):
    """Retorna possível casa perigo e posivel habitante.
    Processa as informações hitórias e faz inferencia com base nelas"""
    casas_intercecao = []
    for casa_percorida in l_casas_percorridas:
        if casa_percorida != cacador.posicao:
            for posicao_adjacente in d_historico[casa_percorida]['posicao_adjacente']:
                if posicao_adjacente in cacador.posicao_adjacente(tamanho_matriz):
                    casas_intercecao.append([casa_percorida, posicao_adjacente])

    if bool(casas_intercecao):
        casas_intercecao_ = []
        for item in casas_intercecao:
            if item[1] not in l_casas_percorridas:
                casas_intercecao_.append(item)

        if bool(casas_intercecao_):
            casas_intercecao_ = casas_intercecao_[0]
            casas_intercecao_perigo = casas_intercecao_[1]
            posicao_historica_percep = casas_intercecao_[0]
            for percepcao_historica in d_historico[posicao_historica_percep]['percepcao']:
                if percepcao_historica in perceber_ambiente():
                    return [casas_intercecao_perigo, percepcao_historica]


def inferir(l_casas_percorridas, d_historico):
    """Age de acordo com inferencias feitas com base nas informações
    historicas."""
    busca = procesar_historico(l_casas_percorridas, d_historico)
    if busca:
        habitante = busca[1]
        casa_perigosa = busca[0]
        if habitante == 'fedor':
            atirar(casa_perigosa)
        elif habitante == 'brisa':
            cacador.casa_com_buraco.add(casa_perigosa)


def voltar_caminho_curto(casas_percorrida):
    posicao_obj_concluido = cacador.posicao
    linha_cacador = posicao_obj_concluido[1]
    coluna_cacador = posicao_obj_concluido[0]
    posicao_voltar = []
    for posicao in casas_percorrida:
        linha1 = posicao[1]
        coluna2 = posicao[0]
        if linha_cacador >= linha1 and coluna_cacador >= coluna2:
            if posicao in cacador.posicao_adjacente(tamanho_matriz):
                posicao_voltar.append(posicao)
                jogo.mover(cacador.posicao, posicao)
                print()
                print(jogo.print_matrix())
    print("lista casa voltar:", posicao_voltar)
    jogo.jogo_on = False


tamanho_matriz = 6
jogo = Ambiente(tamanho_matriz)
matriz = jogo.matriz
cacador = matriz[(0, 0)]
# Lista com informações relevantes
historico = {}
casas_perigosa = cacador.casa_com_buraco
casas_seguras = set()
casas_percorridas = cacador.casas_percorridas

while cacador.vivo and jogo.jogo_on:
    print(jogo.print_matrix())
    print()

    percepcoes_atuais = perceber_ambiente()
    casa_anterior = jogo.casa_anterior
    if cacador.ouro_coletado and cacador.wumpus_morto:
        print("Valeu Paixe!\n Pontuação:", cacador.pontuacao)
        casas_percorridas = sorted(list(casas_percorridas), key=tuple, reverse=True)
        voltar_caminho_curto(casas_percorridas)
    if cacador.posicao_anterior is None:
        #print(jogo.print_matrix())
        cacador.casas_percorridas.add(cacador.posicao)
        cacador.posicao_anterior = cacador.posicao
        upload_historico(pos_anterior=casa_anterior,
                         tamanho=tamanho_matriz,
                         lista_percepcao=percepcoes_atuais,
                         d_historico=historico,
                         ir_para_posicao=(1, 0))
        jogo.mover(p_cacador=cacador.posicao, nova_posicao=(1, 0))

    else:
        percepcao_atual_ambiente = perceber_ambiente()
        upload_historico(pos_anterior=casa_anterior,
                         tamanho=tamanho_matriz,
                         lista_percepcao=percepcoes_atuais,
                         d_historico=historico,
                         ir_para_posicao=(1, 0))

        if bool(percepcao_atual_ambiente) is False:
            for item in cacador.posicao_adjacente(tamanho_matriz):
                casas_seguras.add(item)

            nova_posicao = posicao_(l_casas_perigosas=casas_perigosa,
                                    l_casas_percorridas=casas_percorridas,
                                    l_casas_seguras=casas_seguras,
                                    d_historico=historico)
            jogo.mover(p_cacador=cacador.posicao,
                       nova_posicao=nova_posicao)
        else:
            inferir(l_casas_percorridas=casas_percorridas,
                    d_historico=historico)
            nova_posicao = posicao_(l_casas_perigosas=casas_perigosa,
                                    l_casas_percorridas=casas_percorridas,
                                    l_casas_seguras=casas_seguras,
                                    d_historico=historico)
            jogo.mover(p_cacador=cacador.posicao,
                       nova_posicao=nova_posicao)


