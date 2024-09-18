import pytest

from main import BooksCollector


@pytest.fixture
def expect_books_genre():
    return {'Ну погоди': 'Мультфильмы',
            'Оно': 'Ужасы',
            'Шерлок хомс': 'Детективы',
            'Лунтик': 'Мультфильмы',
            'Война и мир': '',
            'Мгла': 'Ужасы',
            'Маугли': ''}


@pytest.fixture
def books_collector(expect_books_genre):
    collector = BooksCollector()
    for key, value in expect_books_genre.items():
        collector.add_new_book(key)
        collector.set_book_genre(key, value)

    return collector
