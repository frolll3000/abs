import faker
fake = faker.Faker('ru_RU')


def get_full_name():
    return fake.last_name() + " " + fake.first_name() + " " + fake.middle_name()


def get_birth_day():
    return fake.date_of_birth(minimum_age=20, maximum_age=60).strftime("%d.%m.%Y")


def get_passport_number():
    return fake.bothify(text='##########')


def get_address():
    return fake.address()


def get_phone_number():
    return get_passport_number()


def get_email():
    return fake.email()
