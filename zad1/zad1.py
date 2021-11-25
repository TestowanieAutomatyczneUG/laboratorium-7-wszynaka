#! python 3.8
class Calculate:
    def dividingints(self,x, y, z):
        if (type(x) == int and type(y) == int and type(z)):
            return x/y/z
        else:
            raise TypeError("Invalid type: {} and {} and {}".format(type(x), type(y), type(z)))
    
    def addWithDocString(self):
        """
        Takes three ints and dividing them
        # >>> c = Calculate()
        >>> c.dividingints(1,1,1)
        1.0
        >>> c.dividingints(1,2,3)
        0.16666666666666666
        >>> c.dividingints(1.5,2,3)
        Traceback (most recent call last):
          File "zad1.py", line 39, in <module>
            print(c.dividingints(1.5,2,3))
          File "zad1.py", line 7, in dividingints
            raise TypeError("Invalid type: {} and {} and {}".format(type(x), type(y), type(z)))
        TypeError: Invalid type: <class 'float'> and <class 'int'> and <class 'int'>
        >>> c.dividingints(1.5,2.33,3/4)
        Traceback (most recent call last):
          File "zad1.py", line 32, in <module>
            print(c.dividingints(1.5,2.33,3/4))
          File "zad1.py", line 7, in dividingints
            raise TypeError("Invalid type: {} and {} and {}".format(type(x), type(y), type(z)))
        TypeError: Invalid type: <class 'float'> and <class 'float'> and <class 'float'>
        
        """


if __name__ == "__main__":
    #c = Calculate()
    #print(c.dividingints(1.5,2,3))
    import doctest
    doctest.testmod(extraglobs={'c': Calculate()})