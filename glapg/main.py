from glapg.server.factory import GlapgFactory
from twisted.internet import reactor


def main():
    reactor.listenTCP(1025, GlapgFactory())
    reactor.run()

if __name__ == '__main__':
    main()

