from db import engine, Customer, Item, Order, OrderLine, Materials
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
        "6 - Додати замовлення",
        "7 - Про програму",
        "0 - Вихід",
        sep="\n",
    )
    try:
        answer = int(input("Виберіть пункт меню: "))
        if answer == 0:
            App._exit()
        elif answer == 7:
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
        elif answer == 6:
            App.makeOrder()
        else:
            print(
                "Невыдома команда",
                "Спробуйте ще раз",
                sep="\n"
            )
            main()
    except ValueError:
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
        dimensions = map(float, input("Введіть довжину, ширену і висоту (в метрах): ").split(","))
        summ = 1
        dimensions = list(dimensions)
        for i in dimensions:
            summ *= i
        print(f"Габарити виробу складають: {summ} метрів кубічних і {summ/dimensions[2]} метрів квадратних")
        App.question()

    @staticmethod
    def makeOrder():
        session = Session(bind=engine)
        first_name = input("first_name: ")
        last_name = input("last_name: ")
        quantity = int(input("quantity: "))
        serial_number = int(input("serial_number: "))
        customer = Customer(
            first_name=first_name,
            last_name=last_name
        )
        for i in range(10):
            item = Item(
                selling_price=randint(500, 5000),
                quantity=randint(0, 1000),
                serial_number=App.randomaizer(range(10), 4)
            )
            session.add(item)
            session.commit()
        order = Order(
            customer=customer,
            order_number=App.randomaizer(range(10), 10)
        )
        id = session.query(Item).filter(Item.serial_number == serial_number).all()
        if len(list(id)) > 0:
            order_lines = OrderLine(
                item=session.query(Item).get(id[0].id),
                quantity=quantity
            )
            order.line_items.append(order_lines)
            session.add(order)
            session.add(order_lines)
            session.add(customer)
            session.commit()
            print(
                "Ваше замовлення успишно додано",
                f"Ваш номер замовлення: {session.query(Order).all()[len(session.query(Order).all())].order_number}"
            )
        else:
            print("Нажаль виробу більше немає на складі")
            session.rollback()
        App.question()

    @staticmethod
    def order():
        from time import sleep
        answer = int(input("Введіть номер замовлення: "))
        print("Пошук в базах данних складу...")
        sleep(5)
        session = Session(bind=engine)
        id = session.query(Order).filter(Order.order_number == answer).all()
        if len(id) > 0:
            print(f"Замовлення №{answer} зроблено, дякуємо, що вибрали нас")
        else:
            print("Такого замовлення не існує")
        App.question()

    @staticmethod
    def orderSum():
        price = map(float, input("Введіть ціни на замовлені товари: ").split(" "))
        print(f"Кінцева вартість замовлення: {sum(price)} грн.")
        App.question()

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
        answer = int(input("Виберіть пункт меню: "))
        if answer == 1:
            App.order()
        else:
            App.question()

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
