from pyglet.window import key

def KeyBindings(window, commander_ship):
	@window.event
	def on_key_press(symbol, modifiers):
		if symbol == key.UP:
			commander_ship.accelerate()
		elif symbol == key.DOWN:
			commander_ship.decelerate()
		elif symbol == key.LEFT:
			commander_ship.turn_left()
		elif symbol == key.RIGHT:
			commander_ship.turn_right()
	
	@window.event
	def on_key_release(symbol, modifiers):
		if symbol == key.UP:
			commander_ship.decelerate()
		elif symbol == key.DOWN:
			pass
		elif symbol == key.LEFT:
			commander_ship.stop_rotation()
		elif symbol == key.RIGHT:
			commander_ship.stop_rotation()