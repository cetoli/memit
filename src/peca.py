"""
############################################################
Quarto - peca
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/05/08
:Status: This is a "work in progress"
:Revision: 0.1.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
    
class Peca:
    """Peca do jogo"""
    def __init__(self, gui, local, name):
        "local onde nasce, o nome da peca"
        self.gui, self.local, self.name = gui, local, name
        self.casa = self.local.casa
        self._estado_peca = self._estado_pode_posicionar
        self.build(gui)
    def build(self,gui):
        """ Engaja o controlador do envento peca escolhida"""
        gui['p%d'%self.name].onclick = self.escolhida
    def _estado_pode_posicionar(self):
        "a peca escolhida move para a casa da base"
        self.casa.recebe(self)
    def _estado_nao_pode_posicionar(self):
        "a peca escolhida fica na casa onde ja esta posicionada"
        pass
    def escolhida(self, *ev):
        "a peca escolhida move para a casa da base"
        self.gui.send(str(dict(pec=self.name)))
        self._estado_peca()
    def move(self, casa):
        "a peca escolhida move para esta casa"
        self.local.sai(self)
        self.local = casa
        self.atualiza(casa)
        self._estado_peca = self._estado_nao_pode_posicionar
    def atualiza(self, casa):
        "move peca para a casa"
        self.gui['cell_%d'%casa.name] <= self.gui['p%d'%self.name]

