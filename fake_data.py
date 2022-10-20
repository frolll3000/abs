import faker


class FakeLibrary:
    def __init__(self):
        self.fake = faker.Faker('ru_RU')

    def get_full_name(self):
        return self.fake.last_name() + " " + self.fake.first_name() + " " + self.fake.middle_name()

    def get_birth_day(self):
        return self.fake.date_of_birth(minimum_age=20, maximum_age=60).strftime("%d.%m.%Y")

    def get_passport_number(self):
        return self.fake.bothify(text='##########')

    def get_address(self):
        return self.fake.address()

    def get_phone_number(self):
        return self.get_passport_number()

    def get_email(self):
        return self.fake.email()
