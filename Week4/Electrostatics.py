def pointPotential(X,Y,q,posx,posy):
	k=8.987551787
	return k*q/((X-posx)**2 + (Y-posy)**2)**(1./2.)

def dipolePotential(X,Y,q,d):
	k=8.987551787
	return (k*q/((X-d)**2 + Y**2)**(1./2.))-(k*q/((X+d)**2 + Y**2)**(1./2.))
