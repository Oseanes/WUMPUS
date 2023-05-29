import numpy as np
from ouro import Ouro
from wumpus import Wumpus
from buraco import Buraco
from vazio import Vazio
from cacador import Cacador


class Ambiente:
    """ Cria objeto ambiente"""
    def __init__(self, tamanho):
        self.tamanho_matrix = tamanho
        self.matriz = self.posicionar_na_matriz(quant_wumpus=1, quant_ouro=1, quant_buraco=3)
        self.casa_anterior = (0, 0)
        self.jogo_on = True

    def posicionar_na_matriz(self, quant_wumpus, quant_ouro, quant_buraco):
        """ Posiciona os agentes na Matriz"""
        # posições na matriz a serem preenchidas com os agentes.
        lista_posicao = set()
        while len(lista_posicao) < (self.tamanho_matrix * 2):
            posicao = (np.random.randint(self.tamanho_matrix), np.random.randint(self.tamanho_matrix))
            if posicao != (0, 0):
                lista_posicao.add(posicao)

        # Cria a matriz e a preenche toda com objetos Vazio
        matriz = np.full([self.tamanho_matrix, self.tamanho_matrix], Vazio)
        for i in range(self.tamanho_matrix):
            for j in range(self.tamanho_matrix):
                matriz[(i, j)] = Vazio()

        # posiciona o wumpus na matriz
        for i in range(quant_wumpus):
            posicao_wumpus = list(lista_posicao)[i]
            matriz[posicao_wumpus] = Wumpus()
            lista_posicao.remove(posicao_wumpus)

        for i in range(quant_ouro):
            posicao_ouro = list(lista_posicao)[i]
            matriz[posicao_ouro] = Ouro()
            lista_posicao.remove(posicao_ouro)

        for i in range(quant_buraco):
            posicao_buraco = list(lista_posicao)[i]
            matriz[posicao_buraco] = Buraco()
            lista_posicao.remove(posicao_buraco)

        matriz[(0, 0)] = Cacador()
        return matriz

    def mover(self, p_cacador, nova_posicao):
        if nova_posicao:
            self.casa_anterior = p_cacador
            objeto = self.matriz[nova_posicao]
            cacador = self.matriz[p_cacador]
            cacador.passos += 1
            # verifica se o caçador morre
            if objeto.sensacao == 'brisa' or objeto.sensacao == 'fedor':
                cacador.vivo = False
            elif objeto.sensacao == 'brilho':
                cacador.pontuacao += 50
                cacador.ouro_coletado = True

            self.matriz[nova_posicao] = cacador
            cacador.nova_posicao(nova_posicao)
            cacador.casas_percorridas.add(nova_posicao)
            self.matriz[p_cacador] = Vazio()

    def remover_wumpus(self, posicao):
        if posicao:
            self.matriz[posicao] = Vazio()

    def print_matrix(self):
        nova_matrix = np.full((self.tamanho_matrix, self.tamanho_matrix), 'xxxx')
        for i in range(self.tamanho_matrix):
            for j in range(self.tamanho_matrix):
                obj = self.matriz[i, j]
                nova_matrix[i, j] = obj.sensacao
        return nova_matrix
