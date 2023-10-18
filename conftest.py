from main import BooksCollector
import pytest
from data import BOOKS_COLLECTION, GENRE_LIST


@pytest.fixture
def new_book(name='Новая книга'):
    ''' Функция создания коллекции и добавления 1 книги '''
    collect = BooksCollector()
    collect.add_new_book(name)
    return collect

@pytest.fixture
def new_book_with_genre(new_book):
    ''' Функция создания коллекции и добавления 1 книги с жанром '''
    name = 'Новая книга'
    genre = 'Фантастика'
    collect = new_book
    collect.set_book_genre(name, genre)
    return collect

@pytest.fixture
def collection():
    ''' Функция создания коллекции из 5-ти книг 5-ти разных жанров '''
    collection = BooksCollector()
    name, genre = BOOKS_COLLECTION[0], GENRE_LIST[0]
    collection.add_new_book(name)
    collection.set_book_genre(name, genre)
    name, genre = BOOKS_COLLECTION[1], GENRE_LIST[1]
    collection.add_new_book(name)
    collection.set_book_genre(name, genre)
    name, genre = BOOKS_COLLECTION[2], GENRE_LIST[2]
    collection.add_new_book(name)
    collection.set_book_genre(name, genre)
    name, genre = BOOKS_COLLECTION[3], GENRE_LIST[3]
    collection.add_new_book(name)
    collection.set_book_genre(name, genre)
    name, genre = BOOKS_COLLECTION[4], GENRE_LIST[4]
    collection.add_new_book(name)
    collection.set_book_genre(name, genre)
    return collection

