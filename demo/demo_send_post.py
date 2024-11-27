from atproto import Client
from sys import argv
from utils import get_timestamp

def main() -> None:
    if len(argv) != 3:
        raise Exception("We need some arguments")
    client = Client()
    handle = argv[1]
    password = argv[2]
    client.login(handle, password)
    client.send_post(text=get_timestamp())

if __name__ == '__main__':
    main()
