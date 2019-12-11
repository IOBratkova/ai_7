from Classes import Frame, TextSlot, InheritanceIndex, ListSlot

frames = []

# Фрейм Больница
# Название
# Адрес
tmpFrame = Frame('Больница')  # Первый фрейм больница
tmpFrame.slots.append(TextSlot('адрес', InheritanceIndex.u, ''))
tmpFrame.slots.append(TextSlot('название', InheritanceIndex.u, ''))
tmpFrame.slots.append(ListSlot('врачи', InheritanceIndex.u, ''))

# Добавляем больницу в список фреймов
frames.append(frames)

# Фрейм Неболит, родитель - больница
# Название
# Адрес
# Список врачей
tmpFrame = Frame('Неболит', frames[0])
tmpFrame.slots.append(TextSlot('адрес', InheritanceIndex.u, 'ул. Городская, д. 74'))
tmpFrame.slots.append(TextSlot('название', InheritanceIndex.u, 'Неболит'))
