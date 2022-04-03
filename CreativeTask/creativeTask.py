from db import engine, base, Customer, Item, Order, OrderLine, Materials
from sqlalchemy.orm import Session
from time import sleep
from random import randint


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
            main()
    except Exception:
        App.error()


class App:
    @staticmethod
    def error():
        print("Помилка, спробуйте ще раз")
        main()

    @staticmethod
    def randomaizer(lst, count):
        from random import choice
        answer = ""
        for i in range(count):
            answer += str(choice(lst))
        return answer

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
            main()
        else:
            App._exit()

    @staticmethod
    def choiceOfMaterials():
        answer = input("Введіть найважливіші параметри (ціна(діпазон), стійкість до вологи і таке інше): ")
        print("Пошук в базах данних складу...")
        sleep(5)
        session = Session(bind=engine)
        if list(session.query(Materials).all()) is []:
            lst = ["Ялина", "Дуб", "Сосна", "Тополь", "Червоне дерево", "ДВП", "Пластик", "Метал", "Горіх"]
            for i in range(5):
                material = App.randomaizer(lst, 1)
                session.add(Materials(material_name=material))
                lst.remove(material)
                session.commit()
        print("Підбір моделі згідно параметрів...")
        sleep(10)
        material_id = session.query(Materials).get(randint(1, 9))
        if material_id is None:
            print("Нажаль ідеального, для вас, матеріалу на складі не має")
        else:
            print(f"""Вам ідеально підійде {material_id.material_name}""")
        App.question()

    @staticmethod
    def calculationOfDimensions():
        try:
            dimensions = map(float, input("Введіть довжину, ширену і висоту (в метрах): ").split(","))
            summ = 1
            dimensions = list(dimensions)
            for i in dimensions:
                summ *= i
            print(f"Габарити виробу складають: {summ} метрів кубічних і {summ/dimensions[2]} метрів квадратних")
            App.question()
        except Exception:
            App.error()

    @staticmethod
    def make_order():
        session = Session(bind=engine)
        try:
            first_name = input("first_name: ")
            last_name = input("last_name: ")
            quantity = int(input("quantity: "))
            serial_number = int(input("serial_number: "))
            customer = Customer(
                first_name=first_name,
                last_name=last_name
            )
            session.add(customer)
            session.commit()
            for i in range(10):
                item = Item(
                    selling_price=randint(500, 2000),
                    quantity=randint(0, 1000),
                    serial_number=App.randomaizer(range(10), 4)
                )
                session.add(item)
                session.commit()
            order = Order(customer=customer)
            order_lines = OrderLine(
                item=session.query(Item).filter(Item.serial_number == serial_number),
                quantity=quantity
            )
            order.line_items.append(order_lines)
            session.add_all([order, order_lines])
            session.commit()
        except Exception:
            App.error()

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
        answer = input("Введіть найважливіші параметри (ціна(діпазон), стійкість до вологи і таке інше): ")
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


if __name__ == "__main__":
    main()
