#!/usr/bin/env python3

#channel on tv
print("What type of movie would you like to watch? See selection below:")

#channel options
print("Action - Channels: 1 - 10")
print("Adventure - Channels: 11 - 20")
print("Comedy - Channels: 21 - 30")
print("Crime - Channels: 31 - 40")
print("Romance - Channels: 41 - 50")

#channel input
#channelval = int(input())
#if type(channelval) != int:
#    print("Enter a whole value between 1 - 50")

#channel genre
channelgenre = input()
print("The genre is:", channelgenre)

#channel range genres
channelvaldict = {'action':range(10), 'adventure':range(11-20),'comedy':range(21-30), 'crime':range(31-40), 'romance':range(41-50)}
#convert all inputs to lowercase values
#channelgenre.lower() == channelgenre

#reference to channel genre range values
if channelgenre == "action":
    print(channelvaldict["action"])
elif channelgenre == "adventure":
    print(channelvaldict["adventure"])
elif channelgenre == "comedy":
    print(channelvaldict["comedy"])
elif channelgenre == "crime":
    print(channelvaldict["crime"])
elif channelgenre == "romance":
    print(channelvaldict["romance"])
else:
    print("Choose one of the five valid movies genres")



#if channelval in range(10)
 #   print("Action")
  #  print(channelval(

