import math
import pyglet
from camera import Camera

class GraphicsWindow(pyglet.window.Window):
	from _init_graphics import init_graphics, init_background, init_static_objects, init_interactable_objects,\
		init_conditional, init_mobile_objects, init_UI_overlay
	from _update_graphics import update_orientation, update_text, update_view, update_background, update_space_objects
	
	def __init__(self, engine,dt):
		self.screen_width = 1280
		self.screen_height = 720
		self.dt = dt
		super(GraphicsWindow, self).__init__(self.screen_width, self.screen_height) #Set screensize
		self.set_caption('Space Emperor')
		
		self.engine = engine
		self.camera = Camera(self.screen_width, self.screen_height)
		
		self.batch_map = pyglet.graphics.Batch()
		self.batch_mobile = pyglet.graphics.Batch()
		self.batch_UI = pyglet.graphics.Batch()
		self.init_graphics()
		
		self.key_handler = pyglet.window.key.KeyStateHandler()
		self.push_handlers(self.key_handler)
		#KeyBindings(self, self.engine.commandership)
		
		update_fun = self.update_world
		pyglet.clock.schedule_interval(update_fun, self.dt)
		
		update_fun = self.update_world_time
		pyglet.clock.schedule_interval(update_fun, 1.0)
		
		
		self.down_mem = 0
		
	def update_world_time(self,dt):
		self.engine.tick_time()
		self.engine.do_tick_action()
		
	def update_world(self, dt):
		self.engine.commandership.update_angle_position()
		self.update_view()
		self.update_space_objects()
		self.update_text()
		self.update_orientation()
		
		self.engine.update_world()
		
		self.keybindings()
		
	def on_draw(self):
		self.clear()
		self.batch_map.draw()
		self.draw_coditional()
		self.batch_mobile.draw()
		self.view_overlay_sprite.draw()
		self.batch_UI.draw()
		
	def keybindings(self):
		commandership = self.engine.commandership
		up_pressed = self.key_handler[pyglet.window.key.UP]
		down_pressed = self.key_handler[pyglet.window.key.DOWN]
		left_pressed = self.key_handler[pyglet.window.key.LEFT]
		right_pressed = self.key_handler[pyglet.window.key.RIGHT]
		
		if up_pressed:
			if commandership.get_resources() > 0:
				commandership.acc_action()
				self.exhaust_sprite.visible = True
		elif down_pressed:
			speed = math.fabs(commandership.get_x_vel()) + math.fabs(commandership.get_y_vel())
			if speed == 0 and self.down_mem == 0:
				self.engine.action()
			else:
				if commandership.get_resources() > 0 and speed > 0:
					commandership.decelerate()
				self.down_mem = 1
			self.exhaust_sprite.visible = False
		else:
			commandership.no_acc_action()
			self.exhaust_sprite.visible = False
			self.engine.action_reset()
			self.down_mem = 0
		
		if (left_pressed and right_pressed):
			commandership.stop_rotation()
		elif left_pressed:
			commandership.turn_left()
		elif right_pressed:
			commandership.turn_right()
		else:
			commandership.stop_rotation()
		
	def draw_coditional(self):
		object = self.engine.commandership.get_object_in_closerange()
		if object:
			[x, y] = object.get_pos()
			x, y, angle = self.camera.get_posang_in_view(x, y, 0)
			self.act_pos_sprite.x = x
			self.act_pos_sprite.y = y
			self.act_pos_sprite.visible = True
			
			[x,y] = object.get_pos()
			x, y, angle = self.camera.get_posang_in_view(x,y,0)
			self.load_sprite.x = x
			self.load_sprite.y = y + 40
			self.load_sprite.visible = True
			for i in range(10):
				if object.load > i * 10:
					self.load_tick_sprites[i].x = x - 25 + i*5
					self.load_tick_sprites[i].y = y + 40 - 3
					self.load_tick_sprites[i].visible = True
				else:
					self.load_tick_sprites[i].visible = False
		else:
			self.act_pos_sprite.visible = False
			self.load_sprite.visible = False
			for sprite in self.load_tick_sprites:
				sprite.visible = False
	
	def center_image(self, image):
		image.anchor_x = image.width // 2
		image.anchor_y = image.height // 2
		
	