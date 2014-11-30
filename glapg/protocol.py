from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.protocols.policies import TimeoutMixin
from twisted.protocols.basic import LineReceiver

class GlapgServerProtocol(object, Protocol, TimeoutMixin):
    """
    The Glass Plate Game Server Protocol
    """
    name = "Guest"

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.server.client_connected(self)

    def connectionLost(self, reason):
        self.factory.server.client_disconnected(self)

    def dataReceived(self, data):
        """ Handle data received from the client. """
        # Parse received data.
        print("Received command '%s' from client" % data)

        # Call the appropriate command.

    def lineReceived(self, line):
        for c in self.factory.clients:
            #print json.loads(line)
            c.sendLine("<{}> {}".format(self.transport.getHost(), line))
