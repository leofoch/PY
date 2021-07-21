class Calculadora:
	total=0

	def valor(self):
		return self.total

	def suma(self,sums):
		for nro in sums:
			self.total += nro

	def producto(self,prod):
		self.total = 1
		for nro in prod:
			self.total*=nro

	def division(self, dividendo, divisor):
		self.total = dividendo/divisor

	def resta(self,uno,dos):
		self.total = uno-dos