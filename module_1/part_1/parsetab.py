
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGINTABLE CLOSEDATA CLOSEDIV CLOSEHEADER CLOSEHREF CLOSEROW CLOSESPAN CLOSESTYLE CLOSETABLE CONTENT FISH GARBAGE NOBR NOBR2 OPENDATA OPENDIV OPENHEADER OPENHREF OPENROW OPENSPAN OPENSTYLE OPENTABLE PEND PSTART SUPEND SUPSTART TABLECLOSER TABLEHEADER WASTEstart : tableskip : OPENHEADER content skip\n            | CLOSEHEADER content skip\n            | OPENDATA content skip\n            | temp content skip\n            | closerow content skip\n            | OPENROW content skip\n            | OPENHREF content skip\n            | CLOSEHREF content skip\n            | NOBR content skip\n            | NOBR2 content skip\n            | WASTE content skip\n            | content skip \n            | empty\n    skipper : OPENHEADER content skipper\n            | CLOSEHEADER content skipper\n            | OPENHREF content skipper\n            | CLOSEHREF content skipper\n            | NOBR content skipper\n            | NOBR2 content skipper\n            | WASTE content skipper\n            | content skipper \n            | empty\n    temp : CLOSEDATA       \n    closerow : CLOSEROW\n    skiptag : CONTENT skiptag\n               | OPENHEADER skiptag\n               | CLOSEHEADER skiptag\n               | WASTE skiptag\n               | NOBR skiptag\n               | NOBR2 skiptag\n               | OPENHREF skiptag\n               | CLOSEHREF skiptag\n               | emptyrow : OPENROW content data closerow content row\n            | empty\n    datapro  : OPENDATA CLOSEDATA\n                | OPENDATA skipper CLOSEDATA\n    data : datapro data\n            | content data\n            | empty\n    table : BEGINTABLE CONTENT TABLEHEADER skip TABLECLOSER CONTENT OPENTABLE content row CLOSETABLEempty :content : content CONTENT\n               | empty'
    
_lr_action_items = {'BEGINTABLE':([0,],[3,]),'$end':([1,2,54,],[0,-1,-42,]),'CONTENT':([3,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,49,50,52,55,56,58,59,60,62,64,66,67,68,69,70,71,72,73,74,75,76,77,79,80,81,82,83,84,],[4,-43,24,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,37,-44,24,-45,24,24,24,24,24,24,24,24,24,24,-43,24,-43,24,24,-43,-45,-43,-43,-37,-43,24,-43,-43,-43,-43,-43,-43,-45,24,-38,24,24,24,24,24,24,24,]),'TABLEHEADER':([4,],[5,]),'OPENHEADER':([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,60,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,84,],[8,8,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,-44,8,-45,8,8,8,8,8,8,8,8,8,8,66,-43,66,-43,-43,-43,-43,-43,-43,-45,66,66,66,66,66,66,66,]),'CLOSEHEADER':([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,60,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,84,],[9,9,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,-44,9,-45,9,9,9,9,9,9,9,9,9,9,68,-43,68,-43,-43,-43,-43,-43,-43,-45,68,68,68,68,68,68,68,]),'OPENDATA':([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,52,55,56,58,59,64,76,],[10,10,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,-44,10,-45,10,10,10,10,10,10,10,10,10,10,-43,60,60,60,-45,-37,-38,]),'OPENROW':([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,49,50,62,75,],[13,13,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,-44,13,-45,13,13,13,13,13,13,13,13,13,13,-43,52,-43,52,]),'OPENHREF':([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,60,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,84,],[14,14,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,-44,14,-45,14,14,14,14,14,14,14,14,14,14,69,-43,69,-43,-43,-43,-43,-43,-43,-45,69,69,69,69,69,69,69,]),'CLOSEHREF':([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,60,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,84,],[15,15,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,-44,15,-45,15,15,15,15,15,15,15,15,15,15,70,-43,70,-43,-43,-43,-43,-43,-43,-45,70,70,70,70,70,70,70,]),'NOBR':([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,60,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,84,],[16,16,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,-44,16,-45,16,16,16,16,16,16,16,16,16,16,71,-43,71,-43,-43,-43,-43,-43,-43,-45,71,71,71,71,71,71,71,]),'NOBR2':([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,60,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,84,],[17,17,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,-44,17,-45,17,17,17,17,17,17,17,17,17,17,72,-43,72,-43,-43,-43,-43,-43,-43,-45,72,72,72,72,72,72,72,]),'WASTE':([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,60,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,84,],[18,18,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,-44,18,-45,18,18,18,18,18,18,18,18,18,18,73,-43,73,-43,-43,-43,-43,-43,-43,-45,73,73,73,73,73,73,73,]),'CLOSEDATA':([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,60,65,66,67,68,69,70,71,72,73,74,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,],[20,20,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,-44,20,-45,20,20,20,20,20,20,20,20,20,20,64,76,-43,-43,-43,-43,-43,-43,-43,-43,-23,-43,-22,-43,-43,-43,-43,-43,-43,-15,-16,-17,-18,-19,-20,-21,]),'CLOSEROW':([5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,52,55,56,57,58,59,61,63,64,76,],[21,21,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-45,-24,-25,-44,21,-45,21,21,21,21,21,21,21,21,21,21,-43,-43,-43,21,-43,-41,-40,-39,-37,-38,]),'TABLECLOSER':([5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,48,],[-43,22,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-14,-24,-25,-13,-44,-43,-45,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,]),'CLOSETABLE':([21,24,26,49,50,51,53,62,75,85,],[-25,-44,-45,-43,-43,54,-36,-43,-43,-35,]),'OPENTABLE':([37,],[49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'table':([0,],[2,]),'skip':([5,7,25,27,28,29,30,31,32,33,34,35,36,],[6,23,38,39,40,41,42,43,44,45,46,47,48,]),'content':([5,7,8,9,10,11,12,13,14,15,16,17,18,25,27,28,29,30,31,32,33,34,35,36,49,52,55,56,58,60,62,66,67,68,69,70,71,72,73,77,79,80,81,82,83,84,],[7,7,25,27,28,29,30,31,32,33,34,35,36,7,7,7,7,7,7,7,7,7,7,7,50,55,56,56,56,67,75,77,67,79,80,81,82,83,84,67,67,67,67,67,67,67,]),'temp':([5,7,25,27,28,29,30,31,32,33,34,35,36,],[11,11,11,11,11,11,11,11,11,11,11,11,11,]),'closerow':([5,7,25,27,28,29,30,31,32,33,34,35,36,57,],[12,12,12,12,12,12,12,12,12,12,12,12,12,62,]),'empty':([5,7,8,9,10,11,12,13,14,15,16,17,18,25,27,28,29,30,31,32,33,34,35,36,49,50,52,55,56,58,60,62,66,67,68,69,70,71,72,73,75,77,79,80,81,82,83,84,],[19,19,26,26,26,26,26,26,26,26,26,26,26,19,19,19,19,19,19,19,19,19,19,19,26,53,26,59,59,59,74,26,26,74,26,26,26,26,26,26,53,74,74,74,74,74,74,74,]),'row':([50,75,],[51,85,]),'data':([55,56,58,],[57,61,63,]),'datapro':([55,56,58,],[58,58,58,]),'skipper':([60,67,77,79,80,81,82,83,84,],[65,78,86,87,88,89,90,91,92,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> table','start',1,'p_start','Task1.py',98),
  ('skip -> OPENHEADER content skip','skip',3,'p_skip','Task1.py',100),
  ('skip -> CLOSEHEADER content skip','skip',3,'p_skip','Task1.py',101),
  ('skip -> OPENDATA content skip','skip',3,'p_skip','Task1.py',102),
  ('skip -> temp content skip','skip',3,'p_skip','Task1.py',103),
  ('skip -> closerow content skip','skip',3,'p_skip','Task1.py',104),
  ('skip -> OPENROW content skip','skip',3,'p_skip','Task1.py',105),
  ('skip -> OPENHREF content skip','skip',3,'p_skip','Task1.py',106),
  ('skip -> CLOSEHREF content skip','skip',3,'p_skip','Task1.py',107),
  ('skip -> NOBR content skip','skip',3,'p_skip','Task1.py',108),
  ('skip -> NOBR2 content skip','skip',3,'p_skip','Task1.py',109),
  ('skip -> WASTE content skip','skip',3,'p_skip','Task1.py',110),
  ('skip -> content skip','skip',2,'p_skip','Task1.py',111),
  ('skip -> empty','skip',1,'p_skip','Task1.py',112),
  ('skipper -> OPENHEADER content skipper','skipper',3,'p_skipper','Task1.py',115),
  ('skipper -> CLOSEHEADER content skipper','skipper',3,'p_skipper','Task1.py',116),
  ('skipper -> OPENHREF content skipper','skipper',3,'p_skipper','Task1.py',117),
  ('skipper -> CLOSEHREF content skipper','skipper',3,'p_skipper','Task1.py',118),
  ('skipper -> NOBR content skipper','skipper',3,'p_skipper','Task1.py',119),
  ('skipper -> NOBR2 content skipper','skipper',3,'p_skipper','Task1.py',120),
  ('skipper -> WASTE content skipper','skipper',3,'p_skipper','Task1.py',121),
  ('skipper -> content skipper','skipper',2,'p_skipper','Task1.py',122),
  ('skipper -> empty','skipper',1,'p_skipper','Task1.py',123),
  ('temp -> CLOSEDATA','temp',1,'p_temp','Task1.py',126),
  ('closerow -> CLOSEROW','closerow',1,'p_closerow','Task1.py',130),
  ('skiptag -> CONTENT skiptag','skiptag',2,'p_skiptag','Task1.py',134),
  ('skiptag -> OPENHEADER skiptag','skiptag',2,'p_skiptag','Task1.py',135),
  ('skiptag -> CLOSEHEADER skiptag','skiptag',2,'p_skiptag','Task1.py',136),
  ('skiptag -> WASTE skiptag','skiptag',2,'p_skiptag','Task1.py',137),
  ('skiptag -> NOBR skiptag','skiptag',2,'p_skiptag','Task1.py',138),
  ('skiptag -> NOBR2 skiptag','skiptag',2,'p_skiptag','Task1.py',139),
  ('skiptag -> OPENHREF skiptag','skiptag',2,'p_skiptag','Task1.py',140),
  ('skiptag -> CLOSEHREF skiptag','skiptag',2,'p_skiptag','Task1.py',141),
  ('skiptag -> empty','skiptag',1,'p_skiptag','Task1.py',142),
  ('row -> OPENROW content data closerow content row','row',6,'p_row','Task1.py',144),
  ('row -> empty','row',1,'p_row','Task1.py',145),
  ('datapro -> OPENDATA CLOSEDATA','datapro',2,'p_datapro','Task1.py',148),
  ('datapro -> OPENDATA skipper CLOSEDATA','datapro',3,'p_datapro','Task1.py',149),
  ('data -> datapro data','data',2,'p_data','Task1.py',154),
  ('data -> content data','data',2,'p_data','Task1.py',155),
  ('data -> empty','data',1,'p_data','Task1.py',156),
  ('table -> BEGINTABLE CONTENT TABLEHEADER skip TABLECLOSER CONTENT OPENTABLE content row CLOSETABLE','table',10,'p_table','Task1.py',159),
  ('empty -> <empty>','empty',0,'p_empty','Task1.py',163),
  ('content -> content CONTENT','content',2,'p_content','Task1.py',175),
  ('content -> empty','content',1,'p_content','Task1.py',176),
]
