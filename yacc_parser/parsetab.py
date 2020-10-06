
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA CORKSCREW DOT ID LITERAL L_PAREN NUMBER R_PAREN SEMICOLprog : definitionsprog : definitions : definition definitions\n                   | definitiondefinition : head DOT\n                  | head CORKSCREW body DOThead : atomatom : atom_head\n            | atom_head atom_argsatom_head : IDatom_args : atom_arg atom_args\n                | atom_argatom_arg : ID\n               | L_PAREN subatom R_PARENsubatom : atom\n               | L_PAREN subatom R_PARENbody : expressionexpression : term SEMICOL expression\n                  | termterm : factor COMMA term\n            | factorfactor : L_PAREN expression R_PAREN\n              | atom'
    
_lr_action_items = {'$end':([0,1,2,3,8,9,25,],[-2,0,-1,-4,-3,-5,-6,]),'ID':([0,3,6,7,9,10,12,13,14,19,22,25,26,27,30,],[7,7,13,-10,-5,7,13,-13,7,7,7,-6,7,7,-14,]),'DOT':([4,5,6,7,11,12,13,15,16,17,18,20,21,30,31,32,33,],[9,-7,-8,-10,-9,-12,-13,25,-17,-19,-21,-23,-11,-14,-18,-20,-22,]),'CORKSCREW':([4,5,6,7,11,12,13,21,30,],[10,-7,-8,-10,-9,-12,-13,-11,-14,]),'COMMA':([6,7,11,12,13,18,20,21,30,33,],[-8,-10,-9,-12,-13,27,-23,-11,-14,-22,]),'SEMICOL':([6,7,11,12,13,17,18,20,21,30,32,33,],[-8,-10,-9,-12,-13,26,-21,-23,-11,-14,-20,-22,]),'R_PAREN':([6,7,11,12,13,17,18,20,21,23,24,28,29,30,31,32,33,34,],[-8,-10,-9,-12,-13,-19,-21,-23,-11,30,-15,33,34,-14,-18,-20,-22,-16,]),'L_PAREN':([6,7,10,12,13,14,19,22,26,27,30,],[14,-10,19,14,-13,22,19,22,19,19,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'definitions':([0,3,],[2,8,]),'definition':([0,3,],[3,3,]),'head':([0,3,],[4,4,]),'atom':([0,3,10,14,19,22,26,27,],[5,5,20,24,20,24,20,20,]),'atom_head':([0,3,10,14,19,22,26,27,],[6,6,6,6,6,6,6,6,]),'atom_args':([6,12,],[11,21,]),'atom_arg':([6,12,],[12,12,]),'body':([10,],[15,]),'expression':([10,19,26,],[16,28,31,]),'term':([10,19,26,27,],[17,17,17,32,]),'factor':([10,19,26,27,],[18,18,18,18,]),'subatom':([14,22,],[23,29,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> definitions','prog',1,'p_prog','parser.py',9),
  ('prog -> <empty>','prog',0,'p_prog_empty','parser.py',14),
  ('definitions -> definition definitions','definitions',2,'p_definitions','parser.py',19),
  ('definitions -> definition','definitions',1,'p_definitions','parser.py',20),
  ('definition -> head DOT','definition',2,'p_definition','parser.py',28),
  ('definition -> head CORKSCREW body DOT','definition',4,'p_definition','parser.py',29),
  ('head -> atom','head',1,'p_head','parser.py',37),
  ('atom -> atom_head','atom',1,'p_atom','parser.py',42),
  ('atom -> atom_head atom_args','atom',2,'p_atom','parser.py',43),
  ('atom_head -> ID','atom_head',1,'p_atom_head','parser.py',51),
  ('atom_args -> atom_arg atom_args','atom_args',2,'p_atom_args','parser.py',56),
  ('atom_args -> atom_arg','atom_args',1,'p_atom_args','parser.py',57),
  ('atom_arg -> ID','atom_arg',1,'p_atom_arg','parser.py',65),
  ('atom_arg -> L_PAREN subatom R_PAREN','atom_arg',3,'p_atom_arg','parser.py',66),
  ('subatom -> atom','subatom',1,'p_subatom','parser.py',73),
  ('subatom -> L_PAREN subatom R_PAREN','subatom',3,'p_subatom','parser.py',74),
  ('body -> expression','body',1,'p_body','parser.py',82),
  ('expression -> term SEMICOL expression','expression',3,'p_expression','parser.py',94),
  ('expression -> term','expression',1,'p_expression','parser.py',95),
  ('term -> factor COMMA term','term',3,'p_term','parser.py',100),
  ('term -> factor','term',1,'p_term','parser.py',101),
  ('factor -> L_PAREN expression R_PAREN','factor',3,'p_factor','parser.py',106),
  ('factor -> atom','factor',1,'p_factor','parser.py',107),
]
