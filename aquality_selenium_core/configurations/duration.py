import datetime


class Duration(datetime.timedelta):
    @property
    def milliseconds(self) -> float:
        return self.microseconds / 1000.0
