import math
import pyglet
from keybindings import KeyBindings
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
		
		self.init_graphics()
		KeyBindings(self, self.engine.commandership)
		
		self.update = self.update
		pyglet.clock.schedule_interval(self.update, self.dt)
		
	def update(self, dt):
		self.engine.commandership.update_angle_position()
		self.update_view()
		self.update_space_objects()
		self.update_text()
		self.update_orientation()
		
	def on_draw(self):
		self.clear()
		
		self.batch_BG.draw()
		self.batch_static.draw()
		self.engine.commandership.get_sprite().draw()
		if self.engine.commandership.acc > 0:
			self.exhaust_sprite.draw()
			
		self.view_overlay_sprite.draw()
		self.batch_UI.draw()
		
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
		self.position_label.text = "x_pos: {:.2f}, y_pos:{:.2f}, ang={}".format(x_pos,y_pos,ang)
		self.velocity_label.text = "x_vel: {:.2f}, y_vel:{:.2f}, ang_vel={}".format(x_vel,y_vel,ang_vel)
		
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
		
		self.init_background()
		self.init_UI_overlay()
		self.init_static_objects()
		
		CS_image = pyglet.resource.image('commander_ship_16x16.png')
		self.center_image(CS_image)
		self.CS_sprite = pyglet.sprite.Sprite(img=CS_image, x=280+360, y=360)
		self.engine.commandership.set_sprite(self.CS_sprite)
		
		viewol_image = pyglet.resource.image('view_overlay_v2_1280x720.png')
		self.view_overlay_sprite = pyglet.sprite.Sprite(img=viewol_image, x=0, y=0)
		
		exhaust_1_image = pyglet.resource.image('exhaust_fumes_1_4x6.png')
		exhaust_2_image = pyglet.resource.image('exhaust_fumes_2_4x6.png')
		self.center_image(exhaust_1_image)
		x = self.CS_sprite.x
		y = self.CS_sprite.y - 8 - 3
		self.exhaust_sprite = pyglet.sprite.Sprite(img=exhaust_1_image, x=x, y=y)
		
		
	def init_static_objects(self):
		self.batch_static = pyglet.graphics.Batch()
		homeplanet_image = pyglet.resource.image('homeplanet_360x360.png')
		self.center_image(homeplanet_image)
		homeplanet_sprite = pyglet.sprite.Sprite(img=homeplanet_image, batch = self.batch_static)
		self.engine.homeplanet.set_sprite(homeplanet_sprite)
	
	def init_UI_overlay(self):
		self.batch_UI = pyglet.graphics.Batch()
		self.position_label = pyglet.text.Label(text="x_pos: 0, y_pos:0, ang=0", x=10, y=720-20, batch = self.batch_UI)
		self.velocity_label = pyglet.text.Label(text="x_vel: 0, y_vel:0, ang_vel=0", x=10, y=720-40, batch = self.batch_UI)
		
		orientation_image = pyglet.resource.image('orientation_80x80.png')
		self.center_image(orientation_image)
		self.orientation_sprite = pyglet.sprite.Sprite(img=orientation_image, x=40, y=40, batch = self.batch_UI)
	
	def init_background(self):
		#Space background
		self.BG_image = pyglet.resource.image('space_background_80x80.png')
		self.center_image(self.BG_image)
		self.batch_BG = pyglet.graphics.Batch()
		self.BG_sprites = []
		mid = 5
		for i in range(0, 10):
			for j in range(0, 10):
				sprite = pyglet.sprite.Sprite(img=self.BG_image, batch=self.batch_BG)
				self.BG_sprites.append([i,j,sprite])