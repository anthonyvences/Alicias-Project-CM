import time

chocolateQuantity = 30
caramelQuantity = 9
vanillaQuantity = 27
strawberryQuantity = 99

def scoopicecream(money, tip, service, icecreamquant):
  wallet = 0
  wallet = wallet + money + tip + service + icecreamquant

wallet = 0

usermoney = int(input("Hello, I am Anthony your ice cream scooper today. I can get you ice cream, how much do you have? "))

if usermoney >= 100:
  time.sleep(1)  
  print("HOOOOOOOOOORAY!")
elif usermoney < 100:
  time.sleep(1)  
  print("That's fine too.")

time.sleep(1)

icecreamchoice = str(input('What flavor of ice cream would you like? We have chocolate, caramel, vanilla, and strawberry. '))

time.sleep(1)

icecreamquant = int(input('How much scoops do you want? '))

time.sleep(1)
usertip = int(input('Tip?????????? '))
userservice = 20

if icecreamquant <= 10:
  time.sleep(1)
  print("That's reasonable.")

elif icecreamquant > 10:
    time.sleep(1)
    print("Dang it man.")

if icecreamchoice == 'Chocolate' or 'chocolate':
    if chocolateQuantity >= icecreamquant:
        time.sleep(1)
        print('Here you go, enjoy!')
        wallet += 13
    elif chocolateQuantity < icecreamquant:
      time.sleep(1)
      print('Sorry, come back next time!')
elif icecreamchoice == 'Caramel' or 'caramel':
    if caramelQuantity >= icecreamquant:
      time.sleep(1)
      print('Enjoy your scrumtious ice cream!')
      wallet += 25
    elif caramelQuantity < icecreamquant:
      time.sleep(1)
      print('Nope. Nope. Nope')
elif icecreamchoice == 'Vanilla' or 'vanilla':
    if vanillaQuantity >= icecreamquant:
  #and (icecreamchoice == 'Vanilla' or'vanilla'):
      print('Here ya go!')
      wallet += 92
    if vanillaQuantity < icecreamquant:
      print("BOOHOO, come back next time.")
elif icecreamchoice == 'Strawberry' or 'strawberry':
  if strawberryQuantity >= icecreamquant:
      print("I hope you enjoy our handmade ice cream!")
      wallet =+ 24
  elif strawberryQuantity < icecreamquant:
      print("I'm sorry I wasn't able to make enough ice cream so you could have your share.")
else:
  print("NOOOOOOOO!!!!!!! YOU'RE CANCELLED, GET OUT OF MY SHOP THIS INSTANT.")
print("Anthony's funds $:", wallet)
if wallet <= 10:
  money_money = int(input('I demand more money this instance. Insert money now. '))  
  print("After my wonderful, spectacular service I get this in return?!")
  print(money_money)
if money_money <= 10:
    time.sleep(1)
    print("Wow, talk about being a cheapskate.")
elif money_money > 10:
    time.sleep(1)
    print("Hooray! Let's go. You're an awesome civilian.")
scoopicecream(usermoney, usertip, userservice, icecreamquant)