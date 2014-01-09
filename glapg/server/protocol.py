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
        print self
        self.factory.clients.add(self)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def dataReceived(self, data):
        print data

    def lineReceived(self, line):
        for c in self.factory.clients:
            #print json.loads(line)
            c.sendLine("<{}> {}".format(self.transport.getHost(), line))
