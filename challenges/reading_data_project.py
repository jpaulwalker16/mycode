#!/usr/bin/env python3

import csv
#import readlines

#defining the main function for the program
def main():

    #open file to read contents
    with open("cars.csv","r") as carscontents:

#read off the first three lines of data and separate them
        datatitles = carscontents.readline().split(",")

#split off the rest of the lines of data and separate them
        datacontent = carscontents.readlines()[1:]  # readlines converts a fileobj to a list, so the split is redundant
        #ask for input on data points
        answer = input("Welcome to cars.com! Do you have any specific data point on your vehicle?   (y/n)")
        print("\n")
        if answer.lower() == "y":

            #give the following choices for data points
            print("Here are the following choices:\n")
            for a,b,c in zip(datatitles[::3],datatitles[1::3],datatitles[2::3]):
                print('{:<30}{:<30}{:<}'.format(a,b,c))

            #ask for input of a category
                answer1 = input("Input a parameter to list all the vehicles with that information.\n")
                with open("cars.csv","r") as carscontents1:
                  #for x in csv.DictReader(carscontents1):

                  #search each line for the answer1 content and print out the whole line
                    c = datacontent.search(answer1)
                    if c:
                        print(c[answer1])

           # print("Here are the following choices:")
           # for a,b,c in zip(datatitles[::3],datatitles[1::3],datatitles[2::3]):
           #         print('{:<30}{:<30}{:<}'.format(a,b,c))

       #print the following categories of choices    
        else:
            print("Here are the following choices:\n")
            for a,b,c in zip(datatitles[::3],datatitles[1::3],datatitles[2::3]):
                print('{:<30}{:<30}{:<}'.format(a,b,c))
                    
        # vertically
        #for x in datatitles:
           # print(x)

        # horizontally
        #print(" ".join(datatitles))
        #if answer2 in datatitles:
    with open("cars.csv","r") as carscontents2:
        for x in csv.DictReader(carscontents2):
                print(x[answer2])

if __name__== "__main__":
    main()


#URL= "https://raw.githubusercontent.com/csfeeser/Python/master/data%20sets/cars.csv" 

#Getting the data from that url
#carsdata = requests.get(URL)

#reading data out
#carsread = carsdata.read()


