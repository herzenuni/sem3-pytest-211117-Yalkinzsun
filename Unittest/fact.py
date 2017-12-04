def fact(n):
    res = None
    try: 
        if type(n) is not int:
            raise TypeError 
        n = int(n)
    except (ValueError, TypeError) as e:
        print('Argument "{}" is not a number '.format(n))
    else: 
        if n < 0:
            print('Argument "{}" less than 0 '.format(n))
        elif n == 0:
            return 1
        else:
            res = n * fact(n-1)
            return res 

if __name__ == '__main__':
    import unittest
    
    
