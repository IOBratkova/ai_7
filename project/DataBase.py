from Classes import Frame, TextSlot, InheritanceIndex, ListSlot, AtomSlot, FrameSlot

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

talonFrame = Frame('Талон')
talonFrame.slots.append(TextSlot('время', InheritanceIndex.u, None))
talonFrame.slots.append(FrameSlot('врач', InheritanceIndex.u, None))
frames.append(talonFrame) # frames[5]

patientFrame = Frame('Пациент')
patientFrame.slots.append(FrameSlot('талон', InheritanceIndex.u, None))
frames.append(patientFrame) #frame[6]

talon237Frame = Frame('Талон237', frames[5])
time = '10:30'
doctor = frames[2]
talon237Frame.slots.append(TextSlot('время', InheritanceIndex.u, time))
talon237Frame.slots.append(FrameSlot('врач', InheritanceIndex.u, doctor))
frames.append(talon237Frame) #frames[7]

talon217Frame = Frame('Талон217', frames[5])
time = '11:30'
doctor = frames[3]
talon217Frame.slots.append(TextSlot('время', InheritanceIndex.u, time))
talon217Frame.slots.append(FrameSlot('врач', InheritanceIndex.u, doctor))
frames.append(talon217Frame) #frames[8]

kostyaFrame = Frame('Костя', frames[6])
kostyat = frames[7]
kostyaFrame.slots.append(FrameSlot('талон', InheritanceIndex.u, kostyat))
frames.append(kostyaFrame) #frames[9]

marinaFrame = Frame('Марина', frames[6])
marinat = frames[8]
marinaFrame.slots.append(FrameSlot('талон', InheritanceIndex.u, marinat))
frames.append(marinaFrame) #frames[9]


