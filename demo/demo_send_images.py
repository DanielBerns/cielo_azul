from atproto import Client
from sys import argv

def main() -> None:
    if len(argv) != 3:
        raise Exception("We need some arguments")
    client = Client()
    handle = argv[1]
    password = argv[2]
    client.login(handle, password)

    print("Signed in!")
    # replace the path to your image file
    paths = [
        Path("~/projects/bluesky/data/0000.jpg").expanduser(),
        Path("~/projects/bluesky/data/1111.jpg").expanduser(),
        Path("~/projects/bluesky/data/2222.jpg").expanduser()
        ]
    image_alts = ["0000", 
                  "1111", 
                  "2222"
                ]
    images = []
    for path in paths:
        with open(path, 'rb') as f:
            images.append(f.read())
            
    print("Ready to go!")    
    try:
        client.send_images(
            text=f"Post with image from Python {get_timestamp():s}", 
            images=images, 
            image_alts=image_alts
        ) 
        print("Images sent!")
    except Exception as message:
        print("Error", str(message))
    finally:
        print("Done!")

if __name__ == '__main__':
    main()
