import pyglet

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