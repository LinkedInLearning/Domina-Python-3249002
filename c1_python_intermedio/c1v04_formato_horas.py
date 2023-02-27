from datetime import datetime


def dates():

    date = datetime.now()
    new_format_24 = date.strftime('%H:%M:%S')
    new_format_12 = date.strftime('%I:%M:%S %p')

    print("date", date)
    print("24 Hours: ", new_format_24)
    print("AM/PM: ", new_format_12)
