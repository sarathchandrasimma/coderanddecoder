hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
# find a total of all minutes
tm=mins+dura
h=tm//60
m=tm%60
hour+=h
hour=hour%24
mins=m
# find a number of hours hidden in minutes and update the hour
# correct minutes to fall in the (0..59) range
# correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')