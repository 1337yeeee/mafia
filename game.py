# from bot import *
import random
from bot import *


games = {}
numb_of_players = 0
Players = []


def game_start(chat_id):
	global games
	if chat_id not in games:
		games[chat_id] = {'start': 0, 'players': {}}
		send_(chat_id, 'Who\'s gonna play some mafia?\n\
			            *send command add and write your name')
	else: send_(chat_id, 'Please end previous game to start a new one\n\
		**send command /stopgame')


def setListOfPlayers(chat_id, user_id):
	global games
	if chat_id in games:
		if games[chat_id]['start'] == 0:
			if user_id not in games[chat_id]['players']:
				games[chat_id]['players'][user_id] = {
				'name': None,'state': -1, 'role': -1,
				'round': -1, 'target': -1 }
				print('{} = {}'.format(user_id,
				games[chat_id]['players'][user_id]))
	# 		else: print('*----------*\nPlayer already is in list,\
	# 			named as {}\n profile name is {}\n*----------*')
	# 	else: print('*------*\ngame is already started\n*------*')
	# else: print('*------*\ngame hasn\'t been initialized yet\n*------*')


def stopTheGame(chat_id):
	global games
	if chat_id in games:
		del games[chat_id]

##-----------------------##
def aa():
	global numb_of_players

	playeRS = []


def needname(user_id, user_name):
	global numb_of_players, Players

	Players.append[(user_id,user_name)]
	numb_of_players += 1


def some():
	global numb_of_players, Players

	players = {}

	for i in range(numb_of_players):
		players[Players[0]] = [Players[1], 1, -1, -1, None]

	return players


def fillPlayersRoles():
	global numb_of_players

	Roles = [0,0,0,1,2,3,1,0,2]
	roles = []

	for i in range(numb_of_players):
		roles.append(Roles[i])
	# 	загружаются доступные для игры роли


	for i in range(numb_of_players):
		role = random.choice(roles)
		roles.pop(role)
		players[i] = [1, role, 0, None]
	# 	игрокам заполняется словарь, определяются их роли



def gameRound(round):
	pass