#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import socket
import json
import urllib
import Adafruit_CharLCD as LCD
import subprocess



#channel id and API key
channel_id = "<YOUR_CHANNEL_ID>" # channel id
api_key = "<YOUR_API_KEY>"
lookup_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCRmjIoVeHAERre3UNSiPQ_g&key=<YOUR_API_KEY>"

#Change brightness here
brightness_setting = 8 # I hate bright lights
# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)



def is_connected():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

while True:
    try:
        lcd.clear()
        # Catches the webpage from google   
        soup = urllib.urlopen(lookup_url)
        markup = soup.read()
                    
        # Access the part of the JSON object that we care about
        feed_json = json.loads(markup)
        sub_count = feed_json["items"][0]["statistics"]["subscriberCount"]
        view_count = feed_json["items"][0]["statistics"]["viewCount"]
        lcd.message("Abonnes : " + sub_count + "\nVues : " + view_count)
        time.sleep(10)
    except KeyError:
        print("bug")
        subprocess.call(["/usr/bin/python", "abo_count_liquidcristal.py"])
