#Add implementation
def add(X,Y):
     return X+Y

#substract implementation
def substract(X,Y):
     return X-Y # on master branch

#multiply implementation
def multiply(X,Y):
     return X*Y  # on Bug456 branch

#divide implementation
def divide(X,Y):
	if Y==0: # on master branch
	   return DIVIDE_BY_O_ERROR
	else:
	   return X/Y

#square imolementation
def square(X):
    return X*X
