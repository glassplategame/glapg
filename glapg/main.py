#!/usr/bin/env python

from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol

from glapg.server import Server
from glapg.factory import GlapgFactory

def main():
    # Start Glass Plate Game server.
    print("Starting Glass Plate Game Server object")
    server = Server()
    reactor.callWhenRunning(server.run)

    # Begin listening for connections.
    print("Listening for connections")
    reactor.listenTCP(1025, GlapgFactory(server))
    reactor.run()

if __name__ == '__main__':
    main()
