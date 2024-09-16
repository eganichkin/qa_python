import pytest

from main import BooksCollector


@pytest.fixture
def books_collector():
    collector = BooksCollector()

    collector.add_new_book('Ну погоди')
    collector.set_book_genre('Ну погоди', 'Мультфильмы')

    collector.add_new_book('Оно')
    collector.set_book_genre('Оно', 'Ужасы')

    collector.add_new_book('Шерлок хомс')
    collector.set_book_genre('Шерлок хомс', 'Детективы')

    collector.add_new_book('Лунтик')
    collector.set_book_genre('Лунтик', 'Мультфильмы')

    collector.add_new_book('Война и мир')
    collector.set_book_genre('Война и мир', 'Роман')

    collector.add_new_book('Мгла')
    collector.set_book_genre('Мгла', 'Ужасы')

    collector.add_new_book('Маугли')

    return collector


@pytest.fixture
def expect_books_genre():
    return {'Ну погоди': 'Мультфильмы',
            'Оно': 'Ужасы',
            'Шерлок хомс': 'Детективы',
            'Лунтик': 'Мультфильмы',
            'Война и мир': '',
            'Мгла': 'Ужасы',
            'Маугли': ''}
