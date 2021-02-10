import math
import pyglet
#from keybindings import KeyBindings
from camera import Camera

class GraphicsWindow(pyglet.window.Window):
	def __init__(self, engine):
		self.screen_width = 1280
		self.screen_height = 720
		self.dt = 1.0/60.0 #update interval
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
		#clk = clock.get_default()
		
		self.down_mem = 0
		
		
	def update_world(self, dt):
		self.engine.commandership.update_angle_position()
		self.update_view()
		self.update_space_objects()
		self.update_text()
		self.update_orientation()
		
		self.engine.calc_range_do_action()
		
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
			commandership.acc_action()
			self.exhaust_sprite.visible = True
		elif down_pressed:
			speed = math.fabs(commandership.get_x_vel()) + math.fabs(commandership.get_y_vel())
			if speed == 0 and self.down_mem == 0:
				self.engine.action()
			else:
				commandership.decelerate()
				self.down_mem = 1
			self.exhaust_sprite.visible = False
		else:
			commandership.no_acc_action()
			self.exhaust_sprite.visible = False
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
		else:
			self.act_pos_sprite.visible = False
		
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
		self.position_label.text = "x_pos: {:.2f}, y_pos:{:.2f}, ang={}".format(x_pos,y_pos,ang)
		self.velocity_label.text = "x_vel: {:.2f}, y_vel:{:.2f}, acc:{:.2f}, ang_vel={}".format(x_vel,y_vel,acc, ang_vel)
		
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
		
	def init_graphics(self):
		pyglet.resource.path = ['../resources']
		pyglet.resource.reindex()
		
		order = pyglet.graphics.OrderedGroup(0)
		self.init_background(order)
		order = pyglet.graphics.OrderedGroup(1)
		self.init_static_objects(order)
		order = pyglet.graphics.OrderedGroup(2)
		self.init_interactable_objects(order)
		
		order = pyglet.graphics.OrderedGroup(0)
		self.init_conditional(order)
		
		order = pyglet.graphics.OrderedGroup(1)
		self.init_mobile_objects(order)
		
		order = pyglet.graphics.OrderedGroup(2)
		CS_image = pyglet.resource.image('commander_ship_16x16.png')
		self.center_image(CS_image)
		self.CS_sprite = pyglet.sprite.Sprite(img=CS_image, x=280+360, y=360, batch=self.batch_mobile, group=order)
		self.engine.commandership.set_sprite(self.CS_sprite)
		
		order = pyglet.graphics.OrderedGroup(0)
		viewol_image = pyglet.resource.image('view_overlay_1280x720.png')
		self.view_overlay_sprite = pyglet.sprite.Sprite(img=viewol_image, x=0, y=0,batch = self.batch_UI, group=order)
		
		order = pyglet.graphics.OrderedGroup(1)
		self.init_UI_overlay(order)
		
	def init_background(self, order):
		#Space background
		self.BG_image = pyglet.resource.image('space_background_80x80.png')
		self.center_image(self.BG_image)
		self.batch_BG = pyglet.graphics.Batch()
		self.BG_sprites = []
		mid = 5
		for i in range(0, 10):
			for j in range(0, 10):
				#sprite = pyglet.sprite.Sprite(img=self.BG_image, batch=self.batch_BG, group=order)
				sprite = pyglet.sprite.Sprite(img=self.BG_image, batch=self.batch_map, group=order)
				self.BG_sprites.append([i,j,sprite])
		
	def init_static_objects(self, order):
		self.batch_static = pyglet.graphics.Batch()
		homeplanet_image = pyglet.resource.image('homeplanet_360x360.png')
		self.center_image(homeplanet_image)
		homeplanet_sprite = pyglet.sprite.Sprite(img=homeplanet_image, batch = self.batch_static)
		self.homeplanet_sprite = pyglet.sprite.Sprite(img=homeplanet_image, batch = self.batch_map, group=order)
		self.engine.homeplanet.set_sprite(self.homeplanet_sprite)
		
	def init_interactable_objects(self, order):
		base0_image = pyglet.resource.image('base_lvl0_60x60.png')
		self.center_image(base0_image)
		base0_sprite = pyglet.sprite.Sprite(img=base0_image, batch = self.batch_map, group=order)
		self.engine.homeplanet.base.set_level_sprite(base0_sprite)
		
		base1_image = pyglet.resource.image('base_lvl1_60x60.png')
		self.center_image(base1_image)
		base1_sprite = pyglet.sprite.Sprite(img=base1_image, batch = self.batch_map, group=order)
		self.engine.homeplanet.base.set_level_sprite(base1_sprite)
		
	def init_conditional(self, order):
		exhaust_1_image = pyglet.resource.image('exhaust_fumes_1_4x6.png')
		exhaust_2_image = pyglet.resource.image('exhaust_fumes_2_4x6.png')
		self.center_image(exhaust_1_image)
		x = self.engine.commandership.get_x()
		y = self.engine.commandership.get_y() - 8 - 3
		angle = self.engine.commandership.get_angle()
		x,y,angle = self.camera.get_posang_in_view(x, y, angle)
		self.exhaust_sprite = pyglet.sprite.Sprite(img=exhaust_1_image, x=x, y=y, batch=self.batch_mobile, group=order)
		
		action_image = pyglet.resource.image('action_possible_60x60.png')
		self.center_image(action_image)
		x = 0
		y = 0
		angle = 0
		x,y,angle = self.camera.get_posang_in_view(x, y, angle)
		self.act_pos_sprite = pyglet.sprite.Sprite(img=action_image, x=x, y=y, batch=self.batch_mobile, group=order)
		
	def init_mobile_objects(self, order):
		pass
	
	def init_UI_overlay(self, order):
		self.position_label = pyglet.text.Label(text="x_pos: 0, y_pos:0, ang=0", x=10, y=720-20,batch = self.batch_UI, group=order)
		self.velocity_label = pyglet.text.Label(text="x_vel: 0, y_vel:0, ang_vel=0", x=10, y=720-40,batch = self.batch_UI, group=order)
		
		orientation_image = pyglet.resource.image('orientation_80x80.png')
		self.center_image(orientation_image)
		self.orientation_sprite = pyglet.sprite.Sprite(img=orientation_image, x=40, y=40, batch = self.batch_UI, group=order)
	