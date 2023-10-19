from main import BooksCollector
import pytest
from data import GENRE_LIST, GENRE_FOR_CHLDREN, GENRE_AGE_RATING


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        ''' Проверка добавления двух книг '''
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['',
                                      '12345678901234567890123456789012345678901'])
    def test_add_new_book_invalid_name_not_added(self, name):
        ''' Проверка добавления книги с недопустимым названием - длина 0 символов и 41 символ '''
        collect = BooksCollector()
        collect.add_new_book(name)
        assert len(collect.get_books_genre()) == 0

    def test_add_new_book_double_not_added(self):
        ''' Проверка повторного добавление книги '''
        collect = BooksCollector()
        collect.add_new_book('Одна и та же книга')
        collect.add_new_book('Одна и та же книга')
        assert len(collect.get_books_genre()) == 1

    def test_add_new_book_has_not_genre(self, new_book):
        ''' Проверка, что у добавленной книги нет жанра '''
        collect = new_book
        assert collect.get_book_genre('Новая книга') == ''

    def test_set_book_genre_added(self, new_book, new_book_with_genre):
        ''' Проверка добавления жанра для книги '''
        name = 'Новая книга'
        genre = 'Фантастика'
        collect = new_book_with_genre
        assert collect.get_book_genre(name) == genre


    def test_set_book_genre_changed(self, new_book, new_book_with_genre):
        ''' Проверка изменения жанра для книги '''
        name = 'Новая книга'
        genre = 'Ужасы'
        collect = new_book_with_genre
        collect.set_book_genre(name, genre)
        assert collect.get_book_genre(name) == genre

    def test_set_book_genre_invalid_genre_not_added(self, new_book):
        ''' Проверка добавления недопустимого жанра для книги '''
        name = 'Новая книга'
        genre = 'Сказки'
        collect = new_book
        collect.set_book_genre(name, genre)
        assert collect.get_book_genre(name) == ''

    def test_set_book_genre_missing_book_not_added(self, new_book):
        ''' Проверка добавления жанра для отсутствующей в коллекции книги '''
        name = ''
        genre = 'Фантастика'
        collect = new_book
        collect.set_book_genre(name, genre)
        assert not collect.get_book_genre(name)

    def test_get_books_for_children_success(self, collection):
        ''' Проверка получения списка книг для детей '''
        collect = collection
        children_books = collect.get_books_for_children()
        assert (len(children_books) == 3)

    def test_get_books_for_children_has_not_age_rating(self, collection_two_books_with_genre):
        ''' Проверка. что в списке книг для детей отсутствуют книги с возрастным рейтингом '''
        collect = collection_two_books_with_genre
        children_books = collect.get_books_for_children()
        assert (len(children_books) == 1 and
                collect.get_book_genre(children_books[0]) in GENRE_FOR_CHLDREN and
                collect.get_book_genre(children_books[0]) not in GENRE_AGE_RATING
                 )

    @pytest.mark.parametrize('genre', GENRE_LIST)
    def test_get_books_with_specific_genre_success(self, collection, genre):
        ''' Проверка получения книг по жанру '''
        collect = collection
        specific_books = collect.get_books_with_specific_genre(genre)
        assert (len(specific_books) == 1 and
                collect.get_book_genre(specific_books[0]) == genre
                )

    @pytest.mark.parametrize('genre', ['Сказки', 'Ужасы'])
    def test_get_books_with_specific_genre_invalid_or_missing(self, new_book, new_book_with_genre, genre):
        ''' Проверка получения книг по жанру - неверный жанр или отсутствует в коллекции '''
        collect = new_book_with_genre
        specific_books = collect.get_books_with_specific_genre(genre)
        assert len(specific_books) == 0

    def test_add_book_in_favorites_added(self, new_book_with_genre):
        ''' Проверка добавления книги в избранное '''
        collect = new_book_with_genre
        name = 'Новая книга'
        collect.add_book_in_favorites(name)
        favorites = collect.get_list_of_favorites_books()
        assert ( len(favorites) == 1 and favorites[0] == name )

    def test_add_book_in_favorites_missing_book_not_added(self, new_book_with_genre):
        ''' Проверка добавления книги в избранное - если книги нет в коллекции, не добавляется '''
        collect = new_book_with_genre
        name = 'Другая книга'
        collect.add_book_in_favorites(name)
        favorites = collect.get_list_of_favorites_books()
        assert len(favorites) == 0

    def test_add_book_in_favorites_double_not_added(self, new_book_with_genre):
        ''' Проверка, что дубль не добавляется в избранное '''
        collect = new_book_with_genre
        name = 'Новая книга'
        collect.add_book_in_favorites(name)
        collect.add_book_in_favorites(name)
        favorites = collect.get_list_of_favorites_books()
        assert ( len(favorites) == 1 and favorites[0] == name )

    def test_delete_book_from_favorites_deleted(self, new_book_with_genre):
        ''' Проверка удаления книги из избранного '''
        collect = new_book_with_genre
        name = 'Новая книга'
        collect.add_book_in_favorites(name)
        collect.delete_book_from_favorites(name)
        favorites = collect.get_list_of_favorites_books()
        assert len(favorites) == 0

    def test_delete_book_from_favorites_missing_book_not_deleted(self, new_book_with_genre):
        ''' Проверка удаления книги из избранного, если такой книги нет в избранном '''
        collect = new_book_with_genre
        name = 'Новая книга'
        other_name = 'Другая книга'
        collect.add_book_in_favorites(name)
        collect.delete_book_from_favorites(other_name)
        favorites = collect.get_list_of_favorites_books()
        assert ( len(favorites) == 1 and favorites[0] == name )
