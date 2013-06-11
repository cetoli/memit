"""
############################################################
Quarto - Casa
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
class Casa:
    """Casa onde se coloca pecas"""
    def __init__(self, gui, local, name):
        "local onde nasce, o nome da casa"
        class CasaVazia(object):
            """Estado que representa a casa vazia."""
            def recebe(s, peca):
                "esta casa recebe peca quando esta vazia"
                self.peca = peca
                self.peca.move(self)
                self.local.recebe(peca, self.name)
                self._estado_corrente = self._casa_cheia
            def recolhe(s, peca):
                "esta casa recolhe de volta a peca quando esta vazia"
                self.peca = peca
                self.peca.move(self)
                self.local.remove(peca, self.name)
                self._estado_corrente = self._casa_cheia
            def escolhida(s, *ev):
                "remove peca da base e poe aqui"
                self.local.casa.entrega(self)
            def entrega(s, casa):
                "vazia nao entrega a peca pedida"
                pass

        class CasaCheia(object):
            """Estado que representa a casa cheia."""
            def recebe(s, peca):
                "esta casa nao recebe peca quando esta cheia"
                pass
            def recolhe(s, peca):
                "esta casa nao recolhe peca quando esta cheia"
                pass
            def escolhida(s, *ev):
                "esta casa nao nao pode ser escolhida quando esta cheia"
                pass
            def entrega(s, casa):
                "entrega a peca pedida, que sai daqui"
                self._estado_corrente = self._casa_vazia
                casa.recebe(self.peca)
                #print('entregou daqui',self,self._estado_corrente)
        class CasaMorta(CasaCheia):
            """Estado que representa a casa cheia."""
            def entrega(s, casa):
                "morta, nao entrega a peca pedida."
                pass
        
        self.gui, self.local, self.name = gui, local, name
        self.peca = None
        self._estado_corrente = self._casa_vazia = CasaVazia()
        self._casa_cheia = CasaCheia()
        self._casa_morta = CasaMorta()
    def build(self):
        """associa o evento de escolha para o click do mouse"""
        self.gui['cell_%d'%self.name].onclick = self.escolhida
        return self
    def escolhida(self, *ev):
        "esta casa recebe peca quando esta vazia e nega quando cheia"
        self._estado_corrente.escolhida(self)
    def recebe(self, peca):
        "esta casa recebe peca quando esta vazia"
        self._estado_corrente.recebe(peca)
    def recolhe(self, peca):
        "esta casa recolhe peca quando esta vazia"
        self._estado_corrente.recolhe(peca)
    def entrega(self, casa):
        "entrega a peca pedida, que sai daqui"
        self._estado_corrente.entrega(casa)
    def sai(self, peca):
        "a peca escolhida sai daqui"
        self.peca = None
        self._estado_corrente = self._casa_vazia
        #print('saiu daqui',self,self._estado_corrente)
    def morta(self):
        "notifica a casa que ela esta morta"
        self._estado_corrente = self._casa_morta
        #print('venceu morta',self,self._estado_corrente)
    def venceu(self):
        "notifica a casa que ela e vencedora"
        #print('venceu',self.name)
        peca = self.gui['p%d'%self.peca.name]
        peca.setAttribute('transform', "translate(10,550)")