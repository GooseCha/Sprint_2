class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(
        cls,
        name,
        hours,
        rest_days,
    ):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.chourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment


# Примеры использования:
# Создание сотрудника с известными часами
emp1 = EmployeeSalary("Иван", 40, 2, "ivan@company.com")
print(emp1.salary())  # 16000

# Создание сотрудника с расчётом часов по выходным
emp2 = EmployeeSalary.get_hours("Петр", 2)  # rest_days=2, значит hours=(7-2)*8=40
print(emp2.salary())  # 16000

# Создание сотрудника с генерацией email
emp3 = EmployeeSalary.get_email("Мария", 35, 1)  # email сгенерируется автоматически
print(emp3.email)  # Мария@email.com

# Изменение почасовой оплаты
EmployeeSalary.set_hourly_payment(500)
print(emp1.salary())  # 20000 (40 * 500)
