import enum


#  Класс-фрейм
class Frame:
    def __init__(self, name, parent=None):
        self.name = name
        self.slots = []
        self.parent = parent

    def __eq__(self, other):
        return self.name == other.name \
               and self.parent == other.parent \
               and self.slots == other.slots

    def frameToString(self):
        slots = ''
        for slot in self.slots:
            slots += slot.name + ', '
        slots = slots[0: -2]
        if self.parent is None:
            tmp = 'Нет'
        else:
            tmp = self.parent.name
        return 'Название: ' + self.name + \
               ', родитель: ' + tmp + \
               ', слоты: [' + slots + ']'

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

    def __eq__(self, other):
        return self.name == other.name and self.inherit == other.inherit


# Текстовый слот. Текстовая информация
class TextSlot(Slot):
    def __init__(self, name, inherit, text):
        Slot.__init__(self, name, inherit)
        self.text = text
        self.lisps = []

    def __eq__(self, other):
        #return self.__eq__(other) and  self.lisps == other.lisps and self.text == other.text
        return Slot.__eq__(self, other) and self.lisps == other.lisps and self.text == other.text


# Атом. Переменная
class AtomSlot(Slot):
    def __init__(self, name, inherit, atom):
        Slot.__init__(self, name, inherit)
        self.atom = atom
        self.lisps = []

    def __eq__(self, other):
        return Slot.__eq__(self, other) and self.lisps == other.lisps and self.atom == other.atom


# Список
class ListSlot(Slot):
    def __init__(self, name, inherit, array):
        Slot.__init__(self, name, inherit)
        self.array = array
        self.lisps = []

    def __eq__(self, other):
        return Slot.__eq__(self, other) and self.lisps == other.lisps and self.array == other.array


# Фрейм-слот. указывает имя фрейма верхнего уровня
class FrameSlot(Slot):
    def __init__(self, name, inherit, frame):
        Slot.__init__(self, name, inherit)
        self.frame = frame
        self.lisps = []

    def __eq__(self, other):
        return Slot.__eq__(self, other) and self.lisps == other.lisps and self.frame == other.frame

# Лисп-слот. присоединенная процедура
class LispSlot(Slot):
    def __init__(self, name, inherit, lsp):
        Slot.__init__(self, name, inherit)
        self.lsp = lsp

    def __eq__(self, other):
        return Slot.__eq__(self, other) and self.lsp == other.lsp


