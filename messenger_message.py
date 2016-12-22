import fbchat
import time
import sys

def main(argv):
    print argv
    if len(argv) < 3:
        print ("Error!! \n Usage: $python messenger_message userID pass time [url image]")
    else:
        imgSet = False
        imgURL = ""
        if len(argv) == 4:
            print "Se ha definido una imagen"
            imgSet = True
            imgURL = argv[3]

        identifier = argv[0]
        password = argv[1]
        delay = int(argv[2])
        friend = raw_input("Friend: ")
        message = raw_input("Message: ")
        client = fbchat.Client(identifier, password)
        friends = client.getUsers(friend)
        friend = friends[0]
        while True:
            if imgSet:
                client.sendRemoteImage(friend.uid, message=message, image = imgURL)
            else:
                sent = client.send(friend.uid, message)
                if sent:
                    print ("Message sent sucessfully!")
            time.sleep(delay)




if __name__ == "__main__":
    main(sys.argv[1:])
