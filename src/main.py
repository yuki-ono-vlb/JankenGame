# -*- coding: utf-8 -*-
# インポート
import sys
from tkinter import HORIZONTAL, LEFT, END, Button, Entry, Frame, Label, PhotoImage, Text, Tk
from tkinter.messagebox import showinfo, showerror
from functools import partial
from tkinter.ttk import Progressbar
from Unit.enemy import Enemy
from Unit.prayer import Prayer
from const import Const
from utill.func import is_none_empty


class Application(Frame):

	def __init__(self, root: Frame):
		super().__init__(root, width=320, height=640, borderwidth=1, relief='groove')
		self.root = root
		# GUI上のタイトルを設定
		self.root.title("Janken Game")
		self.root.iconphoto(False, PhotoImage(file='src/file/janken.png'))
		self.pack()
		self.rock_img: PhotoImage = PhotoImage(
			file="src/file/janken_rock.png").subsample(3, 3)
		self.scissors_img: PhotoImage = PhotoImage(
			file="src/file/janken_scissors.png").subsample(3, 3)
		self.paper_img: PhotoImage = PhotoImage(
			file="src/file/janken_paper.png").subsample(3, 3)
		self.__create_widgets()
		self.print: partial = partial(self.log_message.insert, END)

		self.enemy_unit: Enemy = Enemy(
			name=self.enemy_name, print=self.print, hp_value=self.enemy_hp, hp_bar=self.enemy_bar)
		self.prayer_unit: Prayer = Prayer(
			name=self.prayer_name, print=self.print, hp_value=self.prayer_hp, hp_bar=self.prayer_bar)

	def __create_widgets(self):
		'''
		ウィジットの作成
		'''
		# ウィジットを作成
		enemy_frame: Frame = Frame(self)
		prayer_frame: Frame = Frame(self)
		menu_frame: Frame = Frame(self)
		janken_frame: Frame = Frame(self)
		enemy_hp_frame: Frame = Frame(self)
		prayer_hp_frame: Frame = Frame(self)

		# Enemy Nameの文言を表示させる
		enemy_label: Label = Label(enemy_frame, text="Enemy Name")
		self.enemy_name: Entry = Entry(enemy_frame, state=Const.NORMAL, width="50")
		self.enemy_hp: Label = Label(
			enemy_hp_frame, text=f"{Const.HP_MAX}/{Const.HP_MAX}", width="10")
		self.enemy_bar: Progressbar = Progressbar(
			enemy_hp_frame, length=Const.BAR_LENGTH, maximum=Const.HP_MAX, value=Const.HP_MAX, cursor="spider", mode="determinate", orient=HORIZONTAL)
		# Prayer Nameの文言を表示させる
		prayer_label: Label = Label(prayer_frame, text="Prayer Name")
		self.prayer_name: Entry = Entry(prayer_frame, state=Const.NORMAL, width="50")
		self.prayer_hp: Label = Label(
			prayer_hp_frame, text=f"{Const.HP_MAX}/{Const.HP_MAX}", width="10")
		self.prayer_bar: Progressbar = Progressbar(
			prayer_hp_frame, length=Const.BAR_LENGTH, maximum=Const.HP_MAX, value=Const.HP_MAX, cursor="spider", mode="determinate", orient=HORIZONTAL)

		# メニューの設定
		self.start: Button = Button(
			menu_frame, text="Start", width=Const.BTN_WIDTH, state=Const.NORMAL)
		self.start.bind("<ButtonPress>", self.__on_start)
		self.restart: Button = Button(
			menu_frame, text="ReStart", width=Const.BTN_WIDTH, state=Const.DISABLE)
		self.restart.bind("<ButtonPress>", self.__on_restart)
		self.end: Button = Button(menu_frame, text="End",
		                          width=Const.BTN_WIDTH, state=Const.DISABLE)
		self.end.bind("<ButtonPress>", self.__on_end)

		# じゃんけんの設定

		self.rock: Button = Button(janken_frame, text="グー", image=self.rock_img,
                             compound="top", state=Const.DISABLE)
		self.rock.bind("<ButtonPress>", self.__on_click)
		self.scissors: Button = Button(janken_frame, text="チョキ",
                                 image=self.scissors_img, compound="top", state=Const.DISABLE)
		self.scissors.bind("<ButtonPress>", self.__on_click)
		self.paper: Button = Button(janken_frame, text="パー",
                              image=self.paper_img, compound="top", state=Const.DISABLE)
		self.paper.bind("<ButtonPress>", self.__on_click)

		# ログテキストの設定
		self.log_message: Text = Text(self, state=Const.NORMAL)

		# エネミーに関するウィジットの配置場所を設定
		enemy_frame.pack()
		enemy_label.pack(side=LEFT)
		self.enemy_name.pack(side=LEFT)
		enemy_hp_frame.pack()
		self.enemy_hp.pack(side=LEFT)
		self.enemy_bar.pack(side=LEFT)

		# ログに関するウィジットの配置場所を設定
		self.log_message.pack()

		# プレイヤーに関するウィジットの配置場所を設定
		prayer_frame.pack()
		prayer_label.pack(side=LEFT)
		self.prayer_name.pack(side=LEFT)
		prayer_hp_frame.pack()
		self.prayer_hp.pack(side=LEFT)
		self.prayer_bar.pack(side=LEFT)

		# メニューに関するウィジットの配置場所を指定
		menu_frame.pack()
		self.start.pack(side=LEFT)
		self.restart.pack(side=LEFT)
		self.end.pack(side=LEFT)

		# じゃんけんに関するウィジットの配置場所を指定
		janken_frame.pack()
		self.rock.pack(side=LEFT)
		self.scissors.pack(side=LEFT)
		self.paper.pack(side=LEFT)

	def __on_start(self, event):
		'''
		ゲームの開始
		'''
		try:
			if is_none_empty(self.prayer_unit.get_name()) and is_none_empty(self.enemy_unit.get_name()):
				showerror(Const.ERR_TITLE, f"プレイヤーとエネミー{Const.ERR_MESSAGE}")
				return
			elif is_none_empty(self.prayer_unit.get_name()) or is_none_empty(self.enemy_unit.get_name()):
				target: str = "プレイヤー"
				if is_none_empty(self.enemy_unit.get_name()):
					target = "エネミー"
				showerror(Const.ERR_TITLE, f"{target}{Const.ERR_MESSAGE}")
				return

			self.print(f"ゲーム開始!!{Const.NEW_LINE}")
			self.log_message.see('end')

			self.rock[Const.STATE] = Const.NORMAL
			self.scissors[Const.STATE] = Const.NORMAL
			self.paper[Const.STATE] = Const.NORMAL
			self.enemy_name[Const.STATE] = Const.DISABLE
			self.prayer_name[Const.STATE] = Const.DISABLE
			self.start[Const.STATE] = Const.DISABLE
			self.restart[Const.STATE] = Const.NORMAL
			self.end[Const.STATE] = Const.NORMAL
		except Exception as e:
			print(f"type:{type(e)}")
			print(f"message:{e}")

	def __on_click(self, event):
		'''
		ゲームの進行
		'''
		try:
			if self.start[Const.STATE] == Const.NORMAL:
				return
			self.prayer_unit.next_hand(Const.JANKEN[event.widget["text"]])
			self.enemy_unit.next_hand()
			self.__judge()
   
		except Exception as e:
			print(f"type:{type(e)}")
			print(f"message:{e}")

	def __on_restart(self, event):
		'''
		ゲームの遣り直し
		'''
		self.enemy_unit.end_game()
		self.prayer_unit.end_game()

		self.__on_start(event=event)

	def __on_end(self, event):
		self.__end()

	def __end(self):
		'''
		ゲーム終了
		'''
		if self.end[Const.STATE] == Const.DISABLE:
			return

		self.print(f"お疲れさまでした。ゲーム終了です。{Const.NEW_LINE}")
		self.log_message.see('end')
  
		self.prayer_unit.end_game()
		self.enemy_unit.end_game()
		self.rock[Const.STATE] = Const.DISABLE
		self.scissors[Const.STATE] = Const.DISABLE
		self.paper[Const.STATE] = Const.DISABLE
		self.enemy_name[Const.STATE] = Const.NORMAL
		self.prayer_name[Const.STATE] = Const.NORMAL
		self.start[Const.STATE] = Const.NORMAL
		self.restart[Const.STATE] = Const.DISABLE
		self.end[Const.STATE] = Const.DISABLE

	def __judge(self):
		'''
		じゃんけんの勝敗とHPの更新を行う
		'''

		if self.prayer_unit.get_hand() == self.enemy_unit.get_hand():
			self.print(f"あいこだ！！{Const.NEW_LINE}")
			self.log_message.see('end')
			return

		win_unit: str = self.prayer_unit.get_name()
		if ((self.prayer_unit.get_hand() == Const.JANKEN["グー"]) and (self.enemy_unit.get_hand() == Const.JANKEN["チョキ"]) or (self.prayer_unit.get_hand() == Const.JANKEN["チョキ"]) and (self.enemy_unit.get_hand() == Const.JANKEN["パー"]) or (self.prayer_unit.get_hand() == Const.JANKEN["パー"]) and (self.enemy_unit.get_hand() == Const.JANKEN["グー"])):
			self.enemy_unit.damage()
			self.enemy_unit.display_status()
		elif ((self.prayer_unit.get_hand() == Const.JANKEN["グー"]) and (self.enemy_unit.get_hand() == Const.JANKEN["パー"]) or (self.prayer_unit.get_hand() == Const.JANKEN["チョキ"]) and (self.enemy_unit.get_hand() == Const.JANKEN["グー"]) or (self.prayer_unit.get_hand() == Const.JANKEN["パー"]) and (self.enemy_unit.get_hand() == Const.JANKEN["チョキ"])):
			win_unit = self.enemy_unit.get_name()
			self.prayer_unit.damage()
			self.prayer_unit.display_status()
   
		self.print(f"{win_unit}{Const.WIN}{Const.NEW_LINE}")
		self.log_message.see('end')

		if self.prayer_unit.is_dead() or self.enemy_unit.is_dead():
			result:str = "Win!!"
			if self.prayer_unit.is_dead():
				result = "lose!!"

			showinfo(title="結果", message=f"You {result}")

			self.__end()


if __name__ == '__main__':
	#ウィジットの設定
	app = Application(Tk())

	# GUIを表示
	app.mainloop()
