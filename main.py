import csv 

#answering the question of what is the ideal size to become an NBA player
print('Best physical dimensions to have as a basketball player-\n')
index=0
i=0
weight=[]
height=[]
sum1=0
sum2=0

with open("all_seasons.csv", newline="") as csv_file:
  csv_reader= csv.reader(csv_file, delimiter=',')
  
  for index,playerName,teamAbbreviation,age,playerHeight,playerWeight,college,country,draftYear,draftRound,draftNumber,gp,pts,reb,ast,netRating,orebPct,drebPct,usgPct,tsPct,astPct,season in csv_reader:
   if i != 0:
     
      
       sum1= float(sum1)+float(playerHeight)
       sum2=float(sum2)+float(playerWeight)
      
   i+=1

average1=float(sum1)/float(i)
average2=float(sum2)/float(i)
print("The average basketball height amoung basketball players is " + str(average1)+ "cm")
print("\n"+"The average weight of a basketball player is "+ str(average2)+" kilograms.\n")

index=0
i=0
NameofAH=[]


with open("all_seasons.csv", newline="") as csv_file:
  csv_reader= csv.reader(csv_file, delimiter=',')
  for index,playerName,teamAbbreviation,age,playerHeight,playerWeight,college,country,draftYear,draftRound,draftNumber,gp,pts,reb,ast,netRating,orebPct,drebPct,usgPct,tsPct,astPct,season in csv_reader:
   if i != 0:
     #print (index,playerName,playerHeight)
     if float(playerHeight) > 162.00 and float(playerHeight) < 176.00:
      NameofAH.append(playerName)
      
      
   i+=1

nameSet =set(NameofAH)

print("The players with height anomalies include: ")
print(nameSet)

index=0
i=0
NameofAW=[]


with open("all_seasons.csv", newline="") as csv_file:
  csv_reader= csv.reader(csv_file, delimiter=',')
  for index,playerName,teamAbbreviation,age,playerHeight,playerWeight,college,country,draftYear,draftRound,draftNumber,gp,pts,reb,ast,netRating,orebPct,drebPct,usgPct,tsPct,astPct,season in csv_reader:
   if i != 0:
     #print (index,playerName,playerHeight)
     if float(playerWeight) > 60.00 and float(playerWeight) < 70.00:
      NameofAW.append(playerName)
      
      
   i+=1
nameSet1 =set(NameofAW)
print("\n" )
print("The players with weight anomalies include: ")
print(nameSet1)


#answering the question of what college has the best basketball culture
print("\n\n\nColleges and number of players that went there-\n")

colleges=[]
collegeValues=[]
index2=0
with open('all_seasons.csv', newline="") as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  
  for index,playerName,teamAbbreviation,age,playerHeight,playerWeight,college,country,draftYear,draftRound,draftNumber,gp,pts,reb,ast,netRating,orebPct,drebPct,usgPct,tsPct,astPct,season in csv_reader:
    if index2>0:
      if colleges.count(college)==0:
        colleges.append(college)
        
    index2+=1;
        
        
  csv_file.seek(0)
  index2=0
  
  for i in range (0,len(colleges)):
    collegeValues.append(0)
    
  for index,playerName,teamAbbreviation,age,playerHeight,playerWeight,college,country,draftYear,draftRound,draftNumber,gp,pts,reb,ast,netRating,orebPct,drebPct,usgPct,tsPct,astPct,season in csv_reader:
    if index2>0:
      collegeValues[colleges.index(college)]+=1
    index2+=1
greatestIndex=0
currGreatest=0;      
for i in range(0,len(colleges)):
  print(str(colleges[i])+': '+str(collegeValues[i])+' players')

for i in range(0,len(collegeValues)):
  if collegeValues[i]>currGreatest and (colleges[i]=='None')==False:
    currGreatest=collegeValues[i]
    greatestIndex=i
print("\nThe college with the best basketball culture is "+colleges[greatestIndex]+" with " + str(currGreatest)+" people from there going to the NBA")



#Answering the question of how NBA scoring changed over time
print("\n\n\nNBA offenses and their evolution over time (PPG means Points Per Game)\n")
index3 = 0

# Finds the average points scored per game by each player in each season
sn = '1996-97'
index2 = 0
avg = 0
avg_list = []
with open ('all_seasons.csv', newline="") as csv_file:
  csv_reader=csv.reader(csv_file, delimiter=',')
  for index, playerName, teamAbbreviation, age, playerHeight, playerWeight, college, country, draftYear, draftRound, draftNumber, gp, pts, reb, ast, netRating, orebPct, drebPct, usgPct, tsPct, astPct, season in csv_reader:
    if index2 !=0:
      avg = avg + float(pts)
      if sn != season:
        if season == '1997-98':
          print('1996-97' + ":")
        avg = round(avg / (index3-1), 1)
        print(str(avg) + " PPG")
        print(season + ":")
        avg_list.append(avg)
        sn = season
        avg = 0
        index3 = 0
    index2 = index2 + 1
    index3 = index3 + 1
avg = round(avg / (index3-1), 1)
print(str(avg) + " PPG")
avg_list.append(avg)

print(" ")

# Finds the most average points scored per game by each player in a season
max = 0
for x in avg_list:
  if x > max:
    max = x
print ("Most average PPG per player in a season was: " + str(max))

print("")

# Finds the least aver points scored per game by each player in a season
min = 10
for x in avg_list:
  if x < min:
    min = x
print ("Least PPG per player in a season was: " + str(min))

print(" ")

# Finds the average PPG scored by each player per season
avg = 0
index = 0
for x in avg_list:
  avg = avg + x
  index = index + 1
avg = round(avg/index, 1)
print ("Average PPG scored by each player per season is: " + str(avg))