#!/usr/bin/env python3

#download the book Dracula by Bram Stoker
#wget ("https://www.gutenberg.org/files/345/345-0.txt") -qO dracula.txt
counter = 0
#open and read content
with open("dracula.txt", "r") as dracula_content:
    with open("vampytimex.txt","w") as transylvania:
        for line in dracula_content:
            if "vampire" in line.lower():
                print(line)
                counter = counter + 1
                transylvania.write(line)

print(counter)
    

