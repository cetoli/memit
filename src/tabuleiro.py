"""
############################################################
Memit - Tabuleiro
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/06/05
:Status: This is a "work in progress"
:Revision: 0.1.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
from casa import Casa
PINGOS, SEGUNDO = 10, 10

class Tabuleiro:
    """Campo do jogo onde se joga as pecas"""
    def __init__(self, gui, local):
        self.gui, self.local = gui, local
        self.puzzle = 0
        self.build(gui)
        self.inicia()

    def finaliza(self):
        self.bomba = self.tempo = self.pingo = 0
        self.ativa = lambda *s : None
        self.gui.setAttribute("drops","visibility","hidden")
    def inicia(self, fase = 0):
        def avanca_bomba(s = self):
            #print (self.bomba)
            s.bomba += 1
        
        self.pecas = []
        self.bomba = self.tempo = self.pingo = 0
        self.avanca_puzzle(-self.puzzle)
        self.ativa = avanca_bomba 
    def build(self, gui):
        " Constroi uma colecao de dezesseis casas"
        self.casas = [Casa(gui, self, i).build() for i in range(27)]
    @property
    def casa(self):
        "retorna a casa da base"
        return self.local.casa
    def venceu(self):
        "trava a casa de selecao colocando ela no estado morta."
        print('venceu tabuleiro',self.local.casa)
        #self.local.casa.morta()
        self.local.avanca_fase()
    def pinga(self):
        "faz a gazolina pingar"
        self.pingo += 1
        self.pingo %= PINGOS
        self.gui.cling('drop%d'%self.pingo, 'drops')
    def temporiza(self):
        "rebe sinal do temporizador"
        self.tempo += 1
        self.pinga()
        if self.tempo >= SEGUNDO:
            self.ativa()
            self.tempo = 0
        pass
    def remove(self, esta_peca, desta_casa):
        "desfaz vencedora se for o caso, retroage o puzzle"
        self.gui.setAttribute("jig%d"%self.puzzle,"visibility","hidden")
        self.puzzle -= 1
        self.gui.setAttribute("jig%d"%self.puzzle,"visibility","visible")
        self.ativa = self.pinga
    def avanca_puzzle(self, passo = 1):
        """coloca proxima peca no puzzle"""
        self.gui.setAttribute("jig%d"%self.puzzle,"visibility","hidden")
        self.puzzle += passo
        self.gui.setAttribute("jig%d"%self.puzzle,"visibility","visible")
    def recebe(self, esta_peca, nesta_casa):
        "verifica se esta peca e vencedora"
        #self.gui.send(pec=esta_peca.name, cas=nesta_casa)
        self.pecas.append(esta_peca)
        self.avanca_puzzle()
        if len(self.pecas) == 9:
            self.ativa = self.venceu
        return
