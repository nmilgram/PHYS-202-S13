def dipolePotential(x,y,q,d):
    return (k*q/((X-d)**2+Y**2)**(1./2.))+(k*q/((X+d)**2+Y**2)**(1./2.))

def pointPotential(x,y,q,posx,posy):
    (k*q/((X-posx)**2+(Y-posy)**2)**(1./2.))
