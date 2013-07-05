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
        self.doc, self.puzzles, self.puzzle = gui.build_base()
        self.jig = 0
        cube = gui.build_cube(None,'memit/beleza.png', 'memit/conforto.png','memit/valor.png')
        markers = gui.build_markers()
        board = gui.build_board()
        hand = gui.build_hand()
        pieces = gui.build_pieces()
        sh = self.house = House(gui.build_house())
        self.board = [House(h, sh, n, self) for n, h in enumerate(board)]
        self.hand =  [House(h, sh, 100+n) for n, h in enumerate(hand)]
        self.piece = [Piece(p, h, sh, n)
                       for n, (p, h) in enumerate(zip(pieces, self.hand))]
        self.next_phase()

    def rehouse(self, step):
        """Constroi o tabuleiro onde as pecas sao jogadas."""
        self.doc <= self.puzzles[self.jig]
        self.gui.set_inc_value(0)
        if self.jig < 8 :
            self.jig += step
            self.puzzle <= self.puzzles[self.jig]
        else:
            self.gui.phaser = self.next_phase

    def next_phase(self, v = 0):
        self.fase += 1
        self.gui.phaser = lambda x = 0: None
        self.gui.set_inc_value(0, 1)
#        self.gui.send("phase", fas = self.fase,
#                pcs = [peca.local.name for peca in self.pecas])
        print(dict(fas= self.fase, pcs=[peca.house.name for peca in self.piece]))
        if self.fase >= 3:
            #self.gui.send("end", fim = self.fase)
            self.gui.set_inc_value(0, 0)
            [self.doc <= piece.piece for piece in self.piece]
            print(dict(fim= self.fase))
            return
        [house.enter(piece) for house, piece in zip(self.hand, self.piece)]
        [house.init() for house in self.board]
        self.jig = -1
        self.rehouse(1)


class Piece:
    """Peca do jogo
    chosen    relay(B)    receive(P,H)   relocate(H)    enter(P)   cling
    ------>[P]------->[SH]+---------->[B] +-------->[SP]------->[H]---->[P]
    """
    def __init__(self, visual_piece, house, board, name):
        "local onde nasce, o nome da peca"
        self.piece, self.house, self.board = visual_piece, house, board
        self.name = name
        self.piece.onclick = self.chosen
        self.house.enter(self)

    def chosen(self, *ev):
        "a peca escolhida move para a casa da base"
        self.house.relay(self.board)

    def relocate(self, house = None):
        "esta peca se move para a casa referida"
        (house or self.house).enter(self)

    def rehouse(self, house = None):
        "esta peca referencia a casa referida"
        self.house = house
    def cling(self, house):
        "esta peca se move visualmente para a casa referida"
        house <= self.piece


class House:
    """Casa onde se coloca pecas"""
    def __init__(self, visual_house, board = None, name = 99, game = None):
        "local onde nasce, o nome da peca"
        self.house, self.board, self.name = visual_house, board or self, name
        self.game = game or self
        self.house.onclick = self.chosen
        self.init()
    def init(self):
        "inicia uma peca falsa, habilita escolha e desabilita outra acoes"
        self.piece = self
        self._got_chosen = self._chosen
        self.rehouse = lambda x=0: None
        self.cling = self.relay = lambda x=0: None
    def _chosen(self):
        "a peca escolhida move para a casa da base"
        self.board.relay(self)
        self.piece.rehouse(self)

    def chosen(self, *ev):
        "a peca escolhida move para a casa da base"
        self._got_chosen()

    def relocate(self, house = None):
        "a peca escolhida referencia esta"
        house.piece = self
        pass

    def _relay(self, house):
        "a peca escolhida move para a casa referida"
        def _chosen(x=0):
            """usado para impedir que o click da casa ative imediatamente"""
            self._got_chosen = self._chosen
        self.game.rehouse(-1)
        self.relay = lambda x: None
        house.receive(self.piece, self)
        self._got_chosen = _chosen

    def enter(self, piece):
        "a peca escolhida move para esta casa"
        self._enter(piece)
        piece.house = self

    def receive(self, piece, house):
        "a peca escolhida move para a casa da base"
        #self.gui.send(str(dict(cas=self.name, pec=piece.name)))
        print(str(dict(cas=self.name, pec=piece.name)))
        self.piece.relocate(house)
        self._enter(piece)

    def _enter(self, piece):
        "a peca escolhida move fisicamente para ca e a casa fica ocupada"
        self.game.rehouse(+1)
        self._got_chosen = lambda : None
        self.relay = self._relay
        self.piece = piece
        piece.cling(self.house)


def main(doc, svg, time):
  print('Memit 0.1.0')
  gui = Visual(doc, svg, time)
  meme =  Meme(gui)
  meme.build_base(gui)

