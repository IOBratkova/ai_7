from Classes import Frame, TextSlot, InheritanceIndex, ListSlot, AtomSlot, FrameSlot


def updateInfo():
    return 'Update!'


# Список фреймов
frames = []

# Фрейм Больница: адрес, врачи
# Создаем табличку фрейма и пишем в нее заголовое - Больница
hospitalFrame = Frame('Больница')
# Записываем в табличку шаблоны строк без значений. Это адрес и список врачей.
hospitalFrame.slots.append(TextSlot('адрес', InheritanceIndex.u, None))
hospitalFrame.slots.append(ListSlot('доктора', InheritanceIndex.u, None))
frames.append(hospitalFrame)  # frames[0]
"""
Получили табличку такую:
________
Больница
________
Адрес
Врачи
________
и добавили ее в список фреймов
"""

# Фрейм Доктор: стаж, специальность, прием (дни)
doctorFrame = Frame('Доктор')
doctorFrame.slots.append(AtomSlot('стаж', InheritanceIndex.u, None))
doctorFrame.slots.append(TextSlot('специальность', InheritanceIndex.u, None))
doctorFrame.slots.append(TextSlot('прием', InheritanceIndex.u, None))
frames.append(doctorFrame)  # frames[1]

# Фрейм Волкова, наследник врача: стаж=40, специальность=кардиолог, прием=пн-пт
volkovaFrame = Frame('Волкова', frames[1])
experience = 40
speciality = 'кардиолог'
datetime = 'пн-пт'
volkovaFrame.slots.append(AtomSlot('стаж', InheritanceIndex.u, experience))
volkovaFrame.slots.append(TextSlot('специальность', InheritanceIndex.u, speciality))
volkovaFrame.slots.append(TextSlot('прием', InheritanceIndex.u, datetime))
frames.append(volkovaFrame)  # frames[2]

# Фрейм Новиков, наследник врача: стаж=10, специальность=лор, прием=пср-вс
novikovFrame = Frame('Новиков', frames[1])
experience = 10
speciality = 'лор'
datetime = 'ср-вс'
novikovFrame.slots.append(AtomSlot('стаж', InheritanceIndex.u, experience))
novikovFrame.slots.append(TextSlot('специальность', InheritanceIndex.u, speciality))
novikovFrame.slots.append(TextSlot('прием', InheritanceIndex.u, datetime))
frames.append(novikovFrame)  # frames[3]

# Фрейм Неболит, наследник больницы: адрес =ул.ОченьДлинная, врачи = [Волкова, Новиков]
"""
Все так же, как и больничкой, только теперь мы уточняем:
_________________________
Неболит
_________________________
Адрес: ул. Очень длинная
Врачи: Новиков, Волкова
_________________________
"""
nopainFrame = Frame('Неболит', frames[0])
address = 'ул. Очень длинная'
doctors = [frames[2], frames[3]]
nopainFrame.slots.append(TextSlot('адрес', InheritanceIndex.u, address))
nopainFrame.slots.append(ListSlot('врачи', InheritanceIndex.u, doctors))
frames.append(nopainFrame)  # frames[4]

# Фрейм Талон: время, врач, дата
talonFrame = Frame('Талон')
talonFrame.slots.append(TextSlot('дата', InheritanceIndex.u, None))
talonFrame.slots.append(TextSlot('время', InheritanceIndex.u, None))
talonFrame.slots.append(FrameSlot('врач', InheritanceIndex.u, None))
lisp = updateInfo
talonFrame.slots[0].lisps = lisp
frames.append(talonFrame)  # frames[5]

# Фрейм Пациент: талон
patientFrame = Frame('Пациент')
patientFrame.slots.append(FrameSlot('талон', InheritanceIndex.u, None))
frames.append(patientFrame)  # frame[6]

# Фрейм Талон237: дата, время, врач
talon237Frame = Frame('Талон237', frames[5])
date = '02.02.2020'
time = '10:30'
doctor = frames[2]
talon237Frame.slots.append(TextSlot('дата', InheritanceIndex.u, date))
talon237Frame.slots.append(TextSlot('время', InheritanceIndex.u, time))
talon237Frame.slots.append(FrameSlot('врач', InheritanceIndex.u, doctor))
lisp = updateInfo
talon237Frame.slots[0].lisps.append(lisp)
frames.append(talon237Frame)  # frames[7]

# Фрейм Талон217: дата, время, врач
talon217Frame = Frame('Талон217', frames[5])
time = '11:30'
doctor = frames[3]
date = '02.02.2020'
talon217Frame.slots.append(TextSlot('дата', InheritanceIndex.u, date))
talon217Frame.slots.append(TextSlot('время', InheritanceIndex.u, time))
talon217Frame.slots.append(FrameSlot('врач', InheritanceIndex.u, doctor))
lisp = updateInfo
talon237Frame.slots[0].lisps = lisp
frames.append(talon217Frame)  # frames[8]

# Фрейм Костя: талон
kostyaFrame = Frame('Костя', frames[6])
kostyat = frames[7]
kostyaFrame.slots.append(FrameSlot('талон', InheritanceIndex.u, kostyat))
frames.append(kostyaFrame)  # frames[9]

# Фрейм Марина: талон
marinaFrame = Frame('Марина', frames[6])
marinat = frames[8]
marinaFrame.slots.append(FrameSlot('талон', InheritanceIndex.u, marinat))
frames.append(marinaFrame)  # frames[10]

fixFrames = frames
