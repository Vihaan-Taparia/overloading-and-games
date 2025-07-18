#ACTIVITY 1
#OVERLOAD
class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self,other):
        if(self.a== other.a):
            return "both are equal"
        else:
            return("Not equal")
ob1=A(2)
ob2=A(3)
print("Passed values:",ob1,ob2)
print(ob1<ob2)


ob3=A(4)
ob4=A(5)
print("Passed values:",ob3,ob4)
print(ob3==ob4)