import pyglet
from enumerations import *

def init_graphics(self):
	pyglet.resource.path = ['../resources']
	pyglet.resource.reindex()
	
	order = pyglet.graphics.OrderedGroup(0)
	self.init_background(order)
	order = pyglet.graphics.OrderedGroup(1)
	self.init_static_objects(order)
	order = pyglet.graphics.OrderedGroup(2)
	self.init_interactable_objects(order)
	
	order0 = pyglet.graphics.OrderedGroup(0)
	order1 = pyglet.graphics.OrderedGroup(1)
	order2 = pyglet.graphics.OrderedGroup(2)
	self.init_conditional(order0,order1,order2)
	
	order = pyglet.graphics.OrderedGroup(3)
	self.init_mobile_objects(order)
	
	order = pyglet.graphics.OrderedGroup(4)
	CS_image = pyglet.resource.image('commander_ship_16x16.png')
	self.center_image(CS_image)
	self.CS_sprite = pyglet.sprite.Sprite(img=CS_image, x=280+360, y=360, batch=self.batch_mobile, group=order)
	self.engine.commandership.set_sprite(self.CS_sprite)
	
	order = pyglet.graphics.OrderedGroup(0)
	viewol_image = pyglet.resource.image('view_overlay_v2_1280x720.png')
	self.view_overlay_sprite = pyglet.sprite.Sprite(img=viewol_image, x=0, y=0,batch = self.batch_UI, group=order)
	
	order = pyglet.graphics.OrderedGroup(1)
	self.init_map(order)
	
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
	
	moon_image = pyglet.resource.image('moon_180x180.png')
	self.center_image(moon_image)
	moon_sprite = pyglet.sprite.Sprite(img=moon_image, batch = self.batch_static)
	self.moon_sprite = pyglet.sprite.Sprite(img=moon_image, batch = self.batch_map, group=order)
	self.engine.moon.set_sprite(self.moon_sprite)
	
def init_interactable_objects(self, order):
	base_image = pyglet.resource.image('base_lvl0_30x30.png')
	self.center_image(base_image)
	base_sprite = pyglet.sprite.Sprite(img=base_image, batch = self.batch_map, group=order)
	self.engine.homeplanet.base.set_level_sprite(base_sprite)
	
	base_image = pyglet.resource.image('base_lvl1_30x30.png')
	self.center_image(base_image)
	base_sprite = pyglet.sprite.Sprite(img=base_image, batch = self.batch_map, group=order)
	base_sprite.visible=False
	self.engine.homeplanet.base.set_level_sprite(base_sprite)
	
	base_image = pyglet.resource.image('base_lvl2_30x30.png')
	self.center_image(base_image)
	base_sprite = pyglet.sprite.Sprite(img=base_image, batch = self.batch_map, group=order)
	base_sprite.visible=False
	self.engine.homeplanet.base.set_level_sprite(base_sprite)
	
	base_image = pyglet.resource.image('base_lvl3_30x30.png')
	self.center_image(base_image)
	base_sprite = pyglet.sprite.Sprite(img=base_image, batch = self.batch_map, group=order)
	base_sprite.visible=False
	self.engine.homeplanet.base.set_level_sprite(base_sprite)
	
	base_image = pyglet.resource.image('base_lvl4_30x30.png')
	self.center_image(base_image)
	base_sprite = pyglet.sprite.Sprite(img=base_image, batch = self.batch_map, group=order)
	base_sprite.visible=False
	self.engine.homeplanet.base.set_level_sprite(base_sprite)
	
	base_image = pyglet.resource.image('base_lvl5_30x30.png')
	self.center_image(base_image)
	base_sprite = pyglet.sprite.Sprite(img=base_image, batch = self.batch_map, group=order)
	base_sprite.visible=False
	self.engine.homeplanet.base.set_level_sprite(base_sprite)
	
	base_image = pyglet.resource.image('base_lvl6_30x30.png')
	self.center_image(base_image)
	base_sprite = pyglet.sprite.Sprite(img=base_image, batch = self.batch_map, group=order)
	base_sprite.visible=False
	self.engine.homeplanet.base.set_level_sprite(base_sprite)
	
	basemine_image = pyglet.resource.image('basemine_30x30.png')
	self.center_image(basemine_image)
	basemine_sprite = pyglet.sprite.Sprite(img=basemine_image, batch = self.batch_map, group=order)
	basemine_sprite.visible=False
	self.engine.homeplanet.basemine.set_level_sprite(basemine_sprite)
	
	factory_image = pyglet.resource.image('builder_factory_30x30.png')
	self.center_image(factory_image)
	factory_sprite = pyglet.sprite.Sprite(img=factory_image, batch = self.batch_map, group=order)
	factory_sprite.visible=False
	self.engine.homeplanet.factory.set_level_sprite(factory_sprite)
	
def init_conditional(self, order0, order1, order2):
	exhaust_1_image = pyglet.resource.image('exhaust_fumes_1_4x6.png')
	exhaust_2_image = pyglet.resource.image('exhaust_fumes_2_4x6.png')
	self.center_image(exhaust_1_image)
	pos = self.engine.get_cs().get_pos()
	x = pos[0]
	y = pos[1] - 8 - 3
	angle = self.engine.commandership.get_angle()
	x,y,angle = self.camera.get_posang_in_view(x, y, angle)
	self.exhaust_sprite = pyglet.sprite.Sprite(img=exhaust_1_image, x=x, y=y, batch=self.batch_mobile, group=order0)
	
	action_image = pyglet.resource.image('action_possible_60x60.png')
	self.center_image(action_image)
	self.act_pos_sprite = pyglet.sprite.Sprite(img=action_image, batch=self.batch_mobile, group=order0)
	
	load_image = pyglet.resource.image('load_bar_54x10.png')
	self.center_image(load_image)
	self.load_sprite = pyglet.sprite.Sprite(img=load_image, batch=self.batch_mobile, group=order1)
	
	self.load_tick_sprites = []
	load_tick_image = pyglet.resource.image('load_tick_5x6.png')
	self.center_image(load_image)
	for i in range(10):
		self.load_tick_sprites.append(pyglet.sprite.Sprite(img=load_tick_image, batch=self.batch_mobile, group=order2))
	
def init_mobile_objects(self, order):
	pass

def init_UI_overlay(self, order):
	self.time_label = pyglet.text.Label(text="day/month/year", x=10, y=720-20,batch = self.batch_UI, group=order)
	self.position_label = pyglet.text.Label(text="x_pos: 0, y_pos:0, ang=0", x=10, y=720-40,batch = self.batch_UI, group=order)
	self.velocity_label = pyglet.text.Label(text="total_vel: 0, x_vel: 0, y_vel:0, ang_vel=0", x=10, y=720-60,batch = self.batch_UI, group=order)
	self.resource_label = pyglet.text.Label(text="Almanite:", x=10, y=720-100,batch = self.batch_UI, group=order)
	self.interaction_label = pyglet.text.Label(text="Interactable:", x=10, y=720-120,batch = self.batch_UI, group=order)
	
	orientation_image = pyglet.resource.image('orientation_80x80.png')
	self.center_image(orientation_image)
	self.orientation_sprite = pyglet.sprite.Sprite(img=orientation_image, x=400, y=40, batch = self.batch_UI, group=order)
	
def init_map(self, order):
	center = self.map.get_center()
	size = self.map.get_size()
	self.map_circle = pyglet.shapes.Arc(center[0], center[1], size/2, color=(50, 0, 255), batch=self.batch_UI, group=order)
	self.map_cs = pyglet.shapes.Arc(center[0], center[1], 2, color=(50, 0, 255), batch=self.batch_UI, group=order)
	self.map_vector = pyglet.shapes.Line(center[0], center[1], center[0], center[1], color=(50, 0, 255), batch=self.batch_UI, group=order)
	self.map_vector_half = pyglet.shapes.Arc(center[0], center[1], 2, color=(100, 100, 255), batch=self.batch_UI, group=order)
	self.map_static = []
	for object in self.engine.get_static_objects():
		color = (0,100,255)
		size = 3
		if EngineList.Static == object.get_description():
			color = (0, 255, 0)
			size = 4
		circle = pyglet.shapes.Arc(100, 100, size, color=color, batch=self.batch_UI, group=order)
		self.map_static.append([object, circle])

