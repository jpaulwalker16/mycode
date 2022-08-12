#!/usr/bin/env python3

import csv
#import readlines

def main():

    #open file to read contents
    carscontents = open("cars.csv","r")
    #if f.mode == "r":
    #    carscontents = f.read() 
        #print(carscontents)

#read off the first three lines of data and separate them
    first3lines = carscontents.readline().split(",")
        print("Enter in which contents you want listed or enter in any data you have about what car you are looking up; see the following choices")
    for x in first3lines:
        print(x)
        
    with open("cars.csv") as carscontents:
        for x in csv.DictReader(carscontents):
            print(x[VIN])

if __name__== "__main__":
    main()


#URL= "https://raw.githubusercontent.com/csfeeser/Python/master/data%20sets/cars.csv" 

#Getting the data from that url
#carsdata = requests.get(URL)

#reading data out
#carsread = carsdata.read()


