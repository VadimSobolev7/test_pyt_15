# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки. При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые, т.е не мая, а 5

import datetime
import sys

WEEKDAYS = {"понедельник": 0, "вторник": 1, "среда": 2, "четверг": 3,
            "пятница": 4, "суббота": 5, "воскресенье": 6}

MONTHS = {"января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6,
          "июля": 7, "августа": 8, "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}

def correct_date(text: str) -> datetime.datetime:
    week_count, weekday, month = text.split()
    week_count = int(week_count[0])
    weekday = WEEKDAYS[weekday]
    month = MONTHS[month]

    week_passed = 0
    for day in range(1, 31):
        temp_date = datetime.datetime(datetime.datetime.now().year, month, day)
        if temp_date.weekday() == weekday:
            week_passed += 1
            if week_passed == week_count:
                return temp_date
    raise ValueError(f"Такой даты не существует: '{text}'")

if __name__ == "__main__":
    path, date, *_ = sys.argv
    print(correct_date(date))