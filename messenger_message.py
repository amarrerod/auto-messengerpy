import time
import sys

from fbchat import Client
from fbchat.models import *
from modes import sendInLoop

def printUsage():
	print("Error!! \n Usage: $python messenger_message email pass delay --<mode>")
	print("Modes: \n")
	print("loop <username> <User || Group> <message> [image_url] [emoji]")

def main(argv):
	if len(argv) < 4:
		printUsage()
	else:
		client = Client(argv[0], argv[1])
		delay = int(argv[2])
		if str(argv[3] == "--loop"):
			if len(argv) < 7:
				printUsage()
				exit(1)
			user = argv[4]
			if str(argv[5]) == "User":
				thtype = ThreadType.USER
			else:
				thtype = ThreadType.GROUP
			message = argv[6]
			image = argv[7] if (len(argv) >= 8) else None
			emoji = argv[8] if (len(argv) >= 9) else None
			sendInLoop(client=client, username=user, type=thtype, delay=delay, message=message, image=image,
			           emoji=emoji,
			           emoji_size=EmojiSize.LARGE)


if __name__ == "__main__":
	main(sys.argv[1:])
