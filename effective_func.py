import random


def title_() -> str:
    """
    Эффективная функция возвращает случайное название книги из файла books.txt
    :return: Название книги в виде str
    """
    path = 'books.txt'
    with open(path) as f:
        cursor = f.readline().split()
        del(cursor[0])
        f.seek(int(random.choice(cursor)), 0)
        book = f.readline()
        return book


if __name__ == "__main__":
    title_()
