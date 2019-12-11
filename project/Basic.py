from Classes import Frame, TextSlot, InheritanceIndex, ListSlot, AtomSlot

frames = []

# Фрейм Больница: Название, Адрес
hospital = Frame('Больница')  # Первый фрейм больница
hospital.slots.append(TextSlot('адрес', InheritanceIndex.u, ''))
hospital.slots.append(TextSlot('название', InheritanceIndex.u, ''))
hospital.slots.append(ListSlot('врачи', InheritanceIndex.u, ''))
frames.append(hospital)

# Фрейм Врач: Имя, специализация, дни приема, стаж
doctor = Frame('Врач')
doctor.slots.append(TextSlot('Имя', InheritanceIndex.u, ''))
doctor.slots.append(TextSlot('Специализация', InheritanceIndex.u, ''))
doctor.slots.append(TextSlot('Дни приема', InheritanceIndex.u, ''))
doctor.slots.append(AtomSlot('Стаж', InheritanceIndex.u, ''))
frames.append(doctor)

# конкретный врач
мщд

