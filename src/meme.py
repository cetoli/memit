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
#from tabuleiro import Tabuleiro gui.build_hand()House
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
        board = gui.build_board()
        hand = gui.build_hand()
        pieces = gui.build_pieces()
        self.house = House(gui.build_house())
        self.board = [House(h, self.house, n) for n, h in enumerate(board)]
        self.hand =  [House(h, self.house, n) for n, h in enumerate(hand)]
        self.piece = [Piece(p, h, self.house, n) 
                       for n, (p, h) in enumerate(zip(pieces, self.hand))]
        #self.house <= self.piece[0]

    def build_tabuleiro(self,gui):
        """Constroi o tabuleiro onde as pecas sao jogadas."""
        #self.tabuleiro =Tabuleiro(gui,self)
        return gui.build_board()
    def build_mao(self,gui):
        """Constroi os dois espacos onde as pecas se iniciam."""
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


class Piece:
    """Peca do jogo
    chosen    receive  relocate
    ------>[P]----->[B]+------>[SP] +->
            +<---------+
    """
    def __init__(self, visual_piece, house, board, name):
        "local onde nasce, o nome da peca"
        self.piece, self.house, self.board = visual_piece, house, board
        self.name = name
        self.piece.onclick = self.chosen
        self.house.enter(self)

    def chosen(self, *ev):
        "a peca escolhida move para a casa da base"
        #self.gui.send(str(dict(pec=self.name)))
        print('peca ',self.name)
        self.board.receive(self)
        #self.house.leave()
    def relocate(self, house = None):
        "esta peca se move para a casa referida"
        #self.gui.send(str(dict(pec=self.name)))
        #(house or self.house.house) <= self.piece
        #self.house.leave()
        (house or self.house).enter(self)


class House:
    """Casa onde se coloca pecas"""
    def __init__(self, visual_house, board = None, name = 0):
        "local onde nasce, o nome da peca"
        self.house, self.board, self.name = visual_house, board or self, name
        self.piece = self
        self.house.onclick = self.chosen
        self._got_chosen = self._chosen
        self.relay = lambda x: None
        
    def _chosen(self):
        "a peca escolhida move para a casa da base"
        #self.gui.send(str(dict(cas=self.name)))
        print("_chosen:",self.name, self.house)
        self.board.relay(self)

    def chosen(self, *ev):
        "a peca escolhida move para a casa da base"
        self._got_chosen()

    def relocate(self, house = None):
        "a peca escolhida move para a casa da base"
        pass

    def _relay(self, house):
        "a peca escolhida move para a casa referida"
        self.relay = lambda x: None
        house.enter(self.piece)
        self.piece = self

    def leave(self):
        "a peca escolhida move para a casa referida"
        self._got_chosen = self._chosen
        self.piece = self
        print("leave:",self._got_chosen, self.piece.name)
       
    def enter(self, piece):
        "a peca escolhida move para esta casa"
        #self.gui.send(str(dict(pec=self.name)))
        self._got_chosen = lambda : None
        self._enter(piece)
        piece.house = self
    def receive(self, piece):
        "a peca escolhida move para a casa da base"
        #self.gui.send(str(dict(pec=self.name)))
        self.relay = self._relay
        self.piece.relocate()
        self._enter(piece)
    def _enter(self, piece):
        "a peca escolhida move fisicamente para ca e deiaxa a casa original"
        #self.gui.send(str(dict(pec=self.name)))
        #piece.house.leave()
        self.piece = piece
        self.house <= piece.piece
        
        
def main(doc, svg, time):
  print('Memit 0.1.0')
  gui = Visual(doc, svg, time)
  meme =  Meme(gui)
  meme.build_base(gui)

