"""Вам потрібно реалізувати корисну функцію для виведення списку колег, 
яких потрібно привітати з днем народження на тижні.
У вас є список словників users, кожен словник у ньому обов'язково має ключі name та birthday. 
Така структура представляє модель списку користувачів з їх іменами та днями народження. 
name — це рядок з ім'ям користувача, 
а birthday — це datetime об'єкт, в якому записаний день народження.
Ваше завдання написати функцію get_birthdays_per_week, 
яка отримує на вхід список users і виводить у консоль 
(за допомогою print) список користувачів, яких потрібно привітати по днях.

Умови приймання​
get_birthdays_per_week виводить іменинників у форматі:
Monday: Bill, Jill
Friday: Kim, Jan
Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.
Для тестування зручно створити тестовий список users та заповнити його самостійно.
Функція виводить користувачів з днями народження на тиждень вперед від поточного дня.
Тиждень починається з понеділка."""

import datetime

users = [{"name": "Bill Klinton", "birthday": "02.08.1990"},
         {"name": "Demmy Moore", "birthday": "05.08.1986"},
         {"name": "Jackie Chan", "birthday": "06.08.2000"},
         {"name": "Tom Kruz", "birthday": "03.08.1970"},
         {"name": "Jay Lo", "birthday": "25.12.1978"},
         {"name": "John Smith", "birthday": "31.07.1978"}]

def get_birthdays_per_week(users):

    birthday_weekdays = {"Monday":[], "Tuesday": [], "Wednesday": [], "Thursday": [],
                          "Friday": [], "Saturday": [], "Sunday" : [], "next Monday": []}

    current_date = datetime.datetime.now().date()
    
    current_weekday = current_date.weekday()
    
    start_point = current_date - datetime.timedelta(days=current_weekday)
    
    end_point = start_point + datetime.timedelta(days=6)
    

    for user in users:
        username = user.get("name")
        
        user_birthday = user.get("birthday")
        user_birthday_dt = datetime.datetime.strptime(user_birthday, "%d.%m.%Y").date()
        

        user_birthday_dt = user_birthday_dt.replace(year=current_date.year)

        if start_point <= user_birthday_dt <= end_point:
            
    
            user_weekday = user_birthday_dt.weekday()
            if user_weekday in [0]:
                birthday_weekdays["Monday"].append(username)
            elif user_weekday in [1]:
                birthday_weekdays["Tuesday"].append(username)
            elif user_weekday in [2]:
                birthday_weekdays["Wednesday"].append(username)
            elif user_weekday in [3]:
                birthday_weekdays["Thursday"].append(username)
            elif user_weekday in [4]:
                birthday_weekdays["Friday"].append(username)
            elif user_weekday in [5,6]:
                birthday_weekdays["next Monday"].append(username)
        
    

    for key, value in birthday_weekdays.items():
        
        if not value:
            continue
        else:
            print(f"{key}: {', '.join(value)}")







if __name__ == "__main__":
    get_birthdays_per_week(users)