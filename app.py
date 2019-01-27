import cowsay
import requests
import sys

def main():
  url = f"http://{sys.argv[1]}.s3.amazonaws.com"

  resp = requests.get(url)

  if resp.status_code == 404:
    cowsay.cow(f"Yay! Domain {sys.argv[1]} is available!!!")
  else:
    cowsay.cow(f"Moo! Domain {sys.argv[1]} is already taken up by some other soul!!!")


if __name__ == "__main__":
  main()
