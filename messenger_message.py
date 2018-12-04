import time
import sys
import argparse
from fbchat import Client
from fbchat.models import *
from modes import SendInLoop

USER = "user"
GROUP = "group"

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Message automatisation in Python")
	parser.add_argument("email", help="user email")
	parser.add_argument("password", help="user password")
	parser.add_argument("delay", help="delay between each message")
	parser.add_argument("receiver", help="user who will receive the message")
	parser.add_argument("message", help="message to send")
	parser.add_argument("receiver_type", help="specify if the receiver is an user or a group")
	parser.add_argument("--image", help="add an image to the message")
	parser.add_argument("--emoji", help="add an emoji to the message")
	args = parser.parse_args()
	client = Client(args.email, args.password)
	delay = int(args.delay)
	sender = SendInLoop(delay)
	message = args.message
	receiver = args.receiver
	receiver_type = args.receiver_type.lower()
	thread_type = None
	if receiver_type == USER:
		thread_type = ThreadType.USER
	elif receiver_type == GROUP:
		thread_type = ThreadType.GROUP
	else:
		raise Exception("Error, receiver is it not an user or a group")
	image = args.image | None
	emoji = args.emoji | None
	sender.send(client=client, username=receiver, type=thread_type, 
	message=message, image=image, emoji=emoji, emoji_size=EmojiSize.LARGE)

