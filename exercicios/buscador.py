import sys
import unicodedata

def buscar(*palavras_chave):
    """ Busca por caracteres que contenham a palavra chave em seu nome.
    Ex:
    
    >>> from exercicios.buscador import buscar
    >>> dict(buscar('BLACK', 'suit'))
    {'♠': 'BLACK SPADE SUIT', '♣': 'BLACK CLUB SUIT', '♥': 'BLACK HEART SUIT', '♦': 'BLACK DIAMOND SUIT'}
    >>> dict(buscar('BlAcK', 'suit', 'ClUb'))
    {'♣': 'BLACK CLUB SUIT'}
    >>> dict(buscar('chess', 'king'))
    {'♔': 'WHITE CHESS KING', '♚': 'BLACK CHESS KING'}
    
    :param palavras_chave: tupla de strings
    :return: generator onde cada elemento é uma tupla. O primeiro elemento da 
    tupla é o caracter e o segundo é seu nome. Assim ele pode ser utilizado no
    construtor de um dicionário
    """
    limite = 0
    max_unicode_value = sys.maxunicode
    palavras_lower = [palavra.lower() for palavra in palavras_chave]
    while limite < max_unicode_value:
        caracter = chr(limite)
        try:
            unicode_name_lower = unicodedata.name(caracter).lower()
        except ValueError:
            pass
        else:
            if all([palavra in unicode_name_lower for palavra in palavras_lower]):
                yield (caracter, unicode_name_lower.upper())
        finally:
            limite += 1
