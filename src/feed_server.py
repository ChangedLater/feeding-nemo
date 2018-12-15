
import logging
from time import sleep
from datetime import datetime, timedelta
import socket
import sys
import RPi.GPIO as GPIO
import motor
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

lastfed = datetime.now()
x = 0
listening = False

def main():
    global listening
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
     
    try:
        s.bind(('', 8888))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
    s.settimeout(60)
    s.listen(1)
    while True:
        if((datetime.now() - lastfed) > timedelta(hours = 36)):
            feed()
        print('Waiting for a connection')
        #wait to accept a connection - blocking call
        try:
          conn, addr = s.accept()
          print("connection made")
          conn.sendall(str.encode("response from python"))
          print("data sent")
          chunk = conn.recv(2048)
          data = chunk.decode('utf-8')
          print(data)
          conn.close()
          should_feed(data)
        except socket.timeout:
          pass

def should_feed(data):
  if((datetime.now() - lastfed) > timedelta(hours = 18)):
    feed();
  elif data.find('SomePassword') != -1:
    feed();
    
def feed():
  print("feeding started")
  global lastfed
  lastfed = datetime.now()
  servo = motor.create(17)
  servo.start()
  servo.moveTo(90)
  sleep(1)
  servo.moveTo(-90)
  sleep(1)
  servo.close()
  Path('/var/www/html/robots.txt').touch()

if __name__ == '__main__':
    main()
