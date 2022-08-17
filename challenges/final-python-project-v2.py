#!/usr/bin/env python3

#import modules used for this program
import requests
import math

#define url, use 'get' to download the data from website, and print the response 
    #url = "https://www.indexmundi.com/facts/united-states/quick-facts/cities/rank/percent-of-population-under-5"
    #response = requests.get(url)
    #print(response.text)

#define main function
def main():
    
    #average rent for a two bedroom apt. according to https://www.rent.com/research/average-rent-price-report/
    rent_list = {'New York City':'8346', 'Boston':'5795', 'San Francisco':'5060', 'Los Angeles':'5010',
            'Seattle':'4884', 'San Diego':'4305', 'San Jose': '3940', 'Providence':'3691', 'Washington DC':'3478',
            'Denver':'3440', 'Chicago':'3425', 'Portland':'3256', 'Sacramento':'2907', 'Nashville':'2860',
            'Philadelphia':'2812', 'Dallas':'2653', 'Atlanta':'2623', 'New Orleans':'2578', 'Miami':'2534',
            'Boise':'2399'}
    #print(rent_list)

    #average city size dictionary
    pop_size = {'New York City':'8336817', 'Boston':'692600', 'San Francisco':'881549', 'Los Angeles':'3979576',
            'Seattle':'753675', 'San Diego':'1423851', 'San Jose': '1021795', 'Providence':'179883',
            'Washington DC':'705749', 'Denver':'727211', 'Chicago':'2693976', 'Portland':'654741',
            'Sacramento':'513624', 'Nashville':'670820', 'Philadelphia':'1584064', 'Dallas':'2693976', 
            'Atlanta':'506811', 'New Orleans':'390144', 'Miami':'467963', 'Boise':'228959'}

    #two bedroom year on year change from August 2021 to August 2022
    percent_change = {'New York City':'8336817', 'Boston':'692600', 'San Francisco':'881549',
            'Los Angeles':'3979576', 'Seattle':'753675', 'San Diego':'1423851', 'San Jose': '1021795',
            'Providence':'179883', 'Washington DC':'705749','Denver':'-.0101', 'Chicago':'.0988',
            'Portland':'.1737', 'Sacramento':'.0906', 'Nashville':'.0043', 'Philadelphia':'.136', 'Dallas':'.1683',
            'Atlanta':'.1359', 'New Orleans':'-.069', 'Miami':'-.1797', 'Boise':'.0962'}

    #safety index per city year 2022 number 100 being the safest 
    #link is https://www.numbeo.com/crime/region_rankings.jsp?title=2022&displayColumn=1&region=019
    safety_index = {'New York City':'52.93', 'Boston':'63.09', 'San Francisco':'41.41', 'Los Angeles':'50.25',
            'Seattle':'49.54', 'San Diego':'63.29', 'San Jose': '54.42', 'Providence':'68.35',
            'Washington DC':'41.29','Denver':'54.99', 'Chicago':'34.05','Portland':'48.52', 'Sacramento':'51.42',
            'Nashville':'53.95', 'Philadelphia':'37.62', 'Dallas':'49.71','Atlanta':'36.98', 'New Orleans':'34.36',
            'Miami':'47.19', 'Boise':'63.92'}

    while True:
        #get income input and test authenticity
        income = input("What is your current gross income? Please enter a value 10 million USD or less.\n")

        #test int value
        if income.isdigit():
            # convert to an integer
            income= int(income)

        else:
            print("Invalid option! Type a numerical value without commas, decimals, or any other
                    symbols/punctuation marks.")  
            continue  # force the user to restart the while loop

        if income > 10000000:
            print("Income entered is too high!")
            continue
        
        #get the value of rent between 1 - 10 to represent the importance of this parameter
        rent_min = input("What is the minimum rent you will pay?\n")
        rent_min = int(rent_min)
        rent_max = input("What is the maximum rent you can pay?\n")
        rent_max = int(rent_max)
            if rent_min < 0 
                 
                print("Value entered is not valid. Enter a number between 0 and" +rent['New York City'] )
                print("\n")
                continue

        #get the value of population size between 1 - 10 to represent the importance of this parameter
        population_min = input("What is the minimum size population for a city you are willing to live in?\n")
        population
            if population in range(1,10):
                population = int(population)
            else:
                print("Value entered is not valid. Enter a number between 1 and 10.\n")
                continue

        #find the value of the % change of the rent in the last year ranked from 1 - 10
        percent_rent_change = input("What is the value between 1 - 10 for the change of rent in the last
        year?")
            if percent_rent_change in range(1,10):
                percent_rent_change = int(percent_rent_change)
            else:                   
                print("Value entered is not valid. Enter a number between 1 and 10.\n")
                continue
        
        #determine the importance of safety
        safety_index = input("Give the value of safety between 1 - 10")
            if safety_index in range(1,10):
                safety_index = int(safety_index)
            else:
                print("Value entered is not valid. Enter a number between 1 and 10.\n")
                continue

if __name__ == "__main__":
    main()

