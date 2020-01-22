import tweepy
import time
import board
import pigpio
import busio
import adafruit_tcs34725


# Szenzor eletre keltese #

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

# led #
pi = pigpio.pi()
# Piros beolvasasa
Rs = sensor.color_rgb_bytes[0]
# Zold beolvasasa
Gs = sensor.color_rgb_bytes[1]
# Kek beolvasasa
Bs = sensor.color_rgb_bytes[2]

# ? to int # 

R=int(Rs)
G=int(Gs)
B=int(Bs)


# Consumer API keys #

auth = tweepy.OAuthHandler("TusohUgMPrDqUtk1gJjZqXECV", 
    "EenWi2QfLYYkHo4LYcmvKYl5lkWlDpIYTrtnoCv13kuHOVir7N")
       

# Access token #

auth.set_access_token("1188950735423193089-IBPwf1euXeqYuwfWig7mvmViFZB4pJ", 
    "cgrs5wZncAw1zxPjvau9qZ7YO8b14K4at6yFxeDcPr6av")

api = tweepy.API(auth)    

 

#Lokalisan irom ki

print('Az alabbi szineket olvastuk be. Piros: {} Zold {} Kek {} '.format(R,G,B))


# DEC -> HEX a weboldalhoz # 

if R > 15:
 RX = str(hex(R).lstrip("0x").rstrip("L"))
else:
 RX = str("0"+hex(R).lstrip("0x").rstrip("L"))
if G > 15:
 GX = str(hex(G).lstrip("0x").rstrip("L"))
else:
 GX = str("0"+hex(G).lstrip("0x").rstrip("L"))
if B > 15:
 BX = str(hex(B).lstrip("0x").rstrip("L"))
else:
 BX = str("0"+hex(B).lstrip("0x").rstrip("L"))

#Lokalis HEx link #
  
print('https://www.colorhexa.com/{}{}{} '.format(RX,GX,BX))

#tweet - jelenleg on # 
api.update_status('Uj meres tortent, az alabbi szint olvasta be a szenzor: https://www.colorhexa.com/{}{}{} '.format(RX,GX,BX)) 

#led#
pi.set_PWM_dutycycle(17, R)
pi.set_PWM_dutycycle(22, G)
pi.set_PWM_dutycycle(24, B)
input("Nyomj entert a kilepeshez.") 
