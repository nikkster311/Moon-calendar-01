import datetime

"""
can get date from user, want to make str with month(jan, feb..) and tell info about that date
"""

basedate = datetime.datetime.strptime("06/01/2000", "%d/%m/%Y")         # new moon on this day

def userdate():
    """these values need to be set at global to use throughout this document"""
    global inputdatestring
    global inputdate
    while True:
        inputdate = input("Pick a date: dd/mm/yyyy: ")
        try:
            inputdatestring = datetime.datetime.strptime(inputdate, "%d/%m/%Y")
            return inputdatestring
            break
        except:
            print("Invalid format, try again (day goes before month).")
            contine

x = userdate() #run userdate()





"""
DAYS FROM TODAY
"""

print("The date you picked was", inputdatestring)
tdays = (x - datetime.datetime.now()).total_seconds()/86400     # 86400 seconds in a day

if tdays < 0:
    print("As of today, ", abs(tdays), " days have passed since ", x)
elif tdays > 0:
    print(tdays, " days until ", x)
else:
    print("You picked today's date.")


print(inputdatestring)




"""
WHEN IS THE NEXT MOON PHASE, AND WHAT IS IT?
"""


tdaysmoon = (x - basedate)     # how many days since reference full moon, if this/29.5=0then full moon
tdaysmoonfloat = ((x - basedate).total_seconds())/86400    # 86400 seconds in a day

print("Tdaysmoon = ", tdaysmoon) #this and next 3 lines as references, refresh your memory after writing this code
print("tdaysmoon float = ", tdaysmoonfloat)
print("basedate = ", basedate) #jan 6 2000, refernce for full moon nearest the new millenium
print('x = ', x) #user input date

print(tdaysmoonfloat, " days have passed since jan 6 2000")
print(float(tdaysmoonfloat) % 29.5, "days before or after a new moon")


def whatphase(): #what phase is/was/will the moon be in?
    # tdaysmoon = (userdate() - basedate)
    if tdaysmoon % 29.5 == 0:
        print("There will be a new moon on ", inputdatestring())
    elif tdaysmoon % 29.5 >=

        """find out how many days the moon is in each phase, break that into columns, waxing waning gibbous cresent, use %s? do elif for each"""



# print(datetime.datetime.strptime(inputdate, "%A, %B %d, %Y"))


""" jan 6 2000 = new moon = reference date, 29.5 days for a full moon cycle
if diff between days"""
