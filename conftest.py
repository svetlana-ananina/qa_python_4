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
    for i in range(len(BOOKS_COLLECTION)):
        name = BOOKS_COLLECTION[i]
        genre = GENRE_LIST[i]
        collection.add_new_book(name)
        collection.set_book_genre(name, genre)
    return collection

