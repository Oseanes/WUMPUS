import numpy as np


class Agente:
    """ Cria objeto com todos os agentes e fornece os métodos."""

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz = np.zeros((self.tamanho, self.tamanho), dtype=np.int64)
        self.posicoes_agentes = self.gerar_posicao_agentes()
        self.posicao_cacador = self.cacador((0, 0))
        self.quant_wumpus = 0
        self.quant_ouro = 0
        self.quant_buraco = 0
        self.flecha = True

    def wumpus(self):
        """ Posiciona o WUMPUS na matrix"""
        w = int(self.tamanho / 2) - 1  # quantidade de wumpus
        self.quant_wumpus = w
        for i in range(w):
            p_wumpus = self.posicoes_agentes[i]
            self.matriz[p_wumpus] = 2
            self.posicoes_agentes.remove(p_wumpus)

    def ouro(self):
        """ Posiciona o OURO na matrix"""
        o = int(self.tamanho / 2) - 1  # quantidade de ouro
        self.quant_ouro = o
        for i in range(o):
            p_ouro = self.posicoes_agentes[i]
            self.matriz[p_ouro] = 3
            self.posicoes_agentes.remove(p_ouro)

    def buraco(self):
        """ Posiciona o POÇO na matrix"""
        b = self.tamanho - 1  # quantidade de poço
        self.quant_buraco = b
        for i in range(b):
            p_buraco = self.posicoes_agentes[i]
            self.matriz[p_buraco] = 4
            self.posicoes_agentes.remove(p_buraco)

    def cacador(self, p_cacador):
        self.matriz[p_cacador] = 1
        return p_cacador

    def gerar_posicao_agentes(self):
        # posições na matriz a serem preenchidas com os agentes.
        l_posicao = set()

        while len(l_posicao) < (self.tamanho * 2):
            posicao = (np.random.randint(self.tamanho), np.random.randint(self.tamanho))
            if posicao != (0, 0):
                l_posicao.add(posicao)

        return list(l_posicao)

    def norte(self, p_cacador):
        """Retorna as novas coordenadas referente a mover ao norte."""
        if self.tamanho > p_cacador[0] + 1:
            nova_posicao = (p_cacador[0] + 1, p_cacador[1])
            return nova_posicao
        else:
            return False

    def sul(self, p_cacador):
        """Retorna as novas coordenadas referente a mover ao sul."""
        if 0 <= p_cacador[0] - 1:
            nova_posicao = (p_cacador[0] - 1, p_cacador[1])
            return nova_posicao
        else:
            return False

    def leste(self, p_cacador):
        """Retorna as novas coordenadas referente a mover ao leste."""
        if self.tamanho > p_cacador[1] + 1:
            nova_posicao = (p_cacador[0], p_cacador[1] + 1)
            return nova_posicao
        else:
            return False

    def oeste(self, p_cacador):
        """Retorna as novas coordenadas referente a mover ao oeste."""
        if 0 <= p_cacador[1] - 1:
            nova_posicao = (p_cacador[0], p_cacador[1] - 1)
            return nova_posicao
        else:
            return False

    def mover(self, p_cacador, nova_posicao):
        if nova_posicao:
            self.matriz[p_cacador] = 0
            self.matriz[nova_posicao] = 1
            self.posicao_cacador = nova_posicao
            #return nova_posicao

    def percepcao_ambiente(self):
        """Retorna as Percepções que o caçador obtém do ambiente. """
        posicao_percepacao = [self.norte(self.posicao_cacador), self.sul(self.posicao_cacador),
                              self.leste(self.posicao_cacador), self.oeste(self.posicao_cacador)]

        percepcao = []
        for i in posicao_percepacao:
            if self.matriz[i] != 0 and i is not False:
                percepcao.append(self.matriz[i])

        return percepcao

    def atirar_norte(self):
        """Atirar flecha para o norte."""
        return self.norte(self.posicao_cacador)

    def atirar_sul(self):
        """ Atirar flecha para o Sul."""
        return self.sul(self.posicao_cacador)

    def atirar_leste(self):
        """Atirar para o Leste."""
        return self.leste(self.posicao_cacador)

    def atirar_oeste(self):
        """Atirar para o Oeste."""
        return self.oeste(self.posicao_cacador)
