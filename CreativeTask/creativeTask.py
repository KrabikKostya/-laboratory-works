from sqlalchemy.orm import sessionmaker
from db import engine
from time import sleep


class App:
    @staticmethod
    def dbWorker():
        session = sessionmaker(bind=engine)
    @staticmethod
    def randomaizer(lst, count):
        from random import choice
        answer = ""
        for i in range(count):
            answer += str(choice(lst))
        return answer

    @staticmethod
    def choiceOfMaterials():
        answer = input(
            "Введіть найважливіші параметри (ціна(діпазон), стійкість до вологи і таке інше): "
        )
        print("Пошук в базах данних складу...")
        sleep(10)
        print("Підбір моделі згідно параметрів...")
        sleep(10)
        print(f"""Вам ідеально підійде {App.randomaizer(["Ялина", "Дуб", "Сосна", "Тополь", "Червоне дерево", "ДВП", "Пластик", "Метал", "Горіх"], 1)}""")
        App.question()

    @staticmethod
    def question():
        print(
            "Ви бажаєте продовжити ?",
            "1 - Так",
            "2 - Ні",
            sep="\n"
        )
        answer = int(input("Виберіть пункт меню: "))
        if answer == 1:
            App.main()
        else:
            App._exit()

    @staticmethod
    def calculationOfDimensions():
        try:
            dimensions = map(float, input("Введіть довжину, ширену і висоту (в метрах): ").split(","))
            summ = 1
            dimensions = list(dimensions)
            for i in dimensions:
                summ *= i
            print(
                f"Габарити виробу складають: {summ} метрів кубічних і {summ/dimensions[2]} метрів квадратних"
            )
            App.question()
        except Exception:
            App.error()

    @staticmethod
    def error():
        print("Помилка, спробуйте ще раз")
        App.main()

    @staticmethod
    def order():
        from time import sleep
        try:
            answer = int(input("Введіть номер виробу: "))
            print("Пошук в базах данних складу...")
            sleep(10)
            print(f"Виріб №{answer} замовлено, дякуємо, що вибрали нас")
            App.question()
        except Exception:
            App.error()

    @staticmethod
    def orderSum():
        try:
            price = map(float, input("Введіть ціни на замовлені товари: ").split(" "))
            print(f"Кінцева вартість замовлення: {sum(price)} грн.")
            App.question()
        except Exception:
            App.error()

    @staticmethod
    def buyerAssistant():
        from time import sleep
        answer = input(
            "Введіть найважливіші параметри (ціна(діпазон), стійкість до вологи і таке інше): "
        )
        print("Пошук в базах данних...")
        sleep(10)
        print("Підбір моделі згідно параметрів...")
        sleep(10)
        print(
            f"Вам ідеально підійде модель №{App.randomaizer(range(10), 4)}"
        )
        print(
            "Перейти до замовлення ? ",
            "1 - Так",
            "2 - Ні",
            sep="\n"
        )
        try:
            answer = int(input("Виберіть пункт меню: "))
            if answer == 1:
                App.order()
            else:
                App.question()
        except Exception:
            App.error()

    @staticmethod
    def about():
        print("Програму розробив студент Б12_Д 122 группи А Грабік Костянтин ігорович")
        App.question()

    @staticmethod
    def _exit():
        print("Дякую, що скористалися програмою")
        exit()


def main():
    print("Помічник збірника меблів")
    print(
        "1 - Підрахувати сумму замовлення",
        "2 - Допомогти покупцеві з вибором",
        "3 - Вибрати матеріал для меблів",
        "4 - Замовити заготовку з скаладу",
        "5 - Обчислення габаритів(об'єму, площі) виробу",
        "6 - Про програму",
        "0 - Вихід",
        sep="\n",
    )
    try:
        answer = int(input("Виберіть пункт меню: "))
        if answer == 0:
            App._exit()
        elif answer == 6:
            App.about()
        elif answer == 5:
            App.calculationOfDimensions()
        elif answer == 4:
            App.order()
        elif answer == 3:
            App.choiceOfMaterials()
        elif answer == 2:
            App.buyerAssistant()
        elif answer == 1:
            App.orderSum()
        else:
            print(
                "Невыдома команда",
                "Спробуйте ще раз",
                sep="\n"
            )
            App.main()
    except Exception:
        App.error()


if __name__ == "__main__":
    main()
