import json
import xlrd #if throws error, please do :
            # File -> Settings -> Project: Mini_Project -> Project Interpreter -> Install xlrd


if __name__== '__main__':

    print("Starting to get popularity json file...")

    total_popularity = 0
    females_popularity = 0
    males_popularity = 0
    persons_counter = 0
    women_counter = 0
    men_counter = 0
    top_pop = []
    tmdb_profile_humens_list = []

    print("Getting details from db.xlsx...")
    ExcelFileName = 'actress_popp.xlsx'
    workbook = xlrd.open_workbook(ExcelFileName)
    worksheet = workbook.sheet_by_name("actress_pop")

    for i in range(1, 1586):
        tmdb_profile_humens_list.append(worksheet.cell(i, 2).value)

    print("Getting details from person_tmdb.json...")

    with open('person_tmdb.json','r',encoding='UTF8') as person_tmdb:
        data = json.load(person_tmdb)
        for person in data["jsons"]:
            persons_counter=persons_counter+1
            total_popularity = total_popularity + person["popularity"]
            if(person["id"] in tmdb_profile_humens_list):
                women_counter = women_counter + 1
                females_popularity = females_popularity + person["popularity"]
                tmdb_profile_humens_list.remove(person["id"])
                if((person["popularity"] > 8) and (person["adult"] == False)):
                    top_pop.append(person)
            else:
                males_popularity = males_popularity + person["popularity"]

    print("Calculating data...")
    men_counter = total_popularity - women_counter
    males_popularity = males_popularity / men_counter
    females_popularity = females_popularity / women_counter
    total_popularity = total_popularity / persons_counter
    top_pop = sorted(top_pop,key = lambda i:i["popularity"],reverse=True)

    print("Creating data.json file...")
    with open('popularity_men.json', 'w') as outfile:
        output = {'total': total_popularity, 'females': females_popularity, 'males':males_popularity ,'top_popularity': top_pop }
        json.dump(output,outfile, indent=4)

    print("Done!")