import enum


#  Класс-фрейм
class Frame:
    def __init__(self, name, parent=None):
        self.name = name
        self.slots = []
        self.parent = parent

    def print_frame(self):
        for slot in self.slots:
            slot.print_slot()

# Указатель типа наследия
class InheritanceIndex(enum.Enum):
    s = 0  # (тот же) - слот наследуется с теми же значениями данных;
    u = 1  # (уникальный) - слот наследуется, но данные в каждом фрейме могут принимать любое значение;
    i = 2  # (независимый) - слот не наследуется.


#  Класс Слот
class Slot:
    def __init__(self, name, inherit):
        self.name = name
        self.inherit = inherit


# Текстовый слот. Текстовая информация
class TextSlot(Slot):
    def __init__(self, name, inherit, text):
        Slot.__init__(self, name, inherit)
        self.text = text
        self.lisps = []

    def print_slot(self):
        return self.name + ", " + self.text


# Атом. Переменная
class AtomSlot(Slot):
    def __init__(self, name, inherit, atom):
        Slot.__init__(self, name, inherit)
        self.atom = atom
        self.lisps = []

    def print_slot(self):
        return self.name + ", " + self.atom


# Список
class ListSlot(Slot):
    def __init__(self, name, inherit, array):
        Slot.__init__(self, name, inherit)
        self.array = array
        self.lisps = []

    def array_to_text(self):
        global s
        for text in self.array:
            s = s + text.name
        return s

    def print_slot(self):
        return self.array_to_text(self)


# Фрейм-слот. указывает имя фрейма верхнего уровня
class FrameSlot(Slot):
    def __init__(self, name, inherit, frame):
        Slot.__init__(self, name, inherit)
        self.lisps = []

    def print_slot(self):
        return self.print_slot(self.frame)

        self.frame = frame

# Лисп-слот. присоединенная процедура
class LispSlot(Slot):
    def __init__(self, name, inherit, lsp):
        Slot.__init__(self, name, inherit)
        self.lsp = lsp


