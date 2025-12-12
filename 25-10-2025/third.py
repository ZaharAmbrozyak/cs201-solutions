class TextManager:
    def __init__(self, text=None):
        if text:
            self.text = text
        else:
            self.text = ''

        self.buffer = ''
        self.history = []

    def add_at_the_end(self, more_text: str) -> None:
        """
        В текст можна додавати новий текст в кінець
        """
        self.text = self.text + more_text

    def insert(self, text: str, line: int, char_i: int) -> None:
        """
        Можна додавати текст в середину по координатам:
        def insert(text: str, line: int, char_i: int)
        """
        self.history.append(self.text)

        line -= 1
        char_i -= 1
        lines = [[ch for ch in line] for line in self.text.split(sep='\n')]
        symbols_text = [ch for ch in text]
        for i in range(len(symbols_text)):
            lines[line].insert(char_i, symbols_text[i])
            char_i += 1
        new_text = '\n'.join([''.join(line) for line in lines])
        self.text = new_text

    def copy(self, line1: int, char_i1: int, line2: int, char_i2: int) -> None:
        line1 -= 1
        char_i1 -= 1
        line2 -= 1
        char_i2 -= 1

        lines = [[ch for ch in line] for line in self.text.split(sep='\n')]

        text_to_copy = []
        for line in range(line1, line2+1):
            for char_i in range(char_i1 if line == line1 else 0, (char_i2 if line == line2 else len(lines[line]))):
                text_to_copy.append(lines[line][char_i])
        self.buffer = ''.join(text_to_copy)

    def delete(self, line: int, char_i: int, char_count: int) -> None:
        self.history.append(self.text)
        line -= 1
        char_i -= 1
        lines = [[ch for ch in ln] for ln in self.text.split(sep='\n')]
        for i in range(char_i, char_i-char_count, -1):
            lines[line][i] = ''

        new_text = '\n'.join([''.join(line) for line in lines])
        self.text = new_text

    def previous(self):
        try:
            self.text = self.history[-1]
            del self.history[-1]
        except Exception:
            print("There's no history")

    def cut(self, line1: int, char_i1: int, line2: int, char_i2: int) -> None:
        pass

    def paste(self) -> str:
        return self.buffer

    def show_text(self) -> None:
        print(self.text)

    def show_buffer(self) -> None:
        print(self.buffer)

    def __str__(self):
        return self.text

def print_underlines():
    print('-'*10)

my_text = """Serafym gave me a nice task.\nI liked it :)\nbo  bo\n123"""
my_text_manager = TextManager(my_text)

print_underlines()

print("TestCase1: insert method, text='alalalalla', line=3, char_i=4")
my_text_manager.insert('alalalalla', 3, 4)
print(my_text_manager)

print_underlines()

print("TestCase2: copy method, line1=1, char_i1=1, line2=2, char_i2=2")
my_text_manager.copy(1, 1, 2, 2)
my_text_manager.show_buffer()

print_underlines()

print("TestCase3: delete method, line=1, char_i=7, char_count=7")
my_text_manager.delete(1, 7, 7)
my_text_manager.show_text()

print_underlines()

print('TestCase4: previous method')
my_text_manager.previous()
print(my_text_manager)



