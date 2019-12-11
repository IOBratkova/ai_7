from typing import List

from Classes import Frame, TextSlot, InheritanceIndex, ListSlot, AtomSlot

frames = []

# Фрейм Больница: Название, Адрес
hospital = Frame('Больница')
# hospital.slots.append(TextSlot('название', InheritanceIndex.u, ''))
hospital.slots.append(TextSlot('адрес', InheritanceIndex.u, ''))
hospital.slots.append(ListSlot('врачи', InheritanceIndex.u, ''))
frames.append(hospital)

# Фрейм Врач: Имя, специализация, дни приема, стаж
doctor = Frame('Врач')
# doctor.slots.append(TextSlot('Имя', InheritanceIndex.u, ''))
doctor.slots.append(TextSlot('Специализация', InheritanceIndex.u, ''))
doctor.slots.append(TextSlot('Дни приема', InheritanceIndex.u, ''))
doctor.slots.append(AtomSlot('Стаж', InheritanceIndex.u, ''))
frames.append(doctor)

# конкретный врач
index = frames.index(doctor)

doctor1 = Frame('Волкова', frames[index])
# doctor1.slots.append(TextSlot('Имя', InheritanceIndex.u, 'Волкова'))
doctor1.slots.append(TextSlot('Специализация', InheritanceIndex.u, 'Кардиолог'))
doctor1.slots.append(TextSlot('Дни приема', InheritanceIndex.u, 'пн-пт'))
doctor1.slots.append(AtomSlot('Стаж', InheritanceIndex.u, 40))
frames.append(doctor1)

doctor2 = Frame('Новиков', frames[index])
# doctor2.slots.append(TextSlot('Имя', InheritanceIndex.u, 'Новиков'))
doctor2.slots.append(TextSlot('Специализация', InheritanceIndex.u, 'Лор'))
doctor2.slots.append(TextSlot('Дни приема', InheritanceIndex.u, 'ср-вск'))
doctor2.slots.append(AtomSlot('Стаж', InheritanceIndex.u, 25))
frames.append(doctor2)

# Больница Неболит

index = frames.index(hospital)
nopain = Frame('Неболит', frames[index])
nopain.slots.append('адрес', InheritanceIndex.u, 'ул. Городская, дом 55')
nopain.slots.append('врачи', InheritanceIndex.u, [doctor1, doctor2])

