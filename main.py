from bot import *
import game


make_url_()




# keyboard =  {
#             "keyboard":[[{"text": "Кнопка 1"}, {"text": "Кнопка 2"}], [{"text": "Кнопка 3"}]],
#             "resize_keyboard":True, "one_time_keyboard": True
#             }








# print(sendReply_(425925900, 'AAAAAAAAA', keyboard))



def main():
	new_offset = None

	while True:
		update = get_(new_offset)
		try:
			update['result'][0]['message']
		except IndexError:
			print('nothing')
			continue
		except KeyError:
			print('чего-то не хватает')
			new_offset = update['result'][0]['update_id'] + 1
			continue

		update = update['result'][0]
		update_id = update['update_id']
		print(update_id)
		chat_id = update['message']['chat']['id']
		chat_type = update['message']['chat']['type']
		user_id = update['message']['from']['id']
		user_name = update['message']['from']['first_name']
		try:
			chat_text = update['message']['text']
			print(chat_text)
		except KeyError:
			chat_text = None

		

		if (chat_text == '/startgame@anatm_f_bot'
		or chat_text == '/startgame'):
			game.game_start(chat_id)

		if (chat_text == '/add@anatm_f_bot'
		or chat_text == '/add'):
			game.setListOfPlayers(chat_id, user_id)

		if (chat_text == '/stopgame@anatm_f_bot'
		or chat_text == '/stopgame'):
			game.stopTheGame(chat_id)

		new_offset = update_id + 1
		print(new_offset)


if __name__ == '__main__':
	main()


















