def pointPotential(X,Y,q,xpos,ypos):
	return k*q/((X-xpos)**2 + (Y-ypos)**2)**(1./2.)

def dipolePotential (X,Y,q,d):
	return (k*q/((X-d)**2 + Y**2)**(1./2.))-(k*q/((X+d)**2 + Y**2)**(1./2.))
