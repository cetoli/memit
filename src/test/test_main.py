#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Memit - Serious Game in cavalier projection for memetics
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2013/03/17  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.1 $
:Home: `Labase http://labase.selfip.org/`__
:Copyright: 2011, `GPL http://is.gd/3Udt`__. 
"""
__author__  = "Carlo E. T. Oliveira (carlo@nce.ufrj.br) $Author: carlo $"
__version__ = "0.1 $Revision$"[10:-1]
__date__    = "2013/03/17 $Date$"

        
import mocker
from mocker import Mocker,KWARGS, ARGS, ANY, CONTAINS, MATCH, expect
#from kwarwp import Place,Way,Border,Door,Tar,Trunk
from memit import main

class TestMain(mocker.MockerTestCase):
  """Testes unitários para o Pyjamas"""
  def __list(self):
        #INVENTORY = {'.':Way, ' ': Border, '&':Door, '@':Tar, '%':Border}
        ES =FS = self.mg       
        INVENTORY = {'.':[Way,ES,None], ' ': [Border,ES,None], '&':[Door,ES,None]
            , '@':[Tar,FS,'piche.gif'], '$':[Trunk,FS,'tronco.gif']}
        return INVENTORY

  def setUp(self):
    self.mock_gui = Mocker()
    self.mock_avt = Mocker()
    self.mg = self.mock_gui.mock()
    self.ma = self.mock_gui.mock()

  def tearDown(self):
    self.mock_gui.restore()
    self.mock_avt.restore()
    self.mock_avt.verify()
    self.mock_avt = None
    self.app = None
    pass

  def _expect_all_place(self):
    "place expectations"
    expect(self.mg.request(ARGS)).result(self.ma)
    #expect(self.mg.handler(ARGS)).count(1,7)
    #expect(self.mg.image(ARGS,KWARGS)).count(1)
    #expect(self.mg.rect(ARGS,KWARGS)).count(1,2).result(self.mg)
    #expect(self.mg.dialog(ARGS,KWARGS)).count(1,2).result(self.mg)
    #expect(self.mg.hide()).count(0,2).result(self.mg)
    #expect(self.mg.text(ARGS,KWARGS)).result(self.mg).count(1,6)
    #expect(self.ma.move(ARGS))
    #expect(self.mg.textarea(ARGS))
    #expect(self.mg(ARGS)).count(1,96).result(self.ma)
    ##expect(self.mg.textContent = ANY).count(0,6)
  def _replay_and_create_place(self,p = '.&.'):
    "create place"
    self.mock_gui.replay()
    #main(doc, doc['panel'], GUI(doc['panel'],doc['data']), '/studio/memit/%s')

    self.app = main(self.mg, self.mg, self.mg, '/studio/memit/%s')
    #self.app.talk = lambda a : None
    #self.talk = self.mock_gui.patch(self.app.talk)
    print('---- NOW OPERATIONS ----')
  def test_create_board(self):
    "create board"
    self._expect_all_place()
    self._replay_and_create_place()
  def test_load_figures(self):
    "load figures"
    self._expect_all_place()
    expect(self.mg.request(ARGS)).result(self.ma)
    self._replay_and_create_place()
    class Response:
      text =str(dict(status=0,result=['%s%02d_%02d.png'%(name,kind,piece)
        for name in 'piece jigs puzzle'.split()
        for piece in range(9) for kind in [0,1]]))
    self.app._load_figures(Response)
    assert 'piece00_00.png' in str(self.app.piece_imgs), 'self.app.pieces %s'%self.app.piece_imgs
    assert 'puzzle00_00.png' in str(self.app.puzzle_imgs), 'self.app.puzzle_imgs %s'%self.app.puzzle_imgs
    assert 'jigs00_00.png' in str(self.app.jig_imgs), 'self.app.jig_imgs %s'%self.app.jig_imgs
  def test_load_scenes(self):
    "load scenes"
    self._expect_all_place()
    expect(self.mg.request(ARGS))
    expect(self.mg.group(KWARGS)).count(1,3).result(self.ma)
    expect(self.mg.ellipse(KWARGS)).count(1,3).result(self.ma)
    expect(self.ma.setAttribute(ARGS)).count(1,3)
    expect(self.mg.clear()).count(1,2)
    expect(self.mg.set(ARGS)).count(1,3)
    expect(self.mg.image(KWARGS)).count(1,9).result(self.ma)
    expect(self.mg.text(ARGS,KWARGS)).count(1,9).result(self.ma)
    expect(self.ma.addEventListener(ARGS)).count(1,80)
    [expect(self.mg.text(ind,KWARGS)).result(self.ma).count(7) for ind in range(9)]
    #---IMAGES---
    expect(self.mg.image(KWARGS)).count(1,9).result(self.ma)
    #---PHASES---
    expect(self.mg.group(KWARGS)).count(1,3).result(self.ma)
    expect(self.mg.image(KWARGS)).count(1,9).result(self.ma)#jigs
    expect(self.mg.image(KWARGS)).count(1,9).result(self.ma)#jigs
    #---FACES---
    expect(self.mg.image(KWARGS)).count(1,3).result(self.ma)#jigs
    expect(self.mg.clear()).count(1,21)
    expect(self.mg.image(KWARGS)).count(1,80).result(self.ma)#jigs
    expect(self.mg.set(ARGS)).count(1,21)
    expect(self.mg.group(KWARGS)).count(1,31).result(self.ma)
    #---MARKERS---
    expect(self.mg.rect(KWARGS)).count(1,3*9).result(self.ma)#jigs
    expect(self.ma.addEventListener(ARGS)).count(1,81)
    #---START---
    expect(self.ma.setAttribute(ARGS)).count(1,3)
    expect(self.ma.setAttribute(ARGS)).count(1,5*9)
    self._replay_and_create_place()
    class Response:
      text =str(dict(status=0,result=['%s%02d_%02d.png'%(name,kind,piece)
        for name in 'piece jigs puzzle'.split()
        for piece in range(9) for kind in [0,1]]))
    self.app._load_figures(Response)
    assert 'puzzle00_00.png' in str(self.app.puzzle_imgs), 'self.app.puzzle_imgs %s'%self.app.puzzle_imgs
    Response.text =str(dict(status=0,result=['%s%02d_%02d.png'%(name,kind,piece)
        for name in 'face back'.split()
        for piece in range(3) for kind in range(7)]))
    self.app._load_scenes(Response)
    assert len(self.app.pieces[0]) == 9, 'self.app.pieces %s'%self.app.pieces

if __name__ == '__main__':
    import unittest
    unittest.main()