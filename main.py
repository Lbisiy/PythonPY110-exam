import itertools
import json
import random
from conf import MODEL
import faker


def dict_generator(pk=1) -> dict:
    """
    Функция-генератор.
    Генерирует словари, содержащие даннные о книгах (название, авторы, год, кол-во страниц, ISBN номер, рейтинг, цена).

    :param pk: Автоинкримент, который увеличивается на 1 при генерации нового объекта. По умолчанию = 1.
    :return: Словарь dict с данными о книге.
    """
    for _ in itertools.count():
        dict_ = {
            "model": MODEL,
            "pk": pk,
            "fields": {
                "title": title(),
                "year": year(),
                "pages": pages(),
                "isbn13": isbn13(),
                "rating": rating(),
                "price": price(),
                "author":
                    author()
            }
        }
        yield dict_
        pk += 1


def name_length(length: int = 30):
    """
    Фабрика декораторов.
    Проверяет длину книги. При превышении передаваемого значения длины выдает ошибку.

    :param length: Передаваемый динамический параметр длины названия книги.
    :return: Возвращает декоратор.
    """
    def main_decorator(func):
        def wrapper():
            result = func()
            if len(result) >= length:
                raise ValueError('Название книги слишком длинное')
            return result
        return wrapper
    return main_decorator


@name_length(50)
def title() -> list[str]:
    """
    Функция генерации названий книг.
    Берет названия из файла books.txt в случайном порядке.

    :return: Название книги.
    """
    path = 'books.txt'
    with open(path, encoding='utf8') as f:
        books = f.readlines()
        books = random.choice(books).rstrip()
        return books


def year() -> int:
    """
    Функция генерации года выхода книги.

    :return: Случайный год выхода книги в диапазоне 1900-2022 гг.
    """
    return random.randint(1900, 2022)


def pages() -> int:
    """
    Функция генерации кол-ва страниц в книге.

    :return: Случайное кол-во страниц в диапазоне 100-1000 стр.
    """
    return random.randint(100, 1000)


def isbn13() -> str:
    """
    Функция генерации номера ISBN.

    :return: Случайный номер ISBN.
    """
    fake = faker.Faker("ru")
    return fake.isbn13()


def rating() -> float:
    """
    Функция генерации рейтинга книги.

    :return: Случайный рейтинг книги в диапазоне 0.00-5.00, округленный до 2-х знаков после запятой.
    """
    return round(random.uniform(0.0, 5.0), 2)


def price() -> float:
    """
    Функция генерации цены книги.

    :return: Случайная цены книги в диапазоне 100-1000000, округленная до 2-х знаков после запятой.
    """
    return round(random.uniform(100.0, 1000000.0), 2)


def author() -> list[str]:
    """
    Функция генерации авторов.
    Генерурует кол-во авторов книги от 1 до 3 и случайно генерирует имена и фамилии авторов (мужского пола).

    :return: Случайные мужские имена и фамилии авторов в случайном количественном диапазоне (1-3).
    """
    fake = faker.Faker("ru")
    return [fake.first_name_male() + ' ' + fake.last_name_male() for _ in range(random.randint(1, 3))]


def main(num_book: int = 100, pk_: int = 1) -> None:
    """
    Main функция, которая вызывает функцию-генератор словарей книг и записывает список сгенерированных словарей в
    json формате в файл dict_books.json.

    :param num_book: Задает кол-во словарей с книгами для генерации. По умолчанию 100.
    :param pk_: Задает начальный автоикримент (счетчик) в функции-генераторе, с которого начинается отсчет при
    генерации.По умолчанию 1.
    :return: None
    """
    with open('dict_books.json', 'w', encoding='utf8') as f:
        book = dict_generator(pk_)
        data = [next(book) for _ in range(num_book)]
        f.write(json.dumps(data, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    """Для генерации нового списка словарей книг прежде необходимо удалить первую строку из файла books.txt,
    содержащую внутреннюю информацию с точками для нахождения позиции курсора на новой строке (0 18 39 68 92 139)
    """
    main()
