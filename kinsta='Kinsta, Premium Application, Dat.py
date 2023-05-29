class Cookie:
    # Constructor
    def __init__(self,name,shape,chips='Chocolate'):
        # Instance attributes
        self.name=name
        self.shape=shape
        self.chips=chips
cookie2=Cookie('Awesome cookie','Star')
print(cookie2.name)
print(cookie2.shape)
print(cookie2.chips)