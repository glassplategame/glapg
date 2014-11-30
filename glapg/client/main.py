#!/usr/bin/env python

from twisted.internet import reactor
from twisted.internet.endpoints import connectProtocol, TCP4ClientEndpoint
from twisted.internet.protocol import Protocol, ClientFactory

class GlapgProtocol(Protocol):
    def __init__(self, factory):
        self.client = factory.client
        self.factory = factory

    def sendMessage(self, message):
        self.transport.write(message)

    def dataReceived(self, data):
        print("Server said: %s" % data)

class GlapgClientFactory(ClientFactory):
    def __init__(self, client):
        self.clients = set()
        self.client = client

    def startedConnecting(self, connector):
        print("Starting connection")

    def buildProtocol(self, address):
        print("Connected")
        return GlapgProtocol(self)

    def clientConnectionLost(self, connector, reason):
        print("Connection lost: %s" % reason)

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed: %s" % reason)

class Client(object):
    """
    The actual Glass Plate Game Client.
    """
    def __init__(self):
        pass

    def main(self):
        pass

def main():
    # Create Glass Plate Game client.
    client = Client()

    # Connect to the glapg server.
    reactor.connectTCP("localhost", 1025, GlapgClientFactory(client))
    reactor.run()

if __name__ == '__main__':
    main()
