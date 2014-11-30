from twisted.internet.protocol import Factory
from glapg.protocol import GlapgServerProtocol

class GlapgFactory(Factory):
    # TODO: Implement commands that the factory can handle.
    #commands = {'newchain', new_chain}

    def __init__(self, server):
        self.server = server

    def buildProtocol(self, addr):
        print('buildProtocol %s' % addr)
        return GlapgServerProtocol(self)
