import csv


def find_directors(tconst):
    with open("C:\Mini_Project\IMDB_DB\\title.crew.tsv\\title_crew_data.tsv", "r", encoding='UTF8') as crew:
        crew_list = (csv.DictReader(crew, dialect='excel-tab'))
        for line in crew_list:
            if (line['tconst']==tconst):
                directors = line['directors']
                if (directors!="\\N"):
                    return directors
        return False

if __name__ == '__main__':
            years = range (0,2030)
            print ("Hey")
            with open("C:\\Mini_Project\\IMDB_DB\\title.basics.tsv\\tite_basics_data.tsv", "r", encoding='UTF8') as movies:
                        label_file = "C:\\Mini_Project\\outputs\\movies_with_crew.tsv"
                        with open(label_file, 'w', encoding='utf8', newline='') as tsv_file:
                            movies_list = (csv.DictReader(movies, dialect='excel-tab'))
                            for movie in movies_list:
                                year = movie['startYear']
                                type = movie['titleType']
                                if (year != '\\N' and int(year) < 2030 and (type =='short' or type=='movie')):
                                    crew=find_directors(movie['tconst'])
                                    if (crew!=False):
                                                print ("%s\t%s\t%s\t%s\t%s" % (movie['tconst'],movie['primaryTitle'],movie['titleType'],movie['startYear'],crew), file=tsv_file)
                                                print ("Printed for: "+movie['tconst'])
                            tsv_file.close()
