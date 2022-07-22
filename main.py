#!/usr/bin/env python3

import requests
import yaml

urls = []
profiles = []
battletags = []

def url_builder():
    with open('battletags.yaml') as f:
        tags = list(yaml.load_all(f, Loader=yaml.FullLoader))
        tags = tags[0]
        for tag in tags:
            url = 'https://ow-api.com/v1/stats/' + tag['platform'] + '/' + tag['region'] + '/' + tag['tag'] + '/profile'
            urls.append(url)
            battletags.append(tag)

def fetch_stats():
    for url in urls:
        profiles.append(requests.get(url).json())
        
def print_ranks():
    counter = 0
    for profile in profiles:
        print('=== ' + battletags[counter]['tag'] + ' ===')
        if not profile['private']:
            for role in profile['ratings']: 
                if role:
                    print('Role: ' + role['role'] + ' - ' + str(role['level']))
            print('Average SR across all three roles: ' + str(profile['rating']))    
        else:
            print('The profile is set to Private or Friends Only')
        print('')
        counter += 1

url_builder()
fetch_stats()
print_ranks()
#print(battletags)
