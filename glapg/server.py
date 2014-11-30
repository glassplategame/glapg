#!/usr/bin/env python

from glapg.models import *
from twisted.internet import reactor

class Server(object):
    """
    Holds game-state information.
    """

    def __init__(self):
        self.protocols = set()
        pass

    def client_connected(self, protocol):
        # Add client to game list.
        print(protocol, "joining the game")
        self.protocols.add(protocol)

        # Waiting for game start.
        for protocol in self.protocols:
            protocol.transport.write("%s players waiting" %
                len(self.protocols))

    def client_disconnected(self, protocol):
        self.protocols.remove(protocol)
        print(protocol, "left the game")

    def run(self):
        """
        Start running the server.
        """
        # Initialize the game board.
        self.board = Board()

    def stop(self):
        """
        Stop running the server.
        """
        reactor.stop()
