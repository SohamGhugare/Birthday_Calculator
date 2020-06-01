import datetime

tday = datetime.date.today()        # Grabbing today's date
bday = datetime.date(2020, 7, 10)   # Enter Birthday date

daysRemain = bday - tday
print('The Birthday is in {} days'.format(daysRemain.days))
