from DataBase import frames
"""
Что можно писать?
+ Стоп-слово: 'стоп' или 'stop'

+ Названия фреймов (с точкой в конце): Больница, Доктор, Пациент, Талон, 
                                       Костя, Марина, Новиков, Волкова, 
                                       Неболит, Талон237, Талон217
                                       
+ Слово Все (с точкой в конце) - "Все." = все фреймы

+ Вопросы типа  Какой адрес у Неболит?
                Какой талон у Марина?
                Какая дата у Талон217?
                Какой врач у Талон237?    
                    
+ Вопросы типа Что такое Неболит?
               Кто такой Новиков?
               Кто такая Волкова?
               Кто такая Марина?

+ Попросить изменить (с точкой в конце):    Хочу изменить дата у Талон237 на 20.12.1996г.
                                            Хочу изменить дата у Талон217 на 20.10.1996г.
                                            Хочу изменить время у Талон237 на 11:33.
                                            Хочу изменить время у Талон217 на 13:50.
"""



flag = True
while flag:
    question = input()

    # Выход из программы
    if question == 'стоп' or question == 'stop':
        print('Пока-пока')
        flag = False
        continue

    # С этого момента писать все со знаками препинания!
    question = question[0:-1]
    question = question.split()

    # Если длина == 1, а слово = Все, печатаем все фреймы.
    if len(question) == 1 and question[0] == 'Все':
        for frame in frames:
            fr = frame.frameToString()
            print(fr)
        continue

    # Вывод фрейма по названию
    if len(question) == 1:
        print(getFrame(frames, question[0]).frameToString())
        continue

    # Если мы хотим изменить какие-то данные у конкретного талона. Работает только для времени и даты
    if len(question) == 7 and question[1] == 'изменить':
        res = removeTalon(frames, question[4], question[6], question[2])
        print(res)
        continue

    # На случай всего остального
    answer = getFrame(frames, question[2])
    if answer is None:
        answer = getAnswerBySlot(frames, question[1], question[3])
    print(answer.frameToString())