import time
import sys

from fbchat import Client
from fbchat.models import *

class Send:
	def __init__(self):
		pass
	
	def send(client, username, type, message=None, image=None, emoji=None,
	emoji_size=None):
		user = client.searchForUsers(username)[0]
		if __debug__:
			print(f"User uid: {user.uid}")
			print(f"User name: {user.name}")
			print(f"User's photo: {user.photo}")
			print(f"Is user client's friend: {user.is_friend"})
	
		while True:
			if image is not None:
				if __debug__:
					print(f"Image is not None: {image}")
				client.sendRemoteImage(str(image), thread_id=user.uid, thread_type=ThreadType.USER)
			if message is not None:
				if __debug__:
					print(f"Message: {message}")
				client.send(Message(text=str(message)), thread_id=user.uid, thread_type=type)
			if emoji is not None:
				if __debug__:
					print(f"Emoji is not None: {emoji}")
				client.send(Message(text=str(emoji), emoji_size=emoji_size), thread_id=user.uid, thread_type=type)

class SendInLoop(Send):
	def __init__(self, delay):
		self.delay = delay
		
	def send(client, username, type, message=None, image=None, emoji=None,
	emoji_size=None):
		super().send(client, username, type, delay, message, image, emoji, 
		emoji_size)
		time.sleep(self.delay)