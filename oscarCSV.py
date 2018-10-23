'''Q3: Write a program that gets the data from the oscar.csv file and figures out
print name of the actor who has more Oscars from the others
print name of the actor who is the oldest actor or actress who got the Oscar, in what year and for what movie
print the name of the actor who got the more than Oscar in row
please note that the CSV file's data are ordered like this ( "Index", "Year", "Age", "Name", "Movie" ).'''

import csv

# function for reading csv file and print actor's name who has more oscars from the others
def maxOscarPrint():
    with open('oscar.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        arrayOfActors=[]
        maxOscar=1
        winnerActor=''
        for row in csv_reader:
            arrayOfActors.append(row[3])
        actorsString=''.join(arrayOfActors)
        for actor in arrayOfActors:
            if actorsString.count(actor)>maxOscar:
                maxOscar=actorsString.count(actor)
                winnerActor=actor
    print("actor who has more oscars from others is : {}".format(winnerActor))
# reading csv file and print oldest actress names and thier movies and the movie year
def oldActorPrint():
    oldActorAge = int(0)
    with open('oscar.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if int(row[2])>oldActorAge:
                oldActorAge=int(row[2])
    with open('oscar.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for item in csv_reader:
            if int(item[2])==oldActorAge:
                print("oldest actor is {} who win oscar in {} for {} movie".format(item[3],item[1],item[4]))

if __name__ == '__main__':
        maxOscarPrint()
        oldActorPrint()




