import csv
import numpy as np

def find_male(director):
    with open("C:\\Mini_Project\\WIKIDATA_DB\\male_screenwriters.tsv", "r", encoding='UTF8') as men_director:
        male_dir_list = (csv.DictReader(men_director, dialect='excel-tab'))
        for male in male_dir_list:
            if (male['imdb_profile'] == director):
                return True
        return False

def is_male_writer(writers):
        for writer in writers:
            if (find_male(writer)==True):
                return True
        return False

def find_writer(tconst,crew_list):
        for ro+w in crew_list:
                if (row['tconst']==tconst):
                        writers = row['writers']
                        if (writers!="\\N"):
                            writers_list = writers.split(',')
                            result= is_male_writer(writers_list)
                            if (result==False):
                                return False
                            else:
                                return True
                        else:
                            return False
        return False

if __name__ == '__main__':
    years = range (0,2030)
    counter = []
    print ("Hey")
    for year in years:
        counter.append('0')
    with open("C:\\Mini_Project\\IMDB_DB\\title.basics.tsv\\tite_basics_data.tsv", "r", encoding='UTF8') as movies:
        with open("C:\Mini_Project\IMDB_DB\\title.crew.tsv\\title_crew_data.tsv", "r", encoding='UTF8') as crew:
                crew_list = (csv.DictReader(crew, dialect='excel-tab'))
                movies_list = (csv.DictReader(movies, dialect='excel-tab'))
                index=0
                for movie in movies_list:
                    year = movie['startYear']
                    type = movie['titleType']
                    if (year != '\\N' and int(year) < 2030 and (type == 'short' or type == 'movie')):
                        writer=find_writer(movie['tconst'],crew_list)
                        if (writer!=False):
                            print(movie['tconst']," ",writer)
                            counter[(int(year))] = int(counter[(int(year))]) + 1


                counter = np.array(counter)
                with open("C:\\Users\\DELL\\Documents\\Mini-project\\DataBase\\output.csv", 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    for row in range(0, counter.shape[0]):
                        myList = []
                        myList.append(counter[row])
                        writer.writerow(myList)

