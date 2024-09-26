from datetime import datetime

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property  # (Use this decorator for the getter or accessor)
    def first_name(self) -> str:
        return self._first_name.title()  # Optional formatting code

    @first_name.setter
    def first_name(self, value: str) -> None:
        if value.isalpha() or value == "":  # allow characters or the default empty string
            self._first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self) -> str:
        return self._last_name.title()  # Optional formatting code

    @last_name.setter
    def last_name(self, value: str) -> None:
        if value.isalpha() or value == "":  # allow characters or the default empty string
            self._last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self) -> str:
        return f'{self.first_name},{self.last_name}'

class Employee:

    def __init__(self, first_name: str, last_name: str, review_date: datetime.date, review_rating: int) -> None:
        super().__init__(first_name, last_name)
        self.review_date = datetime.date.strptime(review_date, "1900-01-01").date()
        self.review_rating = (review_rating, "3")

    @property
    def review_date(self):
        return self._datetime.date   # Optional formatting code

    @review_date.setter
    def review_date(self, value: str):
        self._review_date = value

        if value.isalpha() or value == "":  # allow characters or the default empty string
            self._review_date = value
        else:
            raise ValueError("The review_date should be YYYY-MM-DD.")

    @property
    def review_rating(self):
        return self._review_rating

    @review_rating.setter
    def review_rating(self, value: int, choice= "3"):
        self._review_rating = value

        if choice in ['1', '2', '4', '5']:
            raise Exception("The Rating is defaults to number '3'")

    def __str__(self) -> str:
        return f'{self.first_name},{self.last_name},{self.review_date},{self.review_rating}'

if __name__ == '__main__':
    print("This file is not meant to be run, please run main.py")