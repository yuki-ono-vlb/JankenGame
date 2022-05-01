from tkinter import Label, Text
from tkinter.ttk import Progressbar
from const import Const
from functools import partial
from random import random


class UnitBase():
	'''
	ユニットの基底クラス
	'''

	def __init__(self, name: Text, print: partial, hp_value: Label, hp_bar: Progressbar):
		self.name: Text = name
		self.hp: int = Const.HP_MAX
		self.print: partial = print
		self.hp_value = hp_value
		self.hp_bar: Progressbar = hp_bar
		self.hand: int
		self.hp_bar['value'] = Const.HP_MAX
		self.hp_value["text"] = f"{Const.HP_MAX}/{Const.HP_MAX}"

	def get_name(self) -> str:
		'''
		ユニット名を取得
		'''
		return self.name.get()

	def get_hp(self) -> int:
		'''
		ユニットのHPを取得
		'''
		return self.hp

	def set_hand(self, hand: int):
		'''
		じゃんけんの手を設定
		'''
		self.hand = hand

	def get_hand(self) -> int:
		'''
		じゃんけんの手を取得
		'''
		return self.hand

	def is_dead(self) -> bool:
		'''
		死亡判定
		'''
		return self.hp <= 0

	def damage(self):
		'''
		ダメージ計算
		'''
		value: int = int((random() * 2) + 1)
		_random: int = int(random() * Const.CLITICAL_NAM)

		if _random == 0:
			value *= Const.CRITICAL_MAGNIFICATION
			self.print(f"強烈な一撃!!{Const.NEW_LINE}")
		self.print(f"{self.get_name()}は{value}のダメージを受けた!{Const.NEW_LINE}")
		self.hp -= value
		self.hp_bar['value'] = self.hp

	def display_status(self):
		'''
		画面に表示
		'''
		self.hp_value["text"] = f"{self.hp}/{Const.HP_MAX}"


	def end_game(self):
		'''
		初期化
		'''
		self.hp = Const.HP_MAX
		self.hp_bar['value'] = Const.HP_MAX
		self.hp_value["text"] = f"{Const.HP_MAX}/{Const.HP_MAX}"
