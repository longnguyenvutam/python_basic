class Animal:

    def __init__(self,animalType,animalName,animalWidth,animalHeight,animalWeight):
        self.animalType = animalType
        self.animalName = animalName
        self.animalWidth = animalWidth
        self.animalHeight = animalHeight
        self.animalWeight = animalWeight

#Am thanh cua dong vat

    def makeVoice(self):
        print("Unknown")

    def printMe(self):
        print('Animal Type {0}, Animal Name: {1}, Animal Width: {2}, Animal Height: {3}, Animal Weight: {4}'.format(self.animalType,self.animalName,self.animalWidth,self.animalHeight,self.animalWeight))


class Dog(Animal): #class Dog ke thua tu class Animal
#constructor cua lop con
    def __init__(self,name, width, height, weight,isChampion):
        #goi constructor cua lop cha
        Animal.__init__(self,"Dog",name,width,height,weight)
        #gan gia tri cho cac thuoc tinh bo sung
        self.isChampion = isChampion
    
    
    #Override method
    def makeVoice(self):
        print("{0}: Gau Gau".format(self.animalName))


    def takeCareHome(self):
        print("{0} Gru Gru".format(self.animalName))

dog1 = Dog("Lucky","80cm","40cm","20kg",True)
dog2 = Dog("BullDog","150cm","100cm","50kg",True)
dog1.makeVoice()
dog1.printMe()
dog1.takeCareHome()
dog2.makeVoice()
dog2.printMe()
dog2.takeCareHome()


class Cat(Animal):

    def __init__(self,name, width, height, weight,color):
        Animal.__init__(self,"Cat",name,width,height,weight)
        self.color = color

    def makeVoice(self):
        print("{0} Meow Meow".format(self.animalName))

    def catchMouse(self):
        print('{0} catch a mouse'.format(self.animalName))

cat1 = Cat("Jerry","30cm","100cm","10kg","Brown")
cat2 = Cat("Mimi","20cm","10cm","20kg","White")
cat1.makeVoice()
cat1.printMe()
cat1.catchMouse()
cat2.makeVoice()
cat2.printMe()  
cat2.catchMouse()

 