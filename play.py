#мини игра от дару
print("Приветствуй новобранец!\nНачать игру? Да/Нет")
ng=str(input())
if ng=='Да' or ng=='да':
	print("О нет! На вашу деревню напали!")
	sv=str(input("Спасти жителей(Да/нет): "))
	if sv=='Да' or sv=='да':
		print("Отлично!")
		print("Подсказка на вас скоро нападут ")
		print("Вы и ваши друзья идут купаться")
		input("Вы видете как друг тонет помочь ему(Да/Нет)?\n")
		print("Все обошлось ваш друг всплыл сам")
		input("НА ВАС НАПАДАЮТ ЧТО ДЕЛАТЬ Бежать/Остаться\n")
		print("Ваши друзя побежали ваш друг взял вас за руку и побежал")
		print("Ваш друг кинул вас и вас убили")
	else:
		print("Вы погибли...")
else:
	print('Пока :(')
input()

