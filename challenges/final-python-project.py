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
            'Denver':'3440', 'Chicago':'3425', 'Portland':'3256', 'Sacremento':'2907', 'Nashville':'2860',
            'Philadelphia':'2812', 'Dallas':'2653', 'Atlanta':'2623', 'New Orleans':'2578', 'Miami':'2534',
            'Boise':'2399'}
    #print(rent_list)

    #average city size dictionary
    pop_size = {'New York City':'8336817', 'Boston':'692600', 'San Francisco':'881549', 'Los Angeles':'3979576',
            'Seattle':'753675', 'San Diego':'1423851', 'San Jose': '1021795', 'Providence':'179883', 'Washington DC':'705749',
            'Denver':'727211', 'Chicago':'2693976', 'Portland':'654741', 'Sacremento':'513624', 'Nashville':'670820',
            'Philadelphia':'1584064', 'Dallas':'2693976', 'Atlanta':'506811', 'New Orleans':'390144', 'Miami':'467963',
            'Boise':'228959'}

    #two bedroom year on year change from August 2021 to August 2022
    percent_change = pop_size = {'New York City':'8336817', 'Boston':'692600', 'San Francisco':'881549', 'Los Angeles':'3979576',
            'Seattle':'753675', 'San Diego':'1423851', 'San Jose': '1021795', 'Providence':'179883', 'Washington DC':'705749',
            'Denver':'-.0101', 'Chicago':'.0988', 'Portland':'.1737', 'Sacremento':'.0906', 'Nashville':'.0043',
            'Philadelphia':'.136', 'Dallas':'.1683', 'Atlanta':'.1359', 'New Orleans':'-.069', 'Miami':'-.1797',
            'Boise':'.0962'}

if __name__ == "__main__":
    main()

