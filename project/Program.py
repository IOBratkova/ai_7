from DataBase import frames
from Classes import Slot, TextSlot, InheritanceIndex

print('Hello, Im frame-program')

flag = True


def removeTalon(frames_f, talon, newDate):
    for frame in frames_f:
        if frame.name == talon:
            for slot in frame.slots:
                if slot.name == 'дата':
                    slot.text = newDate
                    slot.lisps[0]()


def getFrame(frames_f, word):
    for frame in frames_f:
        if frame.name == word:
            return frame
    return None


def getAnswerBySlot(frames_f, word1, word3):
    for frame in frames_f:
        if frame.name == word3:
            for slot in frame.slots:
                if slot.name == word1:
                    return frame
    return None


while flag:
    question = input()
    if question == 'стоп' or question == 'stop':
        print('Пока-пока')
        flag = False
    question = question[0:-1]
    question = question.split()
    if question[1] == 'изменить':
        # Хочу изменить дата у Талон237 на 20.20.5000
        tmp = frames[7]
        removeTalon(frames, question[4], question[6])
        break
    answer = getFrame(frames, question[2])
    if answer is None:
        answer = getAnswerBySlot(frames, question[1], question[3])
    print(answer.frameToString())

"""
Хочу удалить Талон237
Cреди frames найдем Талон237
Taлон237: поставим все в None
Найдем чувака, у которого есть этот Талон
Поставим ему None вместо талона





class A:
    def __init__(self, v):
        self.v = v

    def print_v(self):
        print(self.v)


a = A(10)
a.v = 55
a.print_v()

f = a.print_v
a.v = 199
f()


>>> a = A()
>>> a.v = 91
>>> a.print_me()
91
>>> f = a.print_me
>>> a.v = 155
>>> f()
155
>>>
"""
