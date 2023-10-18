# Тесты для проверки методов класса  BooksCollector
Файлы: 
- main.py - описание класса BooksCollector
- tests.py - набор тестов
- conftest.py - вспомогательные функции для тестов (фикстуры)
- data.py - константы для тестов

## Набор тестов реализован в классе TestBooksCollector

Методы класса:
- test_add_new_book_add_two_books - проверка добавления двух книг
- test_add_new_book_invalid_name_not_added (2 теста) - проверка добавления книги с недопустимым названием
- test_add_new_book_double_not_added - проверка повторного добавления книги
- test_add_new_book_has_not_genre - проверка, что у добавленной книги нет жанра
- test_set_book_genre_added - проверка добавления жанра для книги
- test_set_book_genre_changed - проверка изменения жанра для книги
- test_set_book_genre_invalid_genre_not_added - проверка добавления неправильного жанра для книги
- test_set_book_genre_missing_book_not_added - проверка добавления жанра для отсутствующей в коллекции книги
- test_get_books_for_children_success - проверка получения списка книг для детей
- test_get_books_for_children_has_not_age_rating - проверка, что в списке книг для детей отсутствуют книги с возрастным рейтингом
- test_get_books_with_specific_genre_success (5 тестов) - проверка получения книг по жанру
- test_get_books_with_specific_genre_invalid_or_missing (2 теста) - проверка получения книг по жанру - неверный жанр или отсутствует в коллекции
- test_add_book_in_favorites_added - проверка добавления книги в избранное
- test_add_book_in_favorites_missing_book_not_added - проверка добавления книги в избранное, если книги нет в коллекции
- test_add_book_in_favorites_double_not_added - проверка повторного добавления книги в избранное
- test_delete_book_from_favorites_deleted - проверка удаления книги из избранного
- test_delete_book_from_favorites_missing_book_not_deleted - проверка удаления книги из избранного, если такой книги нет в избранном

Реализовано 23 теста со 100% покрытием класса BooksCollector, с учетом ветвления.

- Для запуска тестов должен быть установлен пакет pytest
- Запуск всех тестов выполняется командой: pytest -v tests.py
- Результат выполнения тестов - 100% PASSED
