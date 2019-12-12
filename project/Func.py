
def removeTalon(frames_f, talon, newDate, keyWord):
    s = ''
    name = ''
    for frame_n in frames_f:
        if frame_n.name == talon:
            for slot in frame_n.slots:
                if slot.name == keyWord:
                    slot.text = newDate
                    s = slot.lisps[0]()
                if slot.name == 'пациент':
                    name = slot.frame.name
                    return name + ', ' + s + ': ' + newDate


def getFrame(frames_f, word):
    for frame_n in frames_f:
        if frame_n.name == word:
            return frame_n
    return None


def getAnswerBySlot(frames_f, word1, word3):
    for frame_n in frames_f:
        if frame_n.name == word3:
            for slot in frame_n.slots:
                if slot.name == word1:
                    return frame_n
    return None
