class Point:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def sqSum(self):
		a = self.x ** 2
		b = self.y ** 2
		c = self.z ** 2
		return (a + b + c)

def main():
	val = input("Enter three numbers with a space in between: ")
	lst = val.split()
	a = int(lst[0])
	b = int(lst[1])
	c = int(lst[2])
	d = Point(a,b,c)
	print(f'Sum of the numbers is {d.sqSum()}')

if __name__ == "__main__":
	main()