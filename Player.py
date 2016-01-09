# -*- coding: utf-8 -*-

from Globals import *

import copy

class State(object):
	def __init__(self):
		self.vp = 0;
		self.money = copy.deepcopy(Glob.stones)
		self.tag = 'state'

	# drukowanie punktów zwycięstwa i posiadanych bonusów(kamieni)
	def print_state(self):
		Glob.canvas.create_text(Glob.WINDOW_X-5, 35, anchor='e', text='VP: '+str(self.vp), tags=self.tag)
		i = 55
		for stone in self.money:
			Glob.canvas.create_image(Glob.WINDOW_X-5, i, anchor='e', image=Glob.stoneToImage[stone], tags=self.tag)
			Glob.canvas.create_text(Glob.WINDOW_X-30, i, anchor='e', text=str(self.money[stone]), tags=self.tag)
			i += 25

	# aktualiacja danych
	def update_state(self):
		Glob.canvas.delete(self.tag)
		self.print_state()

class Player(object):
	count = 0

	def __init__(self):
		Player.count += 1
		self.id = self.count
		self.tokenCount = 0
		self.gotToken = False
		self.tmpTokens = copy.deepcopy(Glob.stones)
		self.state = State()
		self.tokens = []
		self.cards = []
		self.tokensBon = copy.deepcopy(Glob.stones)
		self.cardsBon = copy.deepcopy(Glob.stones)
		self.tokensPos = copy.deepcopy(Glob.stones)
		self.cardsPos = copy.deepcopy(Glob.stones)
		self.set_cards_and_tokens_pos()
		self.state.print_state()
	
	# ustawienie pozycji dla kart w polu gracza
	def set_cards_and_tokens_pos(self):
		xC = 530
		yC = 100
		xT = 550
		yT = 450
		for pos in self.cardsPos:
			self.cardsPos[pos] = [xC, yC]
			self.tokensPos[pos] = [xT, yT]
			xC+=90
			xT+=65

	# zabieranie żetonu:
	# można zabrać trzy różne lub dwa tego samego rodzaju
	def get_token(self, token):
		if self.tmpTokens[token.bonus]==1:
			if self.can_buy_second_token(token):
				self.move_token_and_update(token)
			else:
				return
		elif self.tokenCount==2 and self.tmpTokens[token.bonus]==1:
			return
		else:
			self.move_token_and_update(token)

		self.state.update_state()
		if self.tokenCount==3 or (2 in self.tmpTokens.values()):
			Glob.game.change_player()


	# funkcja która przenosi znacznik i aktualizuje właściwości gracza
	def move_token_and_update(self, token):
		self.gotToken = True
		self.state.money[token.bonus]+=1
		self.tokensBon[token.bonus]+=1
		token.move(self.tokensPos[token.bonus][0]-token.a[0], self.tokensPos[token.bonus][1]-token.a[1])
		self.tokenCount+=1
		self.tmpTokens[token.bonus]+=1
		self.tokensPos[token.bonus][1]+=10
		Glob.tokensPos[token.bonus][1]-=10
		self.tokens.insert(0, Glob.tokens.pop(Glob.tokens.index(token)))

	# jeśli gracz ma jeden żeton to może kupić żeton tego samego rodzaju
	def can_buy_second_token(self, token):
		tmpValues = self.tmpTokens.values()
		if tmpValues.count(1)==1 and self.tmpTokens.get(token.bonus)==1:
			return True
		else:
			return False

	# kupowanie karty:
	# sprawdzamy czy nie wzięto już żetonu, jeśli tak to return
	# sprawdzamy czy można kupić kartę(can_buy_card())
	# 	zwracamy tokeny
	# 	przesuwamy karte i dajemy ją graczowi
	def buy_card(self, card):
		if self.gotToken:
			return

		if self.can_buy_card(card):
			self.return_tokens_after_buy(card)
			self.move_card_and_update(card)
		else:
			return

		self.state.update_state()
		if Glob.game.is_end():
			return
		Glob.game.change_player()

	# funkcja która przenosi zakupioną kartę i aktualizuje właściwości gracza
	def move_card_and_update(self, card):
		self.state.money[card.bonus]+=1
		self.cardsBon[card.bonus]+=1
		self.state.vp += 0 if card.vp=='' else int(card.vp)

		Glob.game.draw_new_card(type(card), card)			
		card.move(self.cardsPos[card.bonus][0]-card.a[0], self.cardsPos[card.bonus][1]-card.a[1])
		self.cards.append(card)
		self.cardsPos[card.bonus][1]+=23

	# czy można kupić kartę - czy koszt karty jest mniejszy od posiadanych funduszy
	def can_buy_card(self, card):
		for stone in card.cost:
			if self.state.money[stone]<card.cost[stone]:
				return False
		return True

	# zwracanie żetonów po zakupie: uaktualnianie funduszy, pozycji żetonów
	def return_tokens_after_buy(self, card):
		tmpCost = copy.deepcopy(Glob.stones)
		for stone in tmpCost:
			if card.cost[stone]>0:
				tmpCost[stone] = card.cost[stone] - self.cardsBon[stone] # odejmowanie bonusów, czyli ile trzeba wydać żetonów
				tmpCost[stone] = tmpCost[stone] if tmpCost[stone]>=0 else 0 # jeśli wynik byłby ujemny ustawiam 0
				self.tokensBon[stone] -= tmpCost[stone] # odejmuje pozostały koszt od posiadanych żetonów
				self.state.money[stone] -= tmpCost[stone] # odejmuje również od ogólnie posiadanych
				for i in range(tmpCost[stone]):
					tmpToken = self.find_appr_token_here(stone)
					self.tokensPos[stone][1]-=10
					Glob.tokensPos[stone][1]+=10
					Glob.game.return_token(tmpToken)
					Glob.tokens.insert(0, self.tokens.pop(self.tokens.index(tmpToken)))

	# znajdowanie odpowiedniego żetonu po nazwie(pierwszego w self.tokens czyli tego którego szukamy)
	def find_appr_token_here(self, stone):
		for token in self.tokens:
			if token.bonus==stone:
				return token