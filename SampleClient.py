import signal

from core.client_core import ClientCore

my_p2p_client = None

def signal_handler(signal, frame):
    print('sc1 signal_handler')
    shutdown_client()

def shutdown_client():
    print('sc1 shutdown_client')
    global my_p2p_client
    my_p2p_client.shutdown()

def main():
    print('sc1 main')
    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_client
    my_p2p_client = ClientCore(50095, '192.168.10.104', 50082)
    my_p2p_client.start()


if __name__ == '__main__':
    main()