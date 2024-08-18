# Способы вызова функции


def send_email(message, recipient, sender='university.help@gmail.com'):
    flag_dog = []
    for i in range(0, len(recipient), 1):
        if recipient[i] == '@':
            flag_dog.append(True)
        else:
            flag_dog.append(False)
    for i in range(0, len(sender), 1):
        if sender[i] == '@':
            flag_dog.append(True)
        else:
            flag_dog.append(False)
    # print(bool(sum(flag_dog)))
    flag_end = []
    if (recipient[len(recipient) - 4:len(recipient)]) == '.com' or (recipient[len(recipient) - 4:len(recipient)]) == '.net' or (recipient[len(recipient) - 3:len(recipient)]) == '.ru' and (sender[len(sender) - 4:len(sender)]) == '.com' or (sender[len(sender) - 4:len(sender)]) == '.net' or (sender[len(sender) - 3:len(sender)]) == '.ru':
        flag_end.append(True)
    # print(bool(flag_end))
    if bool(sum(flag_dog)) == False or bool(flag_end) == False:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    else:
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        else:
            if sender == 'university.help@gmail.com':
                print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
            else:
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
# проверка:


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')