// ~/code/scala/demo/functions.sc


def add(x: Int, y: Int): Int = {
  x + y
}


add(2,5)


add(y=2, x=1)


def addWithDefault(x: Int, y: Int = 0): Int = x + y

addWithDefault(3)



def sub(x: Int, y: Int): Int = x - y


def calc(x: Int, y: Int, op: (Int,Int)=>Int): Int = op(x,y)

calc(5,6,add)
calc(5,6,sub)


def isFactor(x: Int, y: Int) = y % x == 0
isFactor(10, 100)
isFactor(3, 100)






def factorial(n: Int): Int = if (n==1) 1 else n * factorial(n-1)

factorial(6)





