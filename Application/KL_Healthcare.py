# This is my current python open source work.
import time
import datetime

# Input value for the rows and the columm is fixed to five.
while True:
    try:
        n = int(input("How many data do you want to enter? "))
        if n > 0:
            break
        else:
           print("Please enter a valid number - From 1 - 10" )
           continue 
    except ValueError:
        print("Please enter a valid number - From 1 - 10")
        continue

# Declare Variables
rows = int(n)
cols = 5
now = time.localtime()
today = datetime.date.today()

data_array = [[0 for i in range(cols)] for j in range(rows)]

for n in range(0,rows):
    i = int(n)

    # Testing to confirm date is in the future
    while True:
        try:
            date = input("Please enter a date: ")
            # Test the date inputed
            date_to_array = date.split('.')

            day = int(date_to_array[0])
            month = int(date_to_array[1])
            year = int(date_to_array[2])
            
            if (day >= today.day and month >= today.month and year >= today.year):
                break
            else:
                print("Please enter a valid date - From "  +  str(today.day) + "." + str(today.month) + "." + str(today.year) + " Using format ( Day.Month.Year )" )
                continue
        except ValueError:
            print("Please enter a valid time - From " +  str(today.day) + "." + str(today.month) + "." + str(today.year) + " Using format ( Day.Month.Year )")
            continue
      

    data_array[i][0] = int(day)
    data_array[i][1] = int(month)
    data_array[i][2] = int(year)
    
    # Testing to confirm time is in the future
    while True:
        try:
            the_time = input("Please enter a time: ")
            # Test the time inputed
            time_to_array = the_time.split(':')

            hour = int(time_to_array[0])
            minutes = int(time_to_array[1])
            
            if (hour in range(0, 24) and minutes in range(0, 60) and data_array[i][0] > today.day and data_array[i][1] >= today.month and data_array[i][2] >= today.year):
                break
            elif(str(hour) >= str(now.tm_hour) and str(minutes) > str(now.tm_min) and data_array[i][0] == today.day and data_array[i][1] == today.month and data_array[i][2] == today.year):
                break
            else:
                print("Please enter a valid time in the future - Hours(0 - 23) and Minutes(0 - 59)")
                continue
        except ValueError:
            print("Please enter a valid time in the future - Hours(0 - 23) and Minutes(0 - 59)")
            continue
    print("\n")
    


    data_array[i][3] = int(hour)
    data_array[i][4] = int(minutes)
    

print("Thank you very much. I will notify them! ")
print("....\n")


# Countdown
numbers = ["First" , "Second" , "Third" , "Fourth" , "Fifth" , "Sixth" , "Seventh", "Eighth", "Ninth" , "Tenth" ]


while True:
    try:
        for n in range(0,rows):
            i = int(n)
                
            wait = True
            while (wait):
                condition = (data_array[i][0] == int(datetime.datetime.now().day) and 
                             data_array[i][1] == int(datetime.datetime.now().month) and 
                             data_array[i][2] == int(datetime.datetime.now().year) and 
                             data_array[i][3] == int(datetime.datetime.now().hour) and 
                             data_array[i][4] == int(datetime.datetime.now().minute))
                if((condition)):
                    print("The " + numbers[i] + " date has been reached! " + "( " + str(data_array[i][0]).zfill(2) +"."+ str(data_array[i][1]).zfill(2) +"."+ str(data_array[i][2]) + " - " + str(data_array[i][3]).zfill(2)+":"+ str(data_array[i][4]).zfill(2) + " )")
                    wait = False
                else:
                    time.sleep(5)
                    continue       
        break
    except ValueError:
        print("Error")
    finally:
        print(" ")

