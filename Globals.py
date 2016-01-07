# -*- coding: utf-8 -*-

from Tkinter import *
import tkFont

class Glob(object):
	# mnoznik - do zmiany szerokości i wysokości
	# albo po prostu lista dostępnych rozmiarów
	WINDOW_X = 1024
	WINDOW_Y = 768
	SIZE_X = 80
	SIZE_Y = 120
	TOKEN_DIAMETER = 50
	root = Tk()
	canvas = Canvas(root, width=WINDOW_X, height=WINDOW_Y)
	myFont = tkFont.Font(family="sans-serif", size=12)
	vpFont = tkFont.Font(family="sans-serif", size=12, weight='bold')
	firstLevCards = []
	secLevCards = []
	thirdLevCards = []
	tokens = []
	game = 0
	tokensPos = {'red': [50, 500], 'green': [120, 500], 'blue': [190, 500], 'white': [260, 500], 'black': [330, 500]}
	stones = {'red': 0, 'green': 0, 'blue': 0, 'white': 0, 'black': 0}
	stonesNames = ['red', 'green', 'blue', 'white', 'black']
	# colorToStone = {'red': 'Rubiny', 'green': 'Szmaragdy', 'blue': 'Szafiry', 'white': 'Diamenty', 'black': 'Onyksy'}
	stoneToColor = {'red': '#ff3333', 'green': '#99ff33', 'blue': '#3333ff', 'white': '#ccffcc', 'black': '#000033'}
	stoneToImage = {'red': PhotoImage(file='./images/ruby.ppm'),
					'green': PhotoImage(file='./images/emerald.ppm'),
					'blue': PhotoImage(file='./images/sapphire.ppm'),
					'white': PhotoImage(file='./images/diamond.ppm'),
					'black': PhotoImage(file='./images/onyx.ppm')
					}