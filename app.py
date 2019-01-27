import cowsay
import requests
import sys
import xml.etree.ElementTree as ET

def main():
  url = f"http://{sys.argv[1]}.s3.amazonaws.com"

  resp = requests.get(url)

  if resp.status_code == 404:
    xmldoc = ET.fromstring(resp.content)
    if xmldoc.findall('Code')[0].text == 'NoSuchBucket':
      cowsay.cow(f"Yay! Domain {sys.argv[1]} is available!!!")
    else:
      cowsay.cow(f"Moo! Domain {sys.argv[1]} is already taken up by some other soul!!!")
  else:
    cowsay.cow(f"Moo! Domain {sys.argv[1]} is already taken up by some other soul!!!")


if __name__ == "__main__":
  main()
