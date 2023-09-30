class FactoryElectricityConsumption:
    total_plan_consumption = 0
    total_actual_consumption = 0

    def __init__(self, serial_number, factory_name, plan_consumption, actual_consumption):
        self.serial_number = serial_number
        self.factory_name = factory_name
        self.plan_consumption = plan_consumption
        self.actual_consumption = actual_consumption

    def calculate_o1(self):
        return self.plan_consumption - self.actual_consumption

    def calculate_o2(self):
        if self.plan_consumption == 0:
            return 0
        return (self.calculate_o1() * 100) / self.plan_consumption

    def display_info(self):
        o1 = self.calculate_o1()
        o2 = self.calculate_o2()
        # Форматуємо рядок так, щоб кожен стовпець мав фіксовану ширину
        print(f"| {self.serial_number:<2} | {self.factory_name:<19} | {self.plan_consumption:<35.2f} | {self.actual_consumption:<29.2f} | {o1:<20.2f} | {o2:<14.2f} |")

    @classmethod
    def update_total_consumption(cls, plan_consumption, actual_consumption):
        cls.total_plan_consumption += plan_consumption
        cls.total_actual_consumption += actual_consumption

def main():
    while True:
        try:
            num_entries = int(input("Введіть кількість записів: "))
            if num_entries <= 0:
                raise ValueError("Кількість записів повинна бути більше нуля")
            break
        except ValueError:
            print("Помилка: Введіть правильне ціле число більше нуля.")

    factories = []


    for i in range(num_entries):
        serial_number = i + 1
        factory_name = input(f"Введіть назву заводу #{serial_number}: ")
        while True:
            try:
                plan_consumption = float(input(f"Введіть споживання електроенергії за планом (кВт/год) для заводу #{serial_number}: "))
                actual_consumption = float(input(f"Введіть фактичне споживання електроенергії (кВт/год) для заводу #{serial_number}: "))
                break
            except ValueError:
                print("Помилка: Введіть правильні числові значення для споживання електроенергії.")

        factory = FactoryElectricityConsumption(serial_number, factory_name, plan_consumption, actual_consumption)
        factories.append(factory)
        FactoryElectricityConsumption.update_total_consumption(plan_consumption, actual_consumption)
    
    # Виводимо заголовок таблиці
    print("| №  | Назва заводу        | Споживання електроенергії (кВт/год) | Фактичне споживання (кВт/год) | Відхилення (кВт/год) | Відхилення (%) |")
    # Розділяємо заголовок лінією
    print("-" * 138)
    
    for factory in factories:
        factory.display_info()
    
    
    # Виводимо загальні значення
    print("-" * 138)
    print(f"|    | {'Загально':<19} | {FactoryElectricityConsumption.total_plan_consumption:<35.2f} | {FactoryElectricityConsumption.total_actual_consumption:<29.2f} | "
          f"{FactoryElectricityConsumption.total_plan_consumption - FactoryElectricityConsumption.total_actual_consumption:<20.2f} | "
          f"{(FactoryElectricityConsumption.total_plan_consumption - FactoryElectricityConsumption.total_actual_consumption) * 100 / FactoryElectricityConsumption.total_plan_consumption:<14.2f} |")

if __name__ == "__main__":
    main()