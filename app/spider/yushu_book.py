from app.libs.req import Http
from flask import current_app


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.books = []
        self.total = 0

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = Http.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = Http.get(url)
        self.__fill_collections(result)

    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config['PER_PAGE']

    def __fill_single(self, data):
        if data:
            self.books.append(data)
            self.total = 1

    def __fill_collections(self, data):
        self.books = data['books']
        self.total = data['total']

    @property
    def first(self):
        return self.books[0] if self.total >=1 else None
