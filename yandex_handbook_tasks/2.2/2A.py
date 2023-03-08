print('Как Вас зовут?')
name = input()
print(f'Здравствуйте, {name}!\nКак дела?')
do = input()
if do == 'хорошо':
    txt = 'Я за вас рада!'
else:
    txt = 'Всё наладится!'
print(txt)