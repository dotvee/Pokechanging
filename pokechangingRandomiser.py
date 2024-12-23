from random import randint, choice
import csv
#import libraries


regionalEvolvers = ['83','122','211','222','264']
pokechangingShielded = ['Ampharos','Conkeldurr','Golisapod','Ribombee','Skarmory','Tinktaton']
pokechangingLegal = []
pokechangingNotAnymore = []
pokechangingNewFriends = []
loops = 0
formes = 1
regional = 0
removals = 0
target = '0'
#creates/assigns variables and lists to be used later

with open('pokechanginglist.csv') as p:
    for row in csv.reader(p):
        pokechangingLegal.append(row[0])
#adds pokechanginglist.csv's contents to a list

while 3 > removals:
    #while loops until 3 removed pokemon have been picked.
    target = choice(pokechangingLegal)
    #picks a random currently legal pokemon to be removed
    if target not in pokechangingNotAnymore and target not in pokechangingShielded:
        if target in pokechangingShielded:
            print('The substitute took the hit for ',target,'!')
    #checks if the pokemon has already been rolled, or if it has a substitute, if it has one, then it announces it and the user should remove it from pokechangingShielded      
        pokechangingNotAnymore.append(target)
        removals = removals + 1
        #adds valid rolled pokemon to the removal list, and increases removals ticking up to 3

while 6 > loops:
    #while loop loops until 6 pokemon have been generated
    with open('all.csv') as f:
        reader = csv.DictReader(f)
        #opens csv of pokemon information, converted from all.json from nerdydrew's Random-Pokemon-Generator on github using convertcsv.com
        dexNumber = str(randint(1,1025))
        #generates a random national dex number as a string since 'id' is a string
        for row in reader:
            #loops through each row of the CSV
            if row['id'] == dexNumber:
                if row['isNfe'] != 'true' and row['forms/1/name'] != 'Samurott Hisui' and row['name'] not in pokechangingLegal:
                    #if mon isn't an nfe or in the format already, checks if it has a regional forme
                    if row['forms/1/spriteSuffix'] == 'alola' or row['forms/1/spriteSuffix'] == 'galar':
                        if row['id'] not in regionalEvolvers:
                            regional = randint(0, 1)
                    #if the pokemon has a regional forme that isn't an NFE, generates either 1 or 0 to see if the regional variant is what gets added    
                    if regional == 1:
                        pokechangingNewFriends.append(row['forms/1/name'])
                        loops = loops + 1
                        regional = 0
                    #prints regional forme name if forme is added,and the name if otherwise or non-applicable
                    else:
                        pokechangingNewFriends.append(row['name'])
                        loops = loops + 1

print('Removed:')
print(pokechangingNotAnymore)
print('Added:')
print(pokechangingNewFriends)

#prints pokemon that have been added and removed (user adds and removes them from pokechanginglist.csv manually)
    


                        
        




