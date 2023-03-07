from datetime import date, timedelta


def default_devolution_date():
    return date.today() + timedelta(days=7)
