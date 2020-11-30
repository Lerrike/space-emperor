import pyglet
from gameengine import GameEngine
from graphicswindow import GraphicsWindow

def main():
	dt = 1.0/60.0 #update interval
	engine = GameEngine(dt)
	window = GraphicsWindow(dt, engine)
	pyglet.app.run()
	
	return 0
	

if __name__ == '__main__':
	main()