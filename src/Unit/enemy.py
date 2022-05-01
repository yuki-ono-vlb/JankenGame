from functools import partial
from tkinter import Label, Text
from tkinter.ttk import Progressbar
from Unit.unit_base import UnitBase

from random import random, randrange

from const import Const


class Enemy(UnitBase):
	'''
	エネミーに関する処理を扱うクラス
	'''

	def __init__(self, name: Text, print: partial, hp_value: Label, hp_bar: Progressbar):
		super().__init__(name=name, print=print, hp_value=hp_value, hp_bar=hp_bar)

	def next_hand(self):
		'''
		エネミーの手をセットする
		'''
		hand: int = randrange(start=0, stop=Const.JANKEN_NAM)
		self.print(
			f"{super().get_name()}は{[key for key, value in Const.JANKEN.items() if value == hand][0]}を出してきた。{Const.NEW_LINE}")
		super().set_hand(hand)
