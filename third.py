def yesmail(a):
    return a
def nomail(b):
    return b
a = 'Получили email, сохраняем все данные'
b = '''Это не похоже на email. Попробуй еще раз.
                "Пример: vasha_pochta@mail.ru'''
email = message.text.strip()
if '@' not in email or "." not in email:
    print(yesmail(a))
else:
    print(nomail(b))