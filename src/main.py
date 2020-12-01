import pyglet
from gameengine import GameEngine
from graphicswindow import GraphicsWindow

def main():
	engine = GameEngine()
	window = GraphicsWindow(engine)
	pyglet.app.run()
	
	return 0
	

if __name__ == '__main__':
	main()