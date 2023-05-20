class Cacador:

    def __init__(self):
        self.posicao = (0, 0)
        self.posicao_anterior = None
        self.sensacao = 'cacador'
        self.flecha = True
        self.pontuacao = 0
        self.casa_com_buraco = set()
        self.casas_percorridas = set()
        self.vivo = True
        self.ouro_coletado = False
        self.wumpus_morto = False

    def nova_posicao(self, p_cacador):
        self.posicao = p_cacador

    def norte(self, tamanho_matrix):
        """Retorna as novas coordenadas referente a mover ao norte."""
        posicao = self.posicao
        if tamanho_matrix > posicao[0] + 1:
            nova_posicao = (posicao[0] + 1, posicao[1])
            return nova_posicao
        else:
            return None

    def sul(self):
        """Retorna as novas coordenadas referente a mover ao sul."""
        posicao = self.posicao
        posicao = list(posicao)
        if 0 <= posicao[0] - 1:
            nova_posicao = (posicao[0] - 1, posicao[1])
            return nova_posicao
        else:
            return None

    def leste(self, tamanho_matrix):
        """Retorna as novas coordenadas referente a mover ao leste."""
        posicao = self.posicao
        posicao = list(posicao)
        if tamanho_matrix > posicao[1] + 1:
            nova_posicao = (posicao[0], posicao[1] + 1)
            return nova_posicao
        else:
            return None

    def oeste(self):
        """Retorna as novas coordenadas referente a mover ao oeste."""
        posicao = self.posicao
        posicao = list(posicao)
        if 0 <= self.posicao[1] - 1:
            nova_posicao = (posicao[0], posicao[1] - 1)
            return nova_posicao
        else:
            return None

    def posicao_adjacente(self, tamanho_matrix):
        """Retorna uma lista das casas adjacentes a do caçador.
         tamanho_matrix --> parametro necessário para acessar apenas posições
         existente na matriz."""
        posicao = [self.norte(tamanho_matrix), self.sul(),
                   self.leste(tamanho_matrix), self.oeste()]
        # Remover False referente a verificação "Bateu na parede".
        posicao = filter(None, posicao)
        return list(posicao)
