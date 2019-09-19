



class Animation():
	

	def __init__(self):
		self.vertex_n = 0
		self.verticies = []

       
	def get_coord(self, V_kind):
		print("\n\t***\nFor vertex %s please enter:\n" % V_kind)
		x = input('X: ')
		y = input('Y: ')
		z = input('Z: ')
		pos = [x, y, z]
		return pos


	def add_Vertex(self):
		self.vertex_n +=1
		self.verticies.append(Vertex())
		self.verticies[self.vertex_n-1].p_zero = self.get_coord("position zero")
		self.verticies[self.vertex_n-1].name = "Vertex_"+ str(self.vertex_n)
		return


class Vertex(object):

	def __init__(self, p_zero = None, position = None, rest = None, name = None):
		self.p_zero = p_zero #initial vertex position and this vertex's zero
		self.position = position #current vertex position
		self.rest = rest #set rest position for the vertex
		self.servos = [] #list of servo objects
		self.servo_n = 0 #servo count on vertex
		self.name = name #Vertex name

	def add_servo(self):
		self.servos.append(Servo(self.name))
		return print("Not Done")


class Servo(object):

	def __init__(self, vertex, vector = None, rate = None, track = None):
		self.vertex = Vertex  #What vertex is this servo linked to
		self.vector = vector #Input for movement
		self.rate = rate #Acceleration
		self.track = track #axis and range of movement



mouth = Animation()


mouth.add_Vertex()


for i, obj in enumerate(mouth.verticies):
	print ("Zero position for", obj.name, "is", obj.p_zero)