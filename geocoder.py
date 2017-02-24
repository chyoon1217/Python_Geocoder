import csv
import time
import requests
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Geocoding an address
# geocode_result = gmaps.geocode('Google, Sydney, Australia')
# result_geometry = geocode_result;
# print(result_geometry);

with open('address.csv', 'r', encoding='utf-8') as csvfile:
    addressreader = csv.reader(csvfile)
    for row in addressreader:
        geocode_result = gmaps.geocode(row);
        try:
            result_geometry = geocode_ressult[0]['geometry']['location'];
            resultstr = str(result_geometry['lng']) + ',' + str(result_geometry['lat']) + '\n'
            print(row)
            print(resultstr)
            with open("coords_result.txt", "a") as myfile:
                myfile.write(resultstr)
            time.sleep(1)
        except IndexError as e:
            print(row)
            print(e)
            with open("coords_result.txt", "a") as myfile:
                myfile.write('failed\n')
            with open("failed.txt", "a") as failedFile:
                failedString = str(row) + '\n'
                failedFile.write(failedString)
