from twisted.internet.protocol import Factory
from glapg.protocol import GlapgServerProtocol

class GlapgFactory(Factory):

    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        print 'buildProtocol %s' % addr
        return GlapgServerProtocol(self)
