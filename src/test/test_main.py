#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Memit - Teste
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/05/08
:Status: This is a "work in progress"
:Revision: 0.1.2
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
import unittest
from meme import Meme
from visual import Visual
#import peca

class _estMeme(unittest.TestCase):

    def setUp(self):
        class Gui(object):
            def __init__(self, *x):
                self.json = ''
                self.count =0

            def __getitem__(self, x):
                return self

            def __le__(self, x):
                return self

            def setAttribute(self, *x):
                self.opacity = 0.5

            def cling(self, *x):
                pass
            def g(self, *x, **y):
                return self
            def image(self, *x, **y):
                return self
            def text(self, *x, **y):
                return self
            def ellipse(self, *x, **y):
                return self
            def rect(self, *x, **y):
                return self
            def set_interval(self, *x, **y):
                return self
            """
            def build_house(self, *x):
                return (self)
            def build_pieces(self, *x):
                return (self)
            def build_hand(self, *x):
                return (self)
            def build_board(self, *x):
                return (self)
            def build_markers(self, *x):
                return ((self,self),self)
            def build_cube(self, *x):
                return (self,self,self)
            def build_base(self, *x):
                return (self,self,self,self)
            """

            def send(self, operation, **x):
                self.count +=1
                self.json = x

        self.gui = Gui()
        self.gui.onclick = object()
        self.app = Meme(Visual(self.gui,self.gui,self.gui))
        self.gui = self.app.gui

    def _est_tabuleiro(self):
        "garante que tem casas no tabuleiro."
        self.app.build_tabuleiro(self.gui)
        t = self.app.board
        self.assertEqual(len(t), 27)
    def test_mao(self):
        "garante que tem pecas na mao."
        self.app.build_mao(self.gui)
        m = self.app.hand
        self.assertEqual(len(m.pecas), 9)
    def test_escolhe_peca(self):
        "peca sai da mao e vai para a base."
        self.app.build_base(self.gui)
        m = self.app.hand
        #: a peca inicia na mao
        p = m.pecas[0]
        self.assertEqual(p.local,m)
        #: a peca chosen vai para a casa
        p.chosen()
        self.assertTrue('pec' in self.gui.json, "em vez json: %s"%self.gui.json)
        self.assertEqual(self.gui.count,1,"chamado mais deuma vez %d"%self.gui.count)
        self.assertEqual(p.local,self.app.casa)
        self.assertEqual(len(m.pecas), 8)
    def test_nao_pode_escolher_outra_peca(self):
        "nao pode escolher outra peca, peca fica na mao."
        self.app.build_base(self.gui)
        #: a peca inicia na mao
        p = self.app.piece[0]
        #: a peca chosen vai para a casa
        p.chosen()
        #: uma segunda peca nao pode ser chosen
        q = self.app.piece[1]
        q.chosen()
        self.assertEqual(q.local,self.app.hand)
    def _pega_peca_e_escolhe_casa(self):
        "peca sai da base e vai para a casa."
        self.app.build_base(self.gui)
        self.m = self.app.hand
        self.t = self.app.board
        #: a peca inicia na mao
        self.p = self.m[0]
        #: a peca chosen vai para a casa
        self.p.chosen()
        #self.assertEqual(self.gui.count,1,"peca varias vezes:%d"%self.gui.count)
        self.gui._tick()
        self.c = self.t[0]
        self.c.chosen()

    def test_escolhe_casa(self):
        "peca vai para a casa"
        self._pega_peca_e_escolhe_casa()
        self.assertEquals(self.p.house, self.c)
        self.assertTrue(self.p in self.t.pecas)
        self.assertEquals(self.t.bomba, 0)

    def test_escolhe_casa_registra(self):
        "peca vai para a casa, regitra no banco e monta puzzle."
        self._pega_peca_e_escolhe_casa()
        self.assertTrue('cas' in self.gui.json, "em vez json: %s"%self.gui.json)
        self.assertEqual(self.gui.json['cas'], 0, "em vez cas: %s"%self.gui.json['cas'])
        self.assertEqual(self.gui.count,2,"casa varias vezes:%d"%self.gui.count)
        self.assertEquals(self.p.local,self.c)
        self.assertTrue(self.p in self.t.pecas)
        self.assertEquals(self.app.casa.peca,None)
        self.assertEquals(self.t.bomba, 0, "bomba nao mudou %d"%self.t.bomba)
        self.assertEquals(self.t.puzzle, 1, "puzzle nao mudou %d"%self.t.puzzle)
    def test_escolhe_peca_na_casa(self):
        "peca volta para a base quando chosen no tabuleiro."
        self.app.build_base(self.gui)
        m = self.app.hand
        t = self.app.board
        #: a peca inicia na mao
        p = m[0]
         #: a peca chosen vai para a casa
        p.chosen()
        c = t[0]
        c.chosen()
         #: a peca chosen volta para a casa
        p.chosen()
        self.assertEquals(p.local, self.app.casa)
        self.assertEquals(self.app.casa.peca,p)
        self.assertEquals(t.puzzle, 0, "puzzle nao zerou %d"%t.puzzle)
    def test_escolhe_casa_sem_peca_selecionada(self):
        "nada acontece, nenhuma peca pode ser movida para a casa."
        self.app.build_base(self.gui)
        m = self.app.hand
        t = self.app.board
        c = t.casas[0]
        c.chosen()
        self.assertEquals(c.peca,None)
    def test_verifica_combinacao_vencedora(self):
        "indica nas pecas e na casa base que houve uma combinacao vencedora."
        self.app.build_base(self.gui)
        pecas = self.app.piece
        casas = self.app.board[0:9]
        self.assertEquals(self.app.casa.peca,None)
        return
        #__ = [casa.recebe(peca) for casa, peca in zip(casas,pecas)]
        __ = [peca.chosen() or casa.chosen() for casa, peca in zip(casas,pecas)]
        print(self.app.casa)
        [self.gui._tick() for t in range(10)]
        self.assertEquals(self.app.casa._estado_corrente,self.app.casa._casa_morta)
        self.assertEquals(self.app.casa.peca,None)
    def test_verifica_mudanca_fase(self):
        "rearruma as pecas na mao"
        self.app.build_base(self.gui)
        pecas = [p for p in self.app.piece]
        casas = self.app.board[0:9]
        self.t = self.app.board
        #__ = [casa.recebe(peca) for casa, peca in zip(casas,pecas)]
        __ = [peca.chosen() or casa.chosen() for casa, peca in zip(casas,pecas)]
        [self.gui._tick() for t in range(10)]
        self.assertEquals(self.app.fase, 1, "fase nao mudou : %d"%self.app.fase)
        self.assertEqual(self.gui.count,19,"casa varias vezes:%d"%self.gui.count)
        self.assertEquals(self.app.casa.peca,None)
        self.assertTrue('fas' in self.gui.json)
        self.assertEquals(self.gui.json['pcs'] ,range(9), "not %s"%self.gui.json['pcs'])
        [self.assertEquals(p.local,c) for p, c in zip(pecas,casas)]
        self.assertEquals(self.t.bomba, 0)
        self.assertEquals(self.t.puzzle, 0)

    def test_jogada_apos_mudanca_fase(self):
        "joga o inicio da proxima fase"
        self.app.build_base(self.gui)
        pecas = [p for p in self.app.piece]
        casas = self.app.board[0:9]
        self.t = self.app.board
        #__ = [casa.recebe(peca) for casa, peca in zip(casas,pecas)]
        __ = [peca.chosen() or casa.chosen() for casa, peca in zip(casas,pecas)]
        [self.gui._tick() for tempo in range(88)]
        self.assertEqual(self.t.pingo, 8)
        self.assertEquals(self.t.bomba, 7)
        self._pega_peca_e_escolhe_casa()
        self.assertEquals(self.t.puzzle, 1)
        self.assertEquals(self.p.local, self.c)
        self.assertTrue(self.p in self.t.pecas)

    def test_verifica_fim_de_jogo(self):
        "terminou todas as fases"
        self.app.build_base(self.gui)
        pecas = [p for p in self.app.piece]
        casas = self.app.board[0:9]
        self.t = self.app.board
        for i in range(5):
            __ = [peca.chosen() or casa.chosen() for casa, peca in zip(casas,pecas)]
            self.assertEquals(self.t.puzzle, 9)
            [self.gui._tick() for t in range(10)]
        self.assertEquals(self.t.puzzle, 9)
        self.assertEquals(self.app.fase, 5, "fase nao mudou : %d"%self.app.fase)
        [self.gui._tick() for t in range(100)]
        self.assertEquals(self.app.casa.peca,None)
        self.assertTrue('fim' in self.gui.json, "no end in %s"%self.gui.json)
        self.assertEquals(self.t.bomba, 0)




if __name__ == '__main__':
    unittest.main()