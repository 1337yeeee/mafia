import requests as r
import json



def make_url_():
	global url

	url = 'https://api.telegram.org/bot'
	url = url + input('here goes token>>\n') + '/'


def get_(offset=None, timeout=30):
    method = 'getUpdates'
    params = {'timeout': timeout, 'offset': offset}
    resp = r.get(url + method, params)
    result = resp.json()
    return result


def send_(chat_id, text):
    method = 'sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    resp = r.post(url + method, params)
    return resp


def sendReply_(chat_id, text, reply_markup):
	method = 'sendMessage'
	params = {'chat_id': chat_id, 'text': text,
	'reply_markup': json.dumps(reply_markup)}
	resp = r.post(url + method, params)
	return resp