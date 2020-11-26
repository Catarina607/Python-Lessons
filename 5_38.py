
day = int(input('DAY: '))
month = int(input('MONTH: '))
year = int(input('YEAR: '))

if ((year % 400 == 0) and (year <= 2020)) and ((month > 0) and (month < 13)):
    print('VALID DATA')
    """BISSEXT YEAR"""
elif ((day > 0) and (day < 31)) and (month == 1):
    print('VALID DATA')
    """ January"""
elif ((day > 0) and (day < 29)) and (month == 2):
    print('VALID DATA')
    """February"""
elif ((day > 0) and (day < 31)) and (month == 3):
    print('VALID DATA')
    """March"""
elif ((day > 0) and (day <= 30)) and (month == 4):
    print('VALID DATA')
    """April"""
elif ((day > 0) and (day < 31)) and (month == 5):
    print('VALID DATA')
    """May"""
elif ((day > 0) and (day <= 30)) and (month == 6):
    print('VALID DATA')
    """June"""
elif ((day > 0) and (day < 31)) and (month == 7):
    print('VALID DATA')
    """July"""
elif ((day > 0) and (day < 31)) and (month == 8):
    print('VALID DATA')
    """August"""
elif ((day > 0) and (day <= 30)) and (month == 9):
    print('VALID DATA')
    """September"""
elif ((day > 0) and (day < 31)) and (month == 10):
    print('VALID DATA')
    """October"""
elif ((day > 0) and (day <= 30)) and (month == 11):
    print('VALID DATA')
    """November"""
elif ((day > 0) and (day < 31)) and (month == 12):
    print('VALID DATA')
    """December"""
elif ((year % 400 > 0) and (year <= 2020)) and ((month > 0) and (month < 13)):
    print('VALID DATA')
    """NON-BISSEXT YEAR"""
elif ((day > 0) and (day < 31)) and (month == 1):
    print('VALID DATA')
    """ January"""
elif ((day > 0) and (day < 28)) and (month == 2):
    print('VALID DATA')
    """February"""
elif ((day > 0) and (day < 31)) and (month == 3):
    print('VALID DATA')
    """March"""
elif ((day > 0) and (day <= 30)) and (month == 4):
    print('VALID DATA')
    """April"""
elif ((day > 0) and (day < 31)) and (month == 5):
    print('VALID DATA')
    """May"""
elif ((day > 0) and (day <= 30)) and (month == 6):
    print('VALID DATA')
    """June"""
elif ((day > 0) and (day < 31)) and (month == 7):
    print('VALID DATA')
    """July"""
elif ((day > 0) and (day < 31)) and (month == 8):
    print('VALID DATA')
    """August"""
elif ((day > 0) and (day <= 30)) and (month == 9):
    print('VALID DATA')
    """September"""
elif ((day > 0) and (day < 31)) and (month == 10):
    print('VALID DATA')
    """October"""
elif ((day > 0) and (day <= 30)) and (month == 11):
    print('VALID DATA')
    """November"""
elif ((day > 0) and (day < 31)) and (month == 12):
    print('VALID DATA')
    """December"""
else:
    print("INVALID DATA!")
