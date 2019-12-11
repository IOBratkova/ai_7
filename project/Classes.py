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

    """
     Делает строку из списка слотов.
     slotType - тип пришедшего в метод слота.
     В зависимости от типа возвращает его значение (см классы).
     Если натыкается на ListSlot, то выписывает последовательно значения name из него.
     Если натыкатеся на FrameSlot, то выписывает имя фрейма, которое в нем лежит.
     Возвращает Нет, если в слоте нет значения или произошла ошибка.
     return 'Нет' if s is None else s.__str__() 
     последнее нужно для того, чтобы преобразовать ответ в строку. 
    """

    def slotsToString(self, oneSlot):
        slotType = type(oneSlot)
        try:
            if slotType == AtomSlot:
                s = oneSlot.atom
            elif slotType == TextSlot:
                s = oneSlot.text
            elif slotType == FrameSlot:
                s = oneSlot.frame.name
            elif slotType == ListSlot:
                s = ''
                for element in oneSlot.array:
                    s += element.name + ', '
                s = s[0: -2]
            else:
                s = 'Нет'
        except Exception:
            s = 'Нет'
        return 'Нет' if s is None else s.__str__()

    """
    Превращаем фрейм в строку. 
    Последоватеьно перебирает слоты фрейма и преобразует каждый из них в строку (см выше).
    Записывает имя фрейма-родителя, если он есть, иначе пишет Нет.
    Возвращает в порядке 
    Название: <текст>, родитель: <текст>, слоты: [<слот1=значение>,..., <слотN=значение>]
    """

    def frameToString(self):
        slots = ''
        for slot in self.slots:
            s = self.slotsToString(slot)
            slots += slot.name + ' = ' + s + ', '
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


#  Класс Слот.  Конструктор и метод сравнения
class Slot:
    def __init__(self, name, inherit):
        self.name = name
        self.inherit = inherit

    def __eq__(self, other):
        return self.name == other.name and self.inherit == other.inherit


# Текстовый слот. Текстовая информация
# В остальных классах все аналогично
class TextSlot(Slot):

    # Конструктор
    # Сначала вызов конструктора бати: Slot.__init__(self, name, inherit)
    # А потом конкретно наши значения self.text = text, self.lisps = []
    def __init__(self, name, inherit, text):
        Slot.__init__(self, name, inherit)
        self.text = text
        self.lisps = []

    # Сравнение очень похоже на конструктор
    # Сначала вызываем сравнение бати: Slot.__eq__(self, other)
    # А потом свои собственные сравнения: self.lisps == other.lisps and self.text == other.text
    def __eq__(self, other):
        return Slot.__eq__(self, other) \
               and self.lisps == other.lisps \
               and self.text == other.text


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
