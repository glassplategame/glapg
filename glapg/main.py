from glapg.server.factory import GlapgFactory
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol

def main():
    reactor.listenTCP(1025, GlapgFactory())
    reactor.run()

if __name__ == '__main__':
    main()
