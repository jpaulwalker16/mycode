#!/usr/bin/env python3

import csv
#import readlines

def main():

    with open("cars.csv") as carscontents:
        for x in csv.DictReader(carscontents):
            print(x['VIN'])

main()
