# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами
user_name = str( input('Введите Имя:'))   #'Alex'
user_age = str(input('Введите Возраст:')) #'30'
user_town = str(input('Введите Город:'))  #'Minsk'
# print( user_name + user_age + user_town)

    # 1-ый способ
print('Приветствую, ' + user_name.strip() + '! Ты из города ' + user_town.strip() + '! Тебе ' + user_age.strip() +' лет.')
    # 2-jй способ
print("Приветствую {name}. Тебе {age} лет. Твой город {city} чистый!".format(age=user_age, name=user_name, city=user_town))
    # 3-ий способ
x = f'Приветствую!!! Имя:{user_name}  Возраст:{user_age}  Город:{user_town}'
print(x)