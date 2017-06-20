from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import time
clients = []
to = time.time()
class SimpleChat(WebSocket):
    
    def handleMessage(self):
       for client in clients:
          if client != self:
             client.sendMessage(self.address[0] + u' - ' + self.data)

    def handleConnected(self):
       print(self.address, 'connected')
       for client in clients:
          global to
          t1 = time.time()
          timediff = (int(t1)-int(to))/5
          print(timediff)
          with open("out_" + str(timediff) + ".txt",'r') as f:
              for line in f:
#    print (line)
                  sentence = line.split(' ')
                  with open('tech_words', 'r') as myfile:
                      techs=myfile.read().replace('\n',' ')
                  with open('nonNoun.txt', 'r') as myfile1:
                      nontechs=myfile1.read().replace('\n',' ')

                  stupid = 'NNNNFFDMMSMSS'

                  mySet = {stupid}

                  for word in sentence:
                      mySet.add(word)

                  Final = {stupid}

                  for word in mySet:
                      if not (word in nontechs):
                          Final.add(word)

                  sz = len(Final)

                  pp = {stupid}
                  for word in Final:
                          pp.add(word)

                  for word in pp:
                      if word in techs:
                          Final.add(word)


              for word in Final:
                  if not (word == stupid):
                      print (word)
                      client.sendMessage(unicode(word))
                      break


# client.sendMessage("" + u'animal')
       clients.append(self)

    def handleClose(self):
       clients.remove(self)
       print(self.address, 'closed')
       for client in clients:
          client.sendMessage(self.address[0] + u' - disconnected')

print (to)
server = SimpleWebSocketServer('', 8765, SimpleChat)
server.serveforever()
