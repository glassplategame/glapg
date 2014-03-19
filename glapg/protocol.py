from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.protocols.policies import TimeoutMixin
from twisted.protocols.basic import LineReceiver

(STATE_UNAUTHENTICATED, STATE_AUTHENTICATED) = range(2)

class GlapgServerProtocol(object, Protocol, TimeoutMixin):
    """
    The Glass Plate Game Server Protocol
    """

    state = STATE_UNAUTHENTICATED

    def __init__(self, factory):
        self.handlers = {
            0x00: self.ping
        }
        self.factory = factory

    def ping(self):
        pass

    def connectionMade(self):
        print self, "connected."
        self.factory.clients.add(self)

    def connectionLost(self, reason):
        print self, "disconnected."
        self.factory.clients.remove(self)

    def dataReceived(self, data):
        print data

    def lineReceived(self, line):
        for c in self.factory.clients:
            #print json.loads(line)
            c.sendLine("<{}> {}".format(self.transport.getHost(), line))

    def chain_new():
        """
        Create a new chain.
        """
        pass

    def branch_new():
        """
        Create a new branch.
        """
        pass

    def permit():
        """
        Permit a move.
        """
        pass

    def challenge():
        """
        Challenge a move.
        """
        pass

    def away():
        """
        Set player as being away.
        """
        pass

    def blank():
        """
        Void a move.
        """
        pass

    def quit():
        """
        Have the player quit the game.
        """
        pass

    def okay():
        """
        Okay the player's move.
        """
        pass

    def message():
        """
        Send a message from one player to another.
        """
        pass

    def kick():
        """
        Kick a player from the game.
        """
        pass

    def game_end():
        """
        End the game.
        """
        pass

    def game_new():
        """
        Create a new game.
        """
        pass

    def silence():
        """
        Mute the specified player.
        """
        pass

    def pause():
        """
        Pause the game.
        """
        pass

    def join():
        """
        Have a player join the specified game.
        """
        pass

    def connect():
        """
        Have a player connect to the specified server.
        Already implemented by the Twisted overload?
        """
        pass

    def disconnect():
        """
        Have a player disconnect from the specified server.
        """
        pass

    def name_set():
        """
        Set the player's name to the specified name.
        """
        pass

