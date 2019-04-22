import requests
from datetime import datetime
 
# getting current date and time, this is in UTC format
d = datetime.today()

# getting current year
currentYear = d.year
 
#getting current month
currentMonth = d.month
 
#getting current day
currentDay = d.day


# click fix
url = "https://chelseama.ogopendata.com/datastore/odata3.0/50fd4973-d1c9-4897-8b7d-092a87ebc23b?&$top=5000000&$format=json"
r = requests.get(url)
clickFix = r.json()

# theft data
url2 = "https://chelseama.ogopendata.com/datastore/odata3.0/fceb31a5-3ebc-48de-baf6-979cf53b7e2b?&$top=5000000&$format=json"
r = requests.get(url2)
r2 = r.json()
theft = r2['value']

def other_scores():
  other = [row for row in clickFix['value'] if "other" in row['Category'].lower()]

  for row in other:
    if (row['Closed Date'] is not None):
       row['Closed Date'] = datetime.strptime(row['Closed Date'], '%m/%d/%Y')
    else:
      row = None
  scores_year = []
  other_year = [row for row in other if (row['Closed Date'] is not None and row['Closed Date'].year == currentYear)]

  for row in other_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_year.append(1)
    else:
      scores_year.append(0)

  other_month = [row for row in other if (row['Closed Date'] is not None and row['Closed Date'].month == currentMonth - 1)]
  scores_month = []
  for row in other_month:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_month.append(1)
    else:
      scores_month.append(0)

  scores_day = []
  for index in range(len(other_month) - 3, len(other_month)):
    row = other_month[index]
    if (closed_days < 7):
      scores_day.append(1)
    else:
      scores_day.append(0)

  other_score_year = round(sum(scores_year) / len(scores_year), 3)
  other_score_month = round(sum(scores_month) / len(scores_month), 3)
  other_score_day = round(sum(scores_day) / len(scores_day), 3)

  return ("All Fix On Time %", other_score_day, other_score_month, other_score_year)

def graffiti_scores():

  graffiti = [row for row in clickFix['value'] if "graffiti" in row['Category'].lower()]

  for row in graffiti:
    if (row['Closed Date'] is not None):
      row['Closed Date'] = datetime.strptime(row['Closed Date'], '%m/%d/%Y')
    else:
      row = None
  
  scores_year = []
  graffiti_year = [row for row in graffiti if (row['Closed Date'] is not None and row['Closed Date'].year == currentYear)]

  for row in graffiti_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_year.append(1)
    else:
      scores_year.append(0)
  
  scores_month = []
  graffiti_month = [row for row in graffiti if (row['Closed Date'] is not None and row['Closed Date'].month == currentMonth - 1)]

  for row in graffiti_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_month.append(1)
    else:
      scores_month.append(0)

  scores_day = []
  
  for index in range(len(graffiti_month) - 3, len(graffiti_month)):
    row = graffiti_month[index]
    closed_days = float(row['Days to Closed'])
    if (closed_days < 14):
      scores_day.append(1)
    else:
      scores_day.append(0)
  
  graffiti_score_year = round(sum(scores_year) / len(scores_year), 3)
  graffiti_score_month = round(sum(scores_month) / len(scores_month), 3)
  graffiti_score_day = round(sum(scores_day) / len(scores_day), 3)

  # print("Graffiti On Time %", graffiti_score_day, graffiti_score_month, graffiti_score_year)

  return ("Graffiti On Time %", graffiti_score_day, graffiti_score_month, graffiti_score_year)

  
    

def street_light_scores():
  
  street_lights = [row for row in clickFix['value'] if "street light" in row['Category'].lower()]

  for row in street_lights:
    if (row['Closed Date'] is not None):
      row['Closed Date'] = datetime.strptime(row['Closed Date'], '%m/%d/%Y')
    else:
      row = None
  
  scores_year = []
  street_light_year = [row for row in street_lights if (row['Closed Date'] is not None and row['Closed Date'].year == currentYear)]

  for row in street_light_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 14):
      scores_year.append(1)
    else:
      scores_year.append(0)
  
  scores_month = []
  street_light_month = [row for row in street_lights if (row['Closed Date'] is not None and row['Closed Date'].month == currentMonth - 1)]

  for row in street_light_month:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 14):
      scores_month.append(1)
    else:
      scores_month.append(0)
  
  scores_day = []
  for index in range(len(street_light_month) - 3, len(street_light_month)):
    row = street_light_month[index]
    closed_days = float(row['Days to Closed'])
    if (closed_days < 14):
      scores_day.append(1)
    else:
      scores_day.append(0)

  street_light_score_year = round(sum(scores_year) / len(scores_year), 3)
  street_light_score_month = round(sum(scores_month) / len(scores_month), 3)
  street_light_score_day = round(sum(scores_day) / len(scores_day), 3)

  return ("Street Light On Time %", street_light_score_day, street_light_score_month, street_light_score_year)

def trash_scores():

  trash = [row for row in clickFix['value'] if "trash" in row['Category'].lower()]
  
  for row in trash:
    if (row['Closed Date'] is not None):
      row['Closed Date'] = datetime.strptime(row['Closed Date'], '%m/%d/%Y')
    else:
      row = None
  scores_year = []
  trash_year = [row for row in trash if (row['Closed Date'] is not None and row['Closed Date'].year == currentYear)]
  for row in trash_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_year.append(1)
    else:
      scores_year.append(0)
  
  trash_month = [row for row in trash if (row['Closed Date'] is not None and row['Closed Date'].month == currentMonth - 1)]
  scores_month = []

  for row in trash_month:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_month.append(1)
    else:
      scores_month.append(0)

  scores_day = []
  for index in range(len(trash_month) - 3, len(trash_month)):
    row = trash_month[index]
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_day.append(1)
    else:
      scores_day.append(0)
  
  trash_score_year = round(sum(scores_year) / len(scores_year), 3)
  trash_score_month = round(sum(scores_month) / len(scores_month), 3)
  trash_score_day = round(sum(scores_day) / len(scores_day), 3)

  return ("Missed Trash On Time %", trash_score_day, trash_score_month, trash_score_year)



def pothole_scores():
  potholes = [row for row in clickFix['value'] if row['Category'] == 'Pothole']

  for row in potholes:
    if (row['Closed Date'] is not None):
      row['Closed Date'] = datetime.strptime(row['Closed Date'], '%m/%d/%Y')
    else:
      row = None

  # gets the pothole incidents with year 2019
  scores_year = []
  potholes_year = [row for row in potholes if (row['Closed Date'] is not None and row['Closed Date'].year == currentYear)]
  for row in potholes_year:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_year.append(1)
    else:
      scores_year.append(0)


  potholes_month = [row for row in potholes if (row['Closed Date'] is not None and row['Closed Date'].month == currentMonth - 1)]
  scores_month = []
  for row in potholes_month:
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_month.append(1)
    else:
      scores_month.append(0)

  scores_day = []
  for index in range(len(potholes_month) - 5, len(potholes_month)):
    row = potholes_month[index]
    closed_days = float(row['Days to Closed'])
    if (closed_days < 7):
      scores_day.append(1)
    else:
      scores_day.append(0)

  pothole_scores_year = round(sum(scores_year) / len(scores_year), 3)
  pothole_scores_month = round(sum(scores_month) / len(scores_month), 3)
  pothole_scores_day = round(sum(scores_day) / len(scores_day), 3)

  return ("Pothole On Time %", pothole_scores_day, pothole_scores_month, pothole_scores_year)


  # print("pothole year:", pothole_scores_year)
  # print("pothole month:", pothole_scores_month)
  # print("pothole day:", pothole_scores_day)

    
def current_robbing_street_score():
    ''' Name of the function:
        Parameters: Fixed parameters include the historic data, which has a yearly avg of 131.667, monthly avg or 10.9722 or a daily avg or .36073
        Computation: Based on the data provided in the API, I subtract a year from the current day to calculate the year score, subtract a month - currentday for the month score and 24 hours - current day for the day score.
        Returns: Tuple with day, month and year score
        '''
    #calculate year score, this will be done by taking into consideration data from today's date - 1 year
    
    #calculating year score
    YearScore = []
    for row in theft:
        #think about edge case January
        month,day,year = str(row['Date']).split('/')
        if ('Robbery - Street' in row['Type']):
            if(int(year)  == currentYear):
                YearScore.append(1)
            elif(int(year) == currentYear - 1 and int(month) > currentMonth):
                YearScore.append(1)
            elif(int(year) == currentYear - 1 and int(month) >= currentMonth and int(day) >= currentDay):
                YearScore.append(1)
    #print(YearScore)
    #total number of robbings this year
    TotalNumberOfRobbingYear = len(YearScore)
    finalYearScore = 131.667/TotalNumberOfRobbingYear
    #print(finalYearScore)

    #calculating month score, information is outdated the months score can't be calculated
    MonthScore = []
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Robbery - Street' in row['Type']):
            if(int(year)  == currentYear and int(month) == currentMonth):
                MonthScore.append(1)
            #edge case if it's January
            elif(int(year) == currentYear - 1 and int(month) == 12 and currentMonth == 1 and int(day) >= currentDay):
                MonthScore.append(1)
            elif(int(year) == currentYear and int(month) == currentMonth -1 and int(day) >= currentDay):
                MonthScore.append(1)
    #total number of robbings this year
    TotalNumberOfRobbingMonth = len(MonthScore)
    if TotalNumberOfRobbingMonth != 0:
        finalMonthScore = 10.9722/TotalNumberOfRobbingMonth
    else:
        finalMonthScore = 0
    #print(finalMonthScore)
    #calculating the day score will be yesterdays score.
    #dictDay is a key value pair with months per day
    dictDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,11:30, 12:31}
    DayScore = []
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Robbery - Street' in row['Type']):
            if(int(year) == currentYear and int(month) == currentMonth and int(day) == currentDay -1):
                DayScore.append(1)
            elif(int(year) == currentYear -1 and int(month) == 12 and currentDay == 1 and int(day) == 31 and currentMonth == 1):
                DayScore.append(1)
                #calculate Dec. 31st score, since today is Jan 1st
            #now test to see if we're in the first of this month
            elif(currentDay == 1 and int(year) == currentYear and int(month)== currentMonth - 1 and int(day) == dictDays[int(month)]):
                DayScore.append(1)
        
    # print(DayScore)
    #total number of robbings this year
    TotalNumberOfRobbingDay = len(DayScore)
    if TotalNumberOfRobbingDay != 0:
        finalDayScore = .3607/TotalNumberOfRobbingDay
    else:
        finalDayScore = 0
    #print(finalDayScore)
    if (finalDayScore == 0):
      finalDayScore = None
    if (finalMonthScore == 0):
      finalMonthScore = None
    
    finalYearScore = round(finalYearScore, 3)
    return ("Robbing Street Score %", finalDayScore, finalMonthScore, finalYearScore)

#current_robbing_street_score()


def current_assault_score():
    ''' Name of the function:
        Parameters: Fixed parameters include the historic data, which has a yearly avg of 861.6, monthly avg or 71.8 or a daily avg or 2.3605
        Computation: Based on the data provided in the API, I subtract a year from the current day to calculate the year score, subtract a month - currentday for the month score and 24 hours - current day for the day score.
        Returns: Tuple with day, month and year score
        '''
    #calculating year score
    YearScore = []
    for row in theft:
        #think about edge case January
        month,day,year = str(row['Date']).split('/')
        if ('Assault' in row['Type'] or 'assault' in row['Type']):
            if(int(year)  == currentYear):
                YearScore.append(1)
            elif(int(year) == currentYear - 1 and int(month) > currentMonth):
                YearScore.append(1)
            elif(int(year) == currentYear - 1 and int(month) >= currentMonth and int(day) >= currentDay):
                YearScore.append(1)
    #print(YearScore)
    #total number of robbings this year
    TotalNumberOfRobbingYear = len(YearScore)
    finalYearScore = 861.6/TotalNumberOfRobbingYear
    #print(finalYearScore)

    #calculating month score, information is outdated the months score can't be calculated
    MonthScore = []
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Assault' in row['Type'] or 'assault' in row['Type']):
            if(int(year)  == currentYear and int(month) == currentMonth):
                MonthScore.append(1)
            #edge case if it's January
            elif(int(year) == currentYear - 1 and int(month) == 12 and currentMonth == 1 and int(day) >= currentDay):
                MonthScore.append(1)
            elif(int(year) == currentYear and int(month) == currentMonth -1 and int(day) >= currentDay):
                MonthScore.append(1)
    #print(MonthScore)
    #total number of robbings this year
    TotalNumberOfRobbingMonth = len(MonthScore)
    if TotalNumberOfRobbingMonth != 0:
        finalMonthScore = 71.8/TotalNumberOfRobbingMonth
    else:
        finalMonthScore = 0
    #print(finalMonthScore)
    #calculating the day score will be yesterdays score.
    #dictDay is a key value pair with months per day
    dictDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,11:30, 12:31}
    DayScore = []
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Assault' in row['Type'] or 'assault' in row['Type']):
            if(int(year) == currentYear and int(month) == currentMonth and int(day) == currentDay -1):
                DayScore.append(1)
            elif(int(year) == currentYear -1 and int(month) == 12 and currentDay == 1 and int(day) == 31 and currentMonth == 1):
                DayScore.append(1)
                #calculate Dec. 31st score, since today is Jan 1st
            #now test to see if we're in the first of this month
            elif(currentDay == 1 and int(year) == currentYear and int(month)== currentMonth - 1 and int(day) == dictDays[int(month)]):
                DayScore.append(1)
        
    #print(DayScore)
    #total number of assults this year
    TotalNumberOfRobbingDay = len(DayScore)
    if TotalNumberOfRobbingDay != 0:
        finalDayScore = 2.3605/TotalNumberOfRobbingDay
    else:
        finalDayScore = 0
    #print(finalDayScore)
    if (finalDayScore == 0):
      finalDayScore = None
    if (finalMonthScore == 0):
      finalMonthScore = None
    
    finalYearScore = round(finalYearScore, 3)
    return ("Assault Score %", finalDayScore, finalMonthScore, finalYearScore)
#current_assault_score()

def current_theft_score():
    ''' Name of the function:
        Parameters: Fixed parameters include the historic data, which has a yearly avg of 517.4, monthly avg or 43.1166 or a daily avg or 1.410
        Computation: Based on the data provided in the API, I subtract a year from the current day to calculate the year score, subtract a month - currentday for the month score and 24 hours - current day for the day score.
        Returns: Tuple with day, month and year score
        '''
    #calculate year score, this will be done by taking into consideration data from today's date - 1 year
    #calculating year score
    YearScore = []
    for row in theft:
        #think about edge case January
        month,day,year = str(row['Date']).split('/')
        if ('Assault' in row['Type'] or 'assault' in row['Type']):
            if(int(year)  == currentYear):
                YearScore.append(1)
            elif(int(year) == currentYear - 1 and int(month) > currentMonth):
                YearScore.append(1)
            elif(int(year) == currentYear - 1 and int(month) >= currentMonth and int(day) >= currentDay):
                YearScore.append(1)
    #print(YearScore)
    #total number of robbings this year
    TotalNumberOfRobbingYear = len(YearScore)
    finalYearScore = 517.4/TotalNumberOfRobbingYear
    print(finalYearScore)

    #calculating month score, information is outdated the months score can't be calculated
    MonthScore = []
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Assault' in row['Type'] or 'assault' in row['Type']):
            if(int(year)  == currentYear and int(month) == currentMonth):
                MonthScore.append(1)
            #edge case if it's January
            elif(int(year) == currentYear - 1 and int(month) == 12 and currentMonth == 1 and int(day) >= currentDay):
                MonthScore.append(1)
            elif(int(year) == currentYear and int(month) == currentMonth -1 and int(day) >= currentDay):
                MonthScore.append(1)
    #print(MonthScore)
    #total number of robbings this year
    TotalNumberOfRobbingMonth = len(MonthScore)
    if TotalNumberOfRobbingMonth != 0:
        finalMonthScore = 43.1166/TotalNumberOfRobbingMonth
    else:
        finalMonthScore = 0
    #print(finalMonthScore)
    #calculating the day score will be yesterdays score.
    #dictDay is a key value pair with months per day
    dictDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,11:30, 12:31}
    DayScore = []
    for row in theft:
        month,day,year = str(row['Date']).split('/')
        if ('Assault' in row['Type'] or 'assault' in row['Type']):
            if(int(year) == currentYear and int(month) == currentMonth and int(day) == currentDay -1):
                DayScore.append(1)
            elif(int(year) == currentYear -1 and int(month) == 12 and currentDay == 1 and int(day) == 31 and currentMonth == 1):
                DayScore.append(1)
                #calculate Dec. 31st score, since today is Jan 1st
            #now test to see if we're in the first of this month
            elif(currentDay == 1 and int(year) == currentYear and int(month)== currentMonth - 1 and int(day) == dictDays[int(month)]):
                DayScore.append(1)
        
    #print(DayScore)
    #total number of assults this year
    TotalNumberOfRobbingDay = len(DayScore)
    if TotalNumberOfRobbingDay != 0:
        finalDayScore = 1.410/TotalNumberOfRobbingDay
    else:
        finalDayScore = 0
    #print(finalDayScore)
    if (finalDayScore == 0):
      finalDayScore = None
    if (finalMonthScore == 0):
      finalMonthScore = None
    
    finalYearScore = round(finalYearScore, 3)
    return ("Theft Score %", finalDayScore, finalMonthScore, finalYearScore)