# def print_params(*, a, b, c):
#     print(a, b, c)
#
#
# print_params(a=1, b=2, c=6)

# def func_with_params(a, b=2, c=None):
#     if c is None:
#         c = []
#         c.append(a)
#     print(c)
#
#
# func_with_params(3, 5)
# func_with_params(4,5)
# func_with_params(5,5)
# func_with_params(6,5)


def send_email(message, recipient,*, sender="university.help@gmail.com"):
    def check_email(email):
        valid_domains = [".com", ".ru", ".net"]
        return "@" in email and any(email.endswith(domain) for domain in valid_domains)
    if not check_email(sender) or not check_email(recipient):
        print(f"Невозможно отправить письмо с адреса, {sender} на адрес, {recipient}")
        return
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        return
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
