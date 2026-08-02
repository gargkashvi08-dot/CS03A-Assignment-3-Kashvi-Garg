# /*****************************************************/
# /* CS03A - Summer 2026
# /* Assignment 3 - Question 2
# /* Student Name: Kashvi Garg
# /* SID: 20744788
# /*****************************************************/

class Employee:
    def __init__(self,name='',number=0):
        self.name=name
        self.number=number

    def getName(self):
        return self.name

    def setName(self,name):
        self.name=name

    def getNumber(self):
        return self.number

    def setNumber(self,number):
        self.number=number

class ProductionWorker(Employee):
    def __init__(self,name='',number=0,shift=1,payRate=0.0):
        super().__init__(name,number)
        self.shift=shift
        self.payRate=payRate

    def getShift(self):
        return self.shift

    def setShift(self,shift):
        self.shift=shift

    def getPayRate(self):
        return self.payRate

    def setPayRate(self,payRate):
        self.payRate=payRate

def run():
    worker=ProductionWorker()

    name=input('Enter employee name: ')
    number=input('Enter employee number: ')
    shift=int(input('Enter shift (1 for day, 2 for night): '))
    payRate=float(input('Enter hourly pay rate: '))

    worker.setName(name)
    worker.setNumber(number)
    worker.setShift(shift)
    worker.setPayRate(payRate)

    print('Name: '+worker.getName())
    print('Number: '+worker.getNumber())
    print('Shift: '+str(worker.getShift()))
    print('Pay rate: '+str(worker.getPayRate()))

if __name__=='__main__':
    run()
