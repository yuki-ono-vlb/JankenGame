from functools import partial
from tkinter import Label, Text
from tkinter.ttk import Progressbar
from Unit.unit_base import UnitBase


class Prayer(UnitBase):
	'''
	プレイヤーに関する処理を扱うクラス
	'''

	def __init__(self, name: Text, print: partial, hp_value: Label, hp_bar: Progressbar):
		super().__init__(name=name, print=print, hp_value=hp_value, hp_bar=hp_bar)

	def next_hand(self, hand: int):
		'''
		プレイヤーの手をセットする
		'''
		super().set_hand(hand)
