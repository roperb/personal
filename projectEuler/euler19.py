
#How many Sundays fell on the first of the month during the 20th century

monthList = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
dayList = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
month = 0
sundayCounter = 0
year = 1901
dayOfMonth = 1
dayOfWeek = 1

def isLeapYear(year):
    if year%4 != 0:
        return False
    if year%400 == 0:
        return True
    return False


while year < 2001:
    if dayOfMonth == 1 and dayOfWeek == 6:
        sundayCounter += 1
        print(year)
        print(month)

    dayOfMonth += 1

    #Check if it is time for the next month for February on a leap year
    if isLeapYear(year) and month == 1:
        if dayOfMonth == 30:
            month = 2
            dayOfMonth = 1

    if ~isLeapYear(year) and month == 1:
        if dayOfMonth == 29:
            month = 2
            dayOfMonth = 1

    #Check if it is the end of the month otherwise
    if dayOfMonth > monthDays[month]:

        dayOfMonth = 1
        month = (month+1)%12
        #Check if the year changed
        if month == 0:
            year += 1
    dayOfWeek = (dayOfWeek+1)%7

print(sundayCounter)


