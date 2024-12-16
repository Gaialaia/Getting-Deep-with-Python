


class Chat:

     def __init__(self, file_name, name=input('Enter your name:')):
         self.name = name
         self.file_name = file_name
         choice = int(input('press 1 to send message 2 to read message'))
         if choice == 1:
            msg = input('enter txt message:')
            with open('chat.txt', 'w') as chat_write:
                chat_write.write(msg)
         elif choice == 2:
            with open('chat.txt', 'r') as chat_write:
                chat_write.read()













ch = Chat()
