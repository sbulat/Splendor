# -*- coding: utf-8 -*-

from Globals import *

import copy

class Player(object):
	count = 0
	tmpTokens = copy.deepcopy(Glob.stones)
	tokenCount = 0
	gotToken = False

	def __init__(self):
		Player.count += 1
		self.id = self.count
		self.vp = 0
		self.cards = []
		self.tokens = []
		self.money = copy.deepcopy(Glob.stones)
		self.tokensBon = copy.deepcopy(Glob.stones)
		self.cardsBon = copy.deepcopy(Glob.stones)
		self.cardsPos = copy.deepcopy(Glob.stones)
		self.tokensPos = copy.deepcopy(Glob.stones)
		self.set_cards_and_tokens_pos()
	
	def set_cards_and_tokens_pos(self):
		xC = 600
		yC = 100
		xT = 600
		yT = 450
		for pos in self.cardsPos:
			self.cardsPos[pos] = [xC, yC]
			self.tokensPos[pos] = [xT, yT]
			xC+=90
			xT+=65

	def get_token(self, token):
		if Player.tokenCount>3:
			raise NotImplementedError()
		elif Player.tokenCount==3 or (2 in Player.tmpTokens.values()):
			# pass
			Player.tokenCount = 0
			Player.gotToken = False
			Player.tmpTokens = copy.deepcopy(Glob.stones)
			# koniec tury gracza
		else:
			if Player.tmpTokens[token.bonus]==1:
					if self.can_buy_second_token(token):
						self.move_token_and_update(token)
					else:
						return
			elif Player.tokenCount==2 and Player.tmpTokens[token.bonus]==1:
				return
			else:
				self.move_token_and_update(token)


	# funkcja która przenosi znacznik i aktualizuje właściwości gracza
	def move_token_and_update(self, token):
		Player.gotToken = True
		self.money[token.bonus]+=1
		self.tokensBon[token.bonus]+=1
		token.move(self.tokensPos[token.bonus][0]-token.a[0], self.tokensPos[token.bonus][1]-token.a[1])
		Player.tokenCount+=1
		Player.tmpTokens[token.bonus]+=1
		self.tokensPos[token.bonus][1]+=10
		self.tokens.insert(0, Glob.tokens.pop(Glob.tokens.index(token)))

	@staticmethod
	def can_buy_second_token(token):
		tmpValues = Player.tmpTokens.values()
		if tmpValues.count(1)==1 and Player.tmpTokens.get(token.bonus)==1:
			return True
		else:
			return False

	# TODO: cała funkcja kupowania karty jest do zrobienia. na razie jedynie moge zakupic karte, jesli mam fundusze
	# po pierwsze nie są zwracane żetony które były użyte do kupna
	def buy_card(self, card):
		if self.gotToken:
			return

		if self.can_buy_card(card):
			self.return_tokens_after_buy(card)
			self.move_card_and_update(card)

	# funkcja która przenosi zakupioną kartę i aktualizuje właściwości gracza
	def move_card_and_update(self, card):
		self.money[card.bonus]+=1
		self.cardsBon[card.bonus]+=1
		self.vp += int(card.vp)
		for stone in card.cost:
			self.money[stone]-=card.cost[stone]

		Glob.game.draw_new_card(type(card), card)			
		card.move(self.cardsPos[card.bonus][0]-card.a[0], self.cardsPos[card.bonus][1]-card.a[1])
		self.cards.append(card)
		self.cardsPos[card.bonus][1]+=23

	def can_buy_card(self, card):
		for stone in card.cost:
			if self.money[stone]<card.cost[stone]:
				return False
		return True

	def return_tokens_after_buy(self, card):
		tmpCost = copy.deepcopy(Glob.stones)
		for stone in tmpCost:
			if card.cost[stone]>0:
				tmpCost[stone] = card.cost[stone] - self.cardsBon[stone] # odejmowanie bonusów, czyli ile trzeba wydać żetonów
				tmpCost[stone] = tmpCost[stone] if tmpCost[stone]>=0 else 0 # jeśli wynik byłby ujemny ustawiam 0
				self.tokensBon[stone] -= tmpCost[stone] # odejmuje pozostały koszt od posiadanych żetonów
				for i in range(tmpCost[stone]):
					tmpToken = self.find_appr_token_here(stone)
					self.tokensPos[stone][1]-=10
					Glob.game.return_token(tmpToken)
					Glob.tokens.insert(0, self.tokens.pop(self.tokens.index(tmpToken)))				

	def find_appr_token_here(self, stone):
		for token in self.tokens:
			if token.bonus==stone:
				return token	