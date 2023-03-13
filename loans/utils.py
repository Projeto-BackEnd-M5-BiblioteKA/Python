from datetime import date, timedelta


def default_devolution_date():
    devolution_date = date(year=2023, month=3, day=10) + timedelta(days=7)
    
    if devolution_date.weekday() == 5:
        devolution_date = devolution_date + timedelta(days=2)
    if devolution_date.weekday() == 6:
        devolution_date = devolution_date + timedelta(days=1)

    return devolution_date
