#!/usr/bin/python3

BuTotal = 50 #o que é isso?!

ClasseA = 20
ClasseB = 10
ClasseC = 5
ClasseD = 2


Bu = 'Bandwidth in use by CoS in selected network path - Total'
Brq = 'Bandwidth required by CoS - Request'
MRth = 'Maximum reservation threshold of CoS'

Bov = 'Over-reservation bandwidth of CoS i'
Brv = (Bov + Brq)

# ----------------- / ---------------------------- #
#	ClasseA = 20
#	ClasseB = 20
#	ClasseC = 20
#	ClasseD = 20


ClasseA = 20 #por que isso tá declarado duas vezes?!
MRthi = ClasseA
Bui = 0.1
Brqi = 0
BrvA = 0

class QvP:

	def __init__(self, MRthi, Bui, Brqi, Brvi):
		self.mrthi = MRthi
		self.bui = Bui
		self.brqi = Brqi
		self.brvi = Brvi
		
	def status(self):
		print("Seu máximo treshold é: %f" % self.mrthi)
		print("Seu Bui é:  %f" % self.bui)
		print("Seu Brqi está sendo considerado:  %f" % self.brqi)
		Bov = ((self.bui/self.mrthi) * (self.mrthi - self.bui - self.brqi))
#		print("%.2f of Reservation" % Bov)
		print("Verificou o status"); print(" ")

	def request(self, n):
		Bov = ((self.bui/self.mrthi) * (self.mrthi - self.bui - n))
		if (Bov > 0):
			print("Ainda cabe")
			print("Bov: %f" % Bov)
			self.bui = self.bui + (Bov + n)
			self.brqi = self.brqi + n
		else:
			print("Não")

		

uma = QvP(MRthi, Bui, Brqi, BrvA)
uma.status()
uma.request(2)
uma.status()
uma.request(5)
uma.status()
uma.request(10)
uma.status()
uma.request(1)
uma.status()







#	def utilizationRatio(self):
#		x = (self.bui/self.mrthi)
#		print ("Bandwidth usage CoS %.2f" % self.bui)
#		print ("Maximum reservation threshold CoS %.2f" % self.mrthi)
#		print ("%.2f of percent ratio" % x)



	#def bandwidthAvailable(self):
#		y = (self.mrthi - self.bui - self.brqi)
#		print ("Maximum reservation threshold CoS %.2f" % self.mrthi)
#		print ("Bandwidth usage CoS %.2f" % self.bui)
#		print ("%.2f bandwith available" % y)

#		print(" ")
