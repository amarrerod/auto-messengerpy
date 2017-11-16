import time
import sys

from fbchat import Client
from fbchat.models import *


def sendInLoop(client, username, type, delay, message=None, image=None, emoji=None, emoji_size=None):
	user = client.searchForUsers(username)[0]
	if __debug__:
		print('User uid: {}'.format(user.uid))
		print('User name: {}'.format(user.name))
		print("User's photo: {}".format(user.photo))
		print("Is user client's friend: {}".format(user.is_friend))

	while True:
		if image is not None:
			if __debug__:
				print('Image is not None: {}'.format(image))
			client.sendRemoteImage(str(image), thread_id=user.uid, thread_type=ThreadType.USER)
		if message is not None:
			if __debug__:
				print('Message: {}'.format(message))
			client.send(Message(text=str(message)), thread_id=user.uid, thread_type=type)
		if emoji is not None:
			if __debug__:
				print('Emoji is not None: {}'.format(emoji))
			client.send(Message(text=str(emoji), emoji_size=emoji_size), thread_id=user.uid, thread_type=type)
		time.sleep(delay)
