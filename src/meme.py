"""
############################################################
Memit - Principal
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/06/23
:Status: This is a "work in progress"
:Revision: 0.1.3
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
#from tabuleiro import Tabuleiro
#from mao import Mao
#from casa import Casa
from visual import Visual

class Meme:
    """Game base with board and pieces."""
    def __init__(self, gui):
        """Constroi a casa que indica a peca que foi selecionada. """
        self.gui = gui
        #self.casa = Casa(gui,self,99)
        self.fase = 0
        
    def build_base(self,gui):
        """Constroi as partes do Jogo. """
        self.build_tabuleiro(gui)
        self.build_mao(gui)
    def build_tabuleiro(self,gui):
        """Constroi o tabuleiro onde as pecas sao jogadas."""
        #self.tabuleiro =Tabuleiro(gui,self)
        gui.build_board()
    def build_mao(self,gui):
        """Constroi os dois espacos onde as pecas se iniciam."""
        gui.build_hand()
        #self.mao1 =Mao(gui,self,0)
        #self.pecas = [peca for peca in self.mao1.pecas]
    '''
    def avanca_fase(self):
        self.fase += 1
        self.gui.send("phase", fas = self.fase,
                pcs = [peca.local.name for peca in self.pecas])
        if self.fase >= 5:
            self.gui.send("end", fim = self.fase)
            return self.tabuleiro.finaliza()
        self.tabuleiro.inicia(self.fase)
        self.mao1.inicia(self.fase)
        
    def remove(self, esta_peca, desta_casa):
        "desfaz vencedora se for o caso, retroage o puzzle"
        self.tabuleiro.remove(esta_peca, desta_casa)
    def recebe(self, peca, casa):
        "notificacao inocua de recebimento da peca pela casa da base"
        pass
    '''

def main(doc, svg, time):
  print('Memit 0.1.0')
  gui = Visual(doc, svg, time)
  meme =  Meme(gui)
  meme.build_base(gui)

