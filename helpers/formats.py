import datetime


def money(number):
    if type(number) == int:
        return '${:,}'.format(number)
    return number


def date(date_string):
    if type(date_string) != datetime.date:
        year, month, day = map(int, date_string.split('-'))
        return datetime.date(year, month, day)
    return date_string
