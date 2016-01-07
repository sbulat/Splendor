# -*- coding: utf-8 -*-

from Globals import *

class Token(object):
	pos = [50, 500]
	def __init__(self, x, y, bonus):
		self.a = x, y
		self.b = x+Glob.TOKEN_DIAMETER, y+Glob.TOKEN_DIAMETER
		self.bonus = bonus
		self.image = Glob.stoneToImage[self.bonus]

		self.ov = Glob.canvas.create_oval(self.a, self.b, fill='white')
		self.tag = str(self.ov) + 't'
		Glob.canvas.itemconfig(self.ov, tags=self.tag)
		Glob.canvas.create_image(self.a[0]+(Glob.TOKEN_DIAMETER/2), self.a[1]+(Glob.TOKEN_DIAMETER/2), tags=self.tag, image=self.image)
		Glob.canvas.pack()

		Glob.tokens.insert(0, self)

	def move(self, x, y):
		if (self.a[0]+x)<0 or (self.a[0]+x)>Glob.WINDOW_X-Glob.TOKEN_DIAMETER or \
			(self.a[1]+y)<0 or (self.a[1]+y)>Glob.WINDOW_Y-Glob.TOKEN_DIAMETER:
			raise ValueError()
		if not( type(x)==int or type(y)==int ):
			raise TypeError()

		self.a = self.a[0]+x, self.a[1]+y
		self.b = self.a[0]+Glob.SIZE_X, self.a[1]+Glob.SIZE_Y
		Glob.canvas.move(self.tag, x, y)
		Glob.canvas.tag_raise(self.tag)		