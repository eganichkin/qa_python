import pytest

from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books_with_correct_name_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('book_name',
                             ['', 'Что делать, если ваш кот хочет вас убить?'])
    def test_add_new_book_add_one_book_with_incorrect_name_book_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize('book_name, genre',
                             [['Оно', 'Ужасы'], ['Лунтик', 'Мультфильмы']])
    def test_set_book_genre_set_exist_genre_success_setting(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    def test_set_book_genre_set_not_exist_genre_not_setting(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Роман')
        assert collector.books_genre['Война и мир'] == ''

    @pytest.mark.parametrize('book_name, genre',
                             [['Оно', 'Ужасы'], ['Лунтик', 'Мультфильмы']])
    def test_get_book_genre_add_book_with_exist_genre_get_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_get_books_with_exist_genre_get_books(self, books_collector):
        assert books_collector.get_books_with_specific_genre('Ужасы') == ['Оно', 'Мгла']

    @pytest.mark.parametrize('genre', ['', 'Романы'])
    def test_get_books_with_specific_genre_get_books_with_not_exist_genre_not_get_books(self, books_collector, genre):
        assert books_collector.get_books_with_specific_genre(genre) == []

    def test_get_books_genre_add_books_with_different_genre_get_books_genre(self, books_collector, expect_books_genre):
        assert books_collector.get_books_genre() == expect_books_genre

    def test_get_books_for_children_add_books_with_different_genres_get_children_books(self, books_collector):
        assert books_collector.get_books_for_children() == ['Ну погоди', 'Лунтик']

    def test_add_book_in_favorites_add_book_from_books_genre_book_added(self, books_collector):
        books_collector.add_book_in_favorites('Лунтик')
        books_collector.add_book_in_favorites('Мгла')
        assert books_collector.favorites == ['Лунтик', 'Мгла']

    def test_add_book_in_favorites_add_book_not_from_books_genre_book_not_added(self, books_collector):
        books_collector.add_book_in_favorites('Геракл')
        assert books_collector.favorites == []

    def test_delete_book_from_favorites_delete_one_of_favorites_books_success_deleted(self, books_collector):
        books_collector.add_book_in_favorites('Лунтик')
        books_collector.add_book_in_favorites('Мгла')
        books_collector.delete_book_from_favorites('Лунтик')
        assert books_collector.favorites == ['Мгла']

    def test_delete_book_from_favorites_delete_one_of_not_favorites_books_not_deleted(self, books_collector):
        books_collector.add_book_in_favorites('Лунтик')
        books_collector.add_book_in_favorites('Мгла')
        books_collector.delete_book_from_favorites('Геракл')
        assert books_collector.favorites == ['Лунтик', 'Мгла']

    def test_get_list_of_favorites_books_add_two_books_in_favorites_get_two_books(self, books_collector):
        books_collector.add_book_in_favorites('Лунтик')
        books_collector.add_book_in_favorites('Мгла')
        assert books_collector.favorites == ['Лунтик', 'Мгла']
