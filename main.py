#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd7in5
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import requests
from io import BytesIO

EVERY = 2000

try:
    epd = epd7in5.EPD()
    epd.init()
    print("Clear")
    epd.Clear(0xFF)
    
    print "read bmp file"

    while True:
      response = requests.get(url)
      img = Image.open(BytesIO(response.content))

      starttime=time.time()
      Himage = Image.open('7in5.bmp')
      epd.display(epd.getbuffer(Himage))
      epd.sleep()
      time.sleep(EVERY - ((time.time() - starttime) % EVERY))
        
except:
    print "nis"
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
    exit()

