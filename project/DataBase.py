from Classes import Frame, TextSlot, InheritanceIndex, ListSlot, AtomSlot
frames = []
# Фрейм Больница: Название, Адрес.
hospitalFrame = Frame('Больница')
hospitalFrame.slots.append(TextSlot('адрес', InheritanceIndex.u, None))
hospitalFrame.slots.append(ListSlot('врачи', InheritanceIndex.u, None))
frames.append(hospitalFrame) # frames[0]

doctorFrame = Frame('Доктор')
doctorFrame.slots.append(AtomSlot('стаж', InheritanceIndex.u, None))
doctorFrame.slots.append(TextSlot('специальность', InheritanceIndex.u, None))
doctorFrame.slots.append(TextSlot('прием', InheritanceIndex.u, None))
frames.append(doctorFrame) # frames[1]

volkovaFrame = Frame('Волкова', frames[1])
experience = 40
speciality = 'кардиолог'
datetime = 'пнд-птн'
volkovaFrame.slots.append(AtomSlot('стаж', InheritanceIndex.u, experience))
volkovaFrame.slots.append(TextSlot('специальность', InheritanceIndex.u, speciality))
volkovaFrame.slots.append(TextSlot('прием', InheritanceIndex.u, datetime))
frames.append(volkovaFrame) # frames[2]

novikovFrame = Frame('Новиков', frames[1])
experience = 10
speciality = 'лор'
datetime = 'ср-вск'
novikovFrame.slots.append(AtomSlot('стаж', InheritanceIndex.u, experience))
novikovFrame.slots.append(TextSlot('специальность', InheritanceIndex.u, speciality))
novikovFrame.slots.append(TextSlot('прием', InheritanceIndex.u, datetime))
frames.append(novikovFrame) # frames[3]

nopainFrame = Frame('Неболит', frames[0])
address = 'ул. Очень длинная, дом Крайне Высокий'
doctors = [frames[2], frames[3]]
nopainFrame.slots.append(TextSlot('адрес', InheritanceIndex.u, address))
nopainFrame.slots.append(ListSlot('врачи', InheritanceIndex.u, doctors))
frames.append(nopainFrame) # frames[4]
