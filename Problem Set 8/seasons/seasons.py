from datetime import date, datetime
import datetime
import sys
import inflect

class Birthdaycalculator():
    def __init__(self):
        pass

    def get_dob(self):
        try:
            dob= datetime.datetime.strptime(input("Date of Birth: "),"%Y-%m-%d")
            return dob.date()
        except ValueError:
            sys.exit("Invalid Date")

    def calculate_age(self, birth_date):
        current= date.today()
        age = (current - birth_date).days * 24 * 60
        return age

    def display_age(self,age_in_minutes):
        p = inflect.engine()
        return p.number_to_words(age_in_minutes, andword ="")

    def run(self):
        age_in_minutes = self.calculate_age(self.get_dob())
        print(f"{self.display_age(age_in_minutes)} minutes".capitalize())
def main():
    calculator = Birthdaycalculator()
    calculator.run()

if __name__=="__main__":
    main()
