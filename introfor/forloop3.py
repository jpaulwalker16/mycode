#!/usr/bin/env python3

#define the array
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

#display invidivual values
for x in farms:
    print("\nThe value of the array is:", x, end="")

