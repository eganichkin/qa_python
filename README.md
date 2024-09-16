## qa_python

### Cписок реализованных тестов:

1. test_add_new_book_add_two_books_with_correct_name_book_added(self)
    >Тест метода **add_new_book**. `Входные данные: две книги с корректной длиной наименования. Ожидаемый результат: книги добавлены в словарь "books_genre".`

2. test_add_new_book_add_one_book_with_incorrect_name_book_not_added(self, book_name)
    >Тест метода **add_new_book**. `Входные данные: книги с некорректной длиной наименования. Ожидаемый результат: книги не добавлены в словарь "books_genre".`

3. test_set_book_genre_set_exist_genre_success_setting(self, book_name, genre)
    >Тест метода **set_book_genre**. `Входные данные: добавленной книге устанавливается жанр из списка возможных жанров "genre". Ожидаемый результат: жанр добавлен в словарь "books_genre".`

4. test_set_book_genre_set_not_exist_genre_not_setting(self)
    >Тест метода **set_book_genre**. `Входные данные: добавленной книге устанавливается жанр, не включённый в список возможных жанров "genre". Ожидаемый результат: жанр не добавлен в словарь "books_genre".`

5. test_get_book_genre_add_book_with_exist_genre_get_book_genre(self, book_name, genre)
    >Тест метода **get_book_genre**. `Входные данные: вводится наименование книги с установленным жанром из списка возможных жанров "genre". Ожидаемый результат: выводится соответствующий жанр.`

6. test_get_books_with_specific_genre_get_books_with_exist_genre_get_books(self, books_collector)
    >Тест метода **get_books_with_specific_genre**. `Входные данные: из словаря "books_genre", выбирыются книги жанра из списка "genre". Ожидаемый результат: выводится список книг определённого жанра.`

7. test_get_books_with_specific_genre_get_books_with_not_exist_genre_not_get_books(self, books_collector, genre)
    >Тест метода **get_books_with_specific_genre**. `Входные данные: из словаря "books_genre", выбираются книги жанра, отсутствующего в списке "genre". Ожидаемый результат: выводится пустой список.`

8. test_get_books_genre_add_books_with_different_genre_get_books_genre(self, books_collector, expect_books_genre)
    >Тест метода **get_books_genre_add_books**. `Входные данные: в словарь "books_genre" добавляются книги различного жанра. Ожидаемый результат: выводится весь словарь словарь "books_genre".`

9. test_get_books_for_children_add_books_with_different_genres_get_children_books(self, books_collector)
    >Тест метода **get_books_for_children**. `Входные данные: в словарь "books_genre" добавляются книги различного жанра. Ожидаемый результат: выводятся книги детского жанра.`

10. test_add_book_in_favorites_add_book_from_books_genre_book_added(self, books_collector)
    >Тест метода **add_book_in_favorites**. `Входные данные: добавление двух книг из словаря "books_genre" . Ожидаемый результат: книги добавлены в список "favorites".`

11. test_add_book_in_favorites_add_book_not_from_books_genre_book_not_added(self, books_collector)
    >Тест метода **add_book_in_favorites**. `Входные данные: добавление книги не из словаря "books_genre" . Ожидаемый результат: книга не добавлена в список "favorites".`

12. test_delete_book_from_favorites_delete_one_of_favorites_books_success_deleted(self, books_collector)
    >Тест метода **delete_book_from_favorites**. `Входные данные: удаление книги, наименование которой содержится в списке "favorites" . Ожидаемый результат: удаление осуществлено.`

13. test_delete_book_from_favorites_delete_one_of_not_favorites_books_not_deleted(self, books_collector)
    >Тест метода **delete_book_from_favorites**. `Входные данные: удаление книги, наименование которой не содержится в списке "favorites" . Ожидаемый результат: удаление не осуществлено, список "favorites" не изменился.`

14. test_get_list_of_favorites_books_add_two_books_in_favorites_get_two_books(self, books_collector)
    >Тест метода **get_list_of_favorites_books**. `Входные данные: добавление двух книг в список "favorites" . Ожидаемый результат: Получение этих же двух книг из списка "favorites".`