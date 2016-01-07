# -*- coding: utf-8 -*-

from Tkinter import *
from Globals import Glob

import random
import copy


class Card(object):
	def __init__(self, x, y):
		if x<0 or x>Glob.WINDOW_X-Glob.SIZE_X or y<0 or y>Glob.WINDOW_Y-Glob.SIZE_Y:
			raise ValueError("Podane współrzędne leżą poza oknem aplikacji.")
		if not( type(x)==int or type(y)==int ):
			raise TypeError()

		self.a = x, y
		self.b = x+Glob.SIZE_X, y+Glob.SIZE_Y
		self.color = 'white'
		self.rect = Glob.canvas.create_rectangle(self.a, self.b, fill=self.color)
		self.tag = str(self.rect) + 't'
		Glob.canvas.itemconfig(self.rect, tags=self.tag)
		Glob.canvas.create_line(self.a[0], self.a[1]+23, self.b[0], self.a[1]+23, tags=self.tag)

	def __setitem__(self, x, y):
		self.a = x, y
		self.b = x+Glob.SIZE_X, y+Glob.SIZE_Y

	def get_cords(self):
		return self.a, self.b

	def move(self, x, y):
		if (self.a[0]+x)<0 or (self.a[0]+x)>Glob.WINDOW_X-Glob.SIZE_X or (self.a[1]+y)<0 or (self.a[1]+y)>Glob.WINDOW_Y-Glob.SIZE_Y:
			raise ValueError()
		if not( type(x)==int or type(y)==int ):
			raise TypeError()

		self.a = self.a[0]+x, self.a[1]+y
		self.b = self.a[0]+Glob.SIZE_X, self.a[1]+Glob.SIZE_Y
		Glob.canvas.move(self.tag, x, y)
		Glob.canvas.tag_raise(self.tag)


class FirstLevelCard(Card):
	bonuses = (copy.deepcopy(Glob.stonesNames))*8
	random.shuffle(bonuses)

	@classmethod
	def gen_attrs(cls):
		vp = random.randint(0, 1)

		bonus = cls.bonuses.pop()

		cost = copy.deepcopy(Glob.stones)
		tmpStones = copy.deepcopy(Glob.stonesNames)
		random.shuffle(tmpStones)
		numOfStones = random.randint(2, 4)
		for j in range(numOfStones):
				cost[tmpStones.pop()] = random.randint(1,3)

		return {'vp': vp, 'bonus': bonus, 'cost': cost}

	def __init__(self, x, y):
		tmpAttr = self.gen_attrs()
		self.vp = tmpAttr['vp'] if tmpAttr['vp'] else ""
		self.bonus = tmpAttr['bonus']
		self.cost = tmpAttr['cost']
		self.image = Glob.stoneToImage[self.bonus]
		super(FirstLevelCard, self).__init__(x, y)

		Glob.canvas.create_text(self.a[0]+5, self.a[1]+12, text=self.vp, tags=self.tag, anchor='w', font=Glob.vpFont)
		Glob.canvas.create_image(self.b[0]-5, self.a[1]+12, image=self.image, tags=self.tag, anchor='e')
		i = 10
		for x in self.cost:
			tmp=self.cost.get(x)
			if tmp==0:
				continue
			Glob.canvas.create_image(self.b[0]-(Glob.SIZE_X/2)+25, self.b[1]-i, image=Glob.stoneToImage.get(x), tags=self.tag, anchor='e')
			Glob.canvas.create_text(self.b[0]-(Glob.SIZE_X/2)-5, self.b[1]-i, text=str(tmp), tags=self.tag, anchor='e', font=(12))
			i+=23

		Glob.canvas.pack()
		Glob.firstLevCards.insert(0, self)

class SecondLevelCard(Card):
	bonuses = (copy.deepcopy(Glob.stonesNames))*6
	random.shuffle(bonuses)

	@classmethod
	def gen_attrs(cls):
		vp = random.randint(1, 3)

		bonus = cls.bonuses.pop()

		cost = copy.deepcopy(Glob.stones)
		tmpStones = copy.deepcopy(Glob.stonesNames)
		random.shuffle(tmpStones)
		numOfStones = random.randint(2, 4)
		for j in range(numOfStones):
				cost[tmpStones.pop()] = random.randint(3,5)

		return {'vp': vp, 'bonus': bonus, 'cost': cost}

	def __init__(self, x, y):
		tmpAttr = self.gen_attrs()
		self.vp = tmpAttr['vp']
		self.bonus = tmpAttr['bonus']
		self.cost = tmpAttr['cost']
		self.image = Glob.stoneToImage[self.bonus]
		super(SecondLevelCard, self).__init__(x, y)

		Glob.canvas.create_text(self.a[0]+5, self.a[1]+12, text=self.vp, tags=self.tag, anchor='w', font=Glob.vpFont)
		Glob.canvas.create_image(self.b[0]-5, self.a[1]+12, image=self.image, tags=self.tag, anchor='e')
		i = 10
		for x in self.cost:
			tmp=self.cost.get(x)
			if tmp==0:
				continue
			Glob.canvas.create_image(self.b[0]-(Glob.SIZE_X/2)+25, self.b[1]-i, image=Glob.stoneToImage.get(x), tags=self.tag, anchor='e')
			Glob.canvas.create_text(self.b[0]-(Glob.SIZE_X/2)-5, self.b[1]-i, text=str(tmp), tags=self.tag, anchor='e', font=(12))
			i+=23

		Glob.canvas.pack()
		Glob.secLevCards.insert(0, self)

class ThirdLevelCard(Card):
	bonuses = (copy.deepcopy(Glob.stonesNames))*4
	random.shuffle(bonuses)

	@classmethod
	def gen_attrs(cls):
		vp = random.randint(3, 5)

		bonus = cls.bonuses.pop()

		cost = copy.deepcopy(Glob.stones)
		tmpStones = copy.deepcopy(Glob.stonesNames)
		random.shuffle(tmpStones)
		numOfStones = random.randint(2, 4)
		for j in range(numOfStones):
				cost[tmpStones.pop()] = random.randint(3,7)

		return {'vp': vp, 'bonus': bonus, 'cost': cost}

	def __init__(self, x, y):
		tmpAttr = self.gen_attrs()
		self.vp = tmpAttr['vp']
		self.bonus = tmpAttr['bonus']
		self.cost = tmpAttr['cost']
		self.image = Glob.stoneToImage[self.bonus]
		super(ThirdLevelCard, self).__init__(x, y)

		Glob.canvas.create_text(self.a[0]+5, self.a[1]+12, text=self.vp, tags=self.tag, anchor='w', font=Glob.vpFont)
		Glob.canvas.create_image(self.b[0]-5, self.a[1]+12, image=self.image, tags=self.tag, anchor='e')

		i = 10
		for x in self.cost:
			tmp=self.cost.get(x)
			if tmp==0:
				continue
			Glob.canvas.create_image(self.b[0]-(Glob.SIZE_X/2)+25, self.b[1]-i, image=Glob.stoneToImage.get(x), tags=self.tag, anchor='e')
			Glob.canvas.create_text(self.b[0]-(Glob.SIZE_X/2)-5, self.b[1]-i, text=str(tmp), tags=self.tag, anchor='e', font=(12))
			i+=23

		Glob.canvas.pack()
		Glob.thirdLevCards.insert(0, self)