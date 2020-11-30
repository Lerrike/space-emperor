from pyglet.window import key

def KeyBindings(window, commander_ship):
	@window.event
	def on_key_press(symbol, modifiers):
		if symbol == key.UP:
			commander_ship.acc_action()
		elif symbol == key.DOWN:
			commander_ship.decelerate()
		elif symbol == key.LEFT:
			commander_ship.turn_left()
		elif symbol == key.RIGHT:
			commander_ship.turn_right()
	
	@window.event
	def on_key_release(symbol, modifiers):
		if symbol == key.UP:
			commander_ship.no_acc_action()
		elif symbol == key.DOWN:
			commander_ship.no_acc_action()
		elif symbol == key.LEFT:
			commander_ship.stop_rotation()
		elif symbol == key.RIGHT:
			commander_ship.stop_rotation()