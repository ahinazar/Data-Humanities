import csv
import numpy as np
import json

def country_exists(country,countries):
    for c in countries:
        if (c[0]==country):
            return True
    return False

def find_popularity(tmdb_id,persons):
    for p in persons:
        if (p['id']==tmdb_id):
            return p['popularity']
    return False

if __name__ == '__main__':
    countries=[]
    print ("Hey")
    with open("C:\\Mini_Project\\WIKIDATA_DB\\actresses_countries.tsv", "r", encoding='UTF8') as actress_file:
                actress_list = (csv.DictReader(actress_file, dialect='excel-tab'))
                json1_file = open('C:\\Mini_Project\\TMDB_DB\\person_tmdb.json', "r", encoding='UTF8')
                data = json.load(json1_file)
                json1_file.close()
                type(data)
                index=0
                len=1700
                persons = (data["jsons"])
                for actress in actress_list:
                    country = actress['countryLabel']
                    tmdb_id = int(actress['tmdb_profile'])
                    if (tmdb_id != '\\N' ):
                        popularity =find_popularity(tmdb_id,persons)
                        if (popularity!=False):
                            if (country_exists(country,countries)):
                                for c in countries:
                                    if (c[0]==country):
                                        c[1]=c[1]+1
                                        c[2]=c[2]+popularity
                            else:
                                new = [country, 1, popularity]
                                countries.append(new)
                    print (index/len)
                    index=index+1

                countries = np.array(countries)
                with open("C:\\Users\\DELL\\Documents\\Mini-project\\DataBase\\output.csv", 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    writer.writerow(["country","count","sum of popularity"])
                    for row in range(0, countries.shape[0]):
                        myList = countries[row]
                        writer.writerow(myList)

