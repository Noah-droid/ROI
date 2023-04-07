# subscription/menu.py
from ussd.menu import Menu

menu = Menu()
menu.add_choice('start', '1', 'Subscribe')
menu.add_choice('start', '2', 'Unsubscribe')
