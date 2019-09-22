import csv
import random

records=1000000
print("Making %d records\n" % records)

fieldnames=['vibrationValue','humidityValue','tempValue','failureValue']
writer = csv.DictWriter(open("dataset20.csv", "w",newline=''), fieldnames=fieldnames)

writer.writerow(dict(zip(fieldnames, fieldnames)))

for i in range(records):
    vV=int(random.randint(0,100))
    hV=int(random.randint(0,100))
    tV=int(random.randint(0,100))
    
    fV=0
    if vV > 80 : fV=fV+((vV - 80)*5/3)
    if hV > 80 : fV=fV+((hV - 80)*5/3)
    if tV > 80 : fV=fV+((tV - 80)*5/3)
    
    prob=int(random.randint(0,100))
    if fV > prob:
        fV=1
    else:
        fV=0

    writer.writerow(dict([
    ('vibrationValue', vV),
    ('humidityValue', hV),
    ('tempValue', tV),
    ('failureValue', fV)]))
 
    				