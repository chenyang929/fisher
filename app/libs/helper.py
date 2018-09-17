def is_isbn_or_key(word):
    """
    :param word: 查询参数
    :return: isbn或key
    """
    isbn_or_key = 'key'
    short_word = word.replace('-', '')
    if len(short_word) in (10, 13) and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
