from twisted.internet import reactor
from twisted.internet.endpoints import connectProtocol, TCP4ClientEndpoint
from twisted.internet.protocol import Protocol

class Client(Protocol):
    def sendMessage(self, message):
        self.transport.write(message)

def connect(protocol):
    # Send a message to the glapg server.
    protocol.sendMessage("Hello, world!")

    # Disconnect from the glapg server.
    reactor.callLater(3, protocol.transport.loseConnection)

def main():
    # Connect to the glapg server.
    point = TCP4ClientEndpoint(reactor, "localhost", 1025)
    protocol = connectProtocol(point, Client())
    protocol.addCallback(connect)
    reactor.run()

if __name__ == '__main__':
    main()
