from constants import MORSE_SPACE_SYMBOL, MORSE_SPACE_WORD, TEXT_SPACE_SYMBOL, TEXT_SPACE_WORD, MORSE_DASH, MORSE_DOT
from data import DICT


# - - - - - - - - - - - - - - - TRANSLATOR - - - - - - - - - - - - - - -

class MorseCodeTranslator:
 
    def __init__(self) -> None:
        self.TABLE = DICT
        self.TREE = MorseTree()

    def encrypt(self, string) -> str:
        """
        Morse encryption using the table.
        (Alphabetical symbol -> Morse code dots and dashes)
        """
        return MORSE_SPACE_WORD.join((MORSE_SPACE_SYMBOL.join(self.__get_code_from_symbol(symbol) for symbol in word) for word in string.split(TEXT_SPACE_WORD)))
 
    def decrypt(self, string) -> str: 
        """
        Morse decryption using the binary tree.
        (Morse code dots and dashes -> Alphabetical symbol)
        """
        return TEXT_SPACE_WORD.join(TEXT_SPACE_SYMBOL.join(self.__get_symbol_from_code(code) for code in word.split(MORSE_SPACE_SYMBOL)) for word in string.split(MORSE_SPACE_WORD))
 
    def __get_code_from_symbol(self, symbol):
        return self.TABLE[symbol]
    
    def __get_symbol_from_code(self, code):
        return self.TREE.get_symbol(code)
    

# - - - - - - - - - - - - - - - TREE - - - - - - - - - - - - - - -

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class MorseTree:
    def __init__(self):
        self.root = Node()
        # Initialize the tree
        for k, v in DICT.items():
            self.__add(k, v)

    def __add(self, letter, code):
        node = self.root
        for symbol in code:
            if symbol == MORSE_DOT:
                if node.left is None:
                    node.left = Node()
                node = node.left
            elif symbol == MORSE_DASH:
                if node.right is None:
                    node.right = Node()
                node = node.right
        node.value = letter
    
    def get_symbol(self, code):
        node = self.root
        for symbol in code:
            if symbol == MORSE_DOT:
                node = node.left
            elif symbol == MORSE_DASH:
                node = node.right
        return node.value