def finiteDifference(x,y):
	dy=diff(y)
	dx=diff(x)
	dydx=dy/dx
	dydx1=zeros(y.shape,float)
	dydx1[:-1]=diff(y)/diff(x)
	dydx1[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
	return dydx1

def fourPtFiniteDiff(x,y):
	dy=zeros(y.shape,float)
	h=x[1]-x[0]
	dy[2:-2]=(y[0:-4]-8*y[1:-3] + 8*y[3:-1] - y[4:])/(12.*h)
	dy[0]=(y[1]-y[0])/(x[1]-x[0])
	dy[1]=(y[2]-y[1])/(x[2]-x[1])
	dy[-2]=(y[-2]-y[-3])/(x[-2]-x[-3])
	dy[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
	return dy
