def send_email (message, recipient, *, sender = 'university.help@gmail.com'): # ОХ и выпило у меня это задание кровушки... пояснениями пометил где!
    ending = ('.com', '.ru', '.net') # переменная содержащая кортеж из окончаний (надо было догадаться!!!)
    if ('@' not in recipient or '@' not in sender
        or not sender.endswith(ending) or not recipient.endswith (ending)): # между содержимым кортежа при сравнении стоит OR !!!
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Неьзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teachermail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')