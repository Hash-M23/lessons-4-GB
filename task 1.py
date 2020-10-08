def sal():
	try:
		hour_price = float(input("В час заработал"))
		hours_quantity = int(input("Выроботка"))
		bonus = int(input("Премия"))
		res = hour_price * hours_quantity + bonus
		print(f"зароботная плата сотрудника {res}")
	except ValueError:
		return print("write number")
sal()