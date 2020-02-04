import random

class Human():

    def __init__(self, id=0, name='', age=0, sex='', education=0, income=0, work_status='', square=0, cash=0, bank_account=0, iq=150, eq=150):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.education = education
        self.income = income
        self.work_status = work_status
        self.square = square
        self.cash = cash
        self.bank_account = bank_account
        self.iq = iq
        self.eq = eq

    def income_calc(self):
        income_temp = 0
        base_income = 1000
        work_status_mult = 1
        age_mult = 1
        education_mult = 1
        sex_mult = 1
        iq_mult = 1
        eq_mult = 1

        if self.work_status == 'bezr':
            work_status_mult = 0.2
        elif self.work_status == 'rab':
            work_status_mult = 1.0
        elif self.work_status == 'high skill rab':
            work_status_mult = 1.2
        elif self.work_status == 'boss':
            work_status_mult = 5.0

        if self.education <= 20:
            education_mult = 0.8
        elif self.education > 20 and self.education <= 40:
            education_mult = 1.0
        elif self.education > 40 and self.education <= 60:
            education_mult = 1.5
        elif self.education >60 and self.education <100:
            education_mult = 1.9

        if self.sex == 'male' :
            self.sex_mult = 1.5
        else:
            self.sex_mult = 1.0

        if self.age <= 18:
            self.age_mult = 0.05
        elif self.age > 18 and self.age <= 25:
            self.age_mult = 2
        elif self.age > 25 and self.age <= 45:
            self.age_mult = 3
        elif self.age > 45 and self.age <= 65:
            self.age_mult = 2
        elif self.age >65:
            self.age_mult = 1.5

        iq_mult = self.iq // 150
        eq_mult = self.eq // 150

        income_temp = base_income * age_mult * sex_mult * education_mult * work_status_mult * iq_mult * eq_mult
        return income_temp

    def index(self):
        pass

max = Human(1, 'Maxim Vladimirovich', 35, 'Male', 45, 0, 'boss', 0, 0, 0, 200, 200)
petr = Human(2, 'Petr', 45, 'Male', 70, 0, 'rab')
olga = Human(3, 'Olga', 20, 'Female', 30, 0, 'bezr')
print(max.name)
print(max.income_calc())
print(petr.name)
print(petr.income_calc())
print(olga.name)
print(olga.income_calc())
print(type(olga))

data = []
data.append(olga)
data.append(petr)
data.append(max)

print(data)
print(len(data))
print(data[1].income_calc())

for i in data:
    if data[i].name == "olga":
        print(data.index())
#
# data.index()