import botlogic

def sağa(x = 1):
	global dialog
	adım = 1
	car = botlogic.dialog.ui.carButton
	while adım <= x:
		car.move(car.x() + 40, car.y())
