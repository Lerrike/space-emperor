import math
import pyglet
from camera import Camera

class GraphicsWindow(pyglet.window.Window):
	from _init_graphics import init_graphics, init_background, init_static_objects, init_interactable_objects,\
		init_conditional, init_mobile_objects, init_UI_overlay
	
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
		
	def update_orientation(self):
		#Negative, because rotation in opposite direction
		self.orientation_sprite.rotation = -self.engine.commandership.get_angle()
		
	def update_text(self):
		CS = self.engine.commandership
		x_pos = CS.get_x()
		y_pos = CS.get_y()
		ang = CS.get_angle()
		x_vel = CS.get_x_vel()
		y_vel = CS.get_y_vel()
		ang_vel = CS.get_ang_vel()
		acc = CS.get_acc()
		date = self.engine.get_date()
		resource_amount = CS.get_resources()
		max_resources = CS.get_max_resources()
		object = CS.get_object_in_closerange()
		amount = 0
		name = 0
		interaction = 0
		if object:
			amount = object.get_interaction_cost()
			resource = object.get_resources()
			if resource:
				amount = resource
			name = object.get_name()
			interaction = object.get_interaction_name()
		self.time_label.text = "day/month/year:{}/{}/{}".format(date[0],date[1],date[2])
		self.position_label.text = "x_pos: {:.2f}, y_pos:{:.2f}, ang={}".format(x_pos,y_pos,ang)
		self.velocity_label.text = "x_vel: {:.2f}, y_vel:{:.2f}, acc:{:.2f}, ang_vel={}".format(x_vel,y_vel,acc, ang_vel)
		self.resource_label.text = "Almanite:{:.2f}/{}".format(resource_amount,max_resources)
		self.interaction_label.text = "Interactable:{}, {}:{:.2f}".format(name, interaction, amount)
		
		
	def update_view(self):
		CS = self.engine.commandership
		x_cs = CS.get_x()
		y_cs = CS.get_y()
		ang_cs = CS.get_angle()
		self.camera.update_camera_posang(x_cs, y_cs, ang_cs)
		
		self.update_background(x_cs, y_cs, ang_cs)
	
	
	def update_background(self, x_cs, y_cs, ang_cs):
		pos_cam = self.camera.get_position()
		mid = 4
		for x_y_sprite in self.BG_sprites:
			i = x_y_sprite[0]
			j = x_y_sprite[1]
			sprite = x_y_sprite[2]
			
			x_bos = (i-mid)*80 + (pos_cam[0]//80)*80
			y_bos = (j-mid)*80 + (pos_cam[1]//80)*80
			x,y,angle = self.camera.get_posang_in_view(x_bos,y_bos,0)
			sprite.x = x
			sprite.y = y
			sprite.rotation = angle
			
	def update_space_objects(self):
		for object in self.engine.get_objects():
			sprite = object.get_sprite()
			if self.camera.is_on_view(object):
				x = object.get_x()
				y = object.get_y()
				angle = object.get_angle()
				x, y, angle = self.camera.get_posang_in_view(x, y, angle)
				sprite.x = x
				sprite.y = y
				sprite.rotation = angle
	
	def center_image(self, image):
		image.anchor_x = image.width // 2
		image.anchor_y = image.height // 2
		
	