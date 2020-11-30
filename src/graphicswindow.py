import math
import pyglet
from keybindings import KeyBindings
from camera import Camera

class GraphicsWindow(pyglet.window.Window):
	def __init__(self, dt, engine):
		self.screen_width = 1280
		self.screen_height = 720
		self.dt = dt
		super(GraphicsWindow, self).__init__(self.screen_width, self.screen_height) #Set screensize
		self.set_caption('Space Emperor')
		
		self.engine = engine
		
		self.init_graphics()
		KeyBindings(self, self.engine.commandership)
		
		self.update = self.update
		pyglet.clock.schedule_interval(self.update, self.dt)
		
		self.camera = Camera(self.screen_width, self.screen_height)
		
	def update(self, dt):
		self.engine.commandership.update_angle_position()
		self.update_background()
		self.update_text()
		self.update_orientation()
		
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
	
	
	def update_background(self):
		CS = self.engine.commandership
		x_cs = CS.get_x()
		y_cs = CS.get_y()
		ang_cs = CS.get_angle()
		mid = 4
		self.camera.update_camera_posang(x_cs, y_cs, ang_cs)
		pos_cam = self.camera.get_position()
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
			
	
	def on_draw(self):
		self.clear()
		
		self.batch_BG.draw()
		self.viewol_sprite.draw()
		self.position_label.draw()
		self.velocity_label.draw()
		self.orientation_sprite.draw()
		#self.cross_sprite.draw()
		self.CS_sprite.draw()
		
	def center_image(self, image):
		image.anchor_x = image.width // 2
		image.anchor_y = image.height // 2
		
	def init_graphics(self):
		pyglet.resource.path = ['../resources']
		pyglet.resource.reindex()
		
		self.position_label = pyglet.text.Label(text="x_pos: 0, y_pos:0, ang=0", x=10, y=720-20)
		self.velocity_label = pyglet.text.Label(text="x_vel: 0, y_vel:0, ang_vel=0", x=10, y=720-40)
		
		self.init_background()
		self.CS_image = pyglet.resource.image('commander_ship_16x16.png')
		self.center_image(self.CS_image)
		self.CS_sprite = pyglet.sprite.Sprite(img=self.CS_image, x=280+360, y=360)
		
		self.orientation_image = pyglet.resource.image('orientation_80x80.png')
		self.center_image(self.orientation_image)
		self.orientation_sprite = pyglet.sprite.Sprite(img=self.orientation_image, x=40, y=40)
		
		#self.cross_image = pyglet.resource.image('cross_10x10.png')
		#self.center_image(self.cross_image)
		#self.cross_sprite = pyglet.sprite.Sprite(img=self.cross_image, x=280+360, y=360)
		
		self.viewol_image = pyglet.resource.image('view_overlay_v2_1280x720.png')
		#self.center_image(self.cross_image)
		self.viewol_sprite = pyglet.sprite.Sprite(img=self.viewol_image, x=0, y=0)
	
	def init_background(self):
		#Space background
		self.BG_image = pyglet.resource.image('space_background_80x80.png')
		self.center_image(self.BG_image)
		self.batch_BG = pyglet.graphics.Batch()
		self.BG_sprites = []
		mid = 5
		for i in range(0, 10):
			for j in range(0, 10):
				#x_i = 280 - 40 + i * 80
				#y_i = -40 + j * 80
				#x_i = 280 + 360 + (i-mid) * 80
				#y_i = 360 + (j-mid) * 80
				#sprite = pyglet.sprite.Sprite(img=self.BG_image, x=x_i, y=y_i, batch=self.batch_BG)
				sprite = pyglet.sprite.Sprite(img=self.BG_image, batch=self.batch_BG)
				self.BG_sprites.append([i,j,sprite])