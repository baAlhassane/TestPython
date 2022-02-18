
i=0;
def random_gen():
    global i
    a=randint(10,20)
    i+=1
    if a!=15:
        print(" not egal to 15.  it's = ", a)
        return random_gen()
    else:
        print(" it generate 15 in  {} times ".format(i))
        return i ;


def decorator_to_str(func):
    # todo exercise 2
    return str(func)


@decorator_to_str
def add(a, b):
    return (a + b)


@decorator_to_str
def get_info(d):
    return d['info']


def ignore_exception(exception):
    # todo exercise 3
    raise exception
    
    
        
           
        


@ignore_exception(ZeroDivisionError)
def div(a, b):
    try:
        x= (a/b)
        return x
    except ZeroDivisionError(" division zero erreo "):
        return 
         

@ignore_exception(TypeError)
def raise_something(exception):
    try:
        raise exception
    except TypeError("errot type"):
        return 


# exercise 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap

def f(*a,**kw):
    return sum(a)
def testCacheDecorator():
    cache=CacheDecorator ()# instance of cache 
    assert cache(f([1,2,3]))==None # __call__ method will be called
    assert cache(f([1,2,3]))==1
    
    
class MetaInherList(type):
    # todo exercise 5
    def __init__(self):
        super().__init__()
    #pass


class Ex:
    x = 4


class ForceToList(Ex, metaclass=MetaInherList):
   def __init__(self,x):
       super().__init__(x)
       self.x=x
       

class TestClass( Ex,object, metaclass=ForceToList):
      def __init__(self):
          super().__init__()
          
      def __getattribute__(self,name):
          if name=='process':
              return 0
          else:
              return object.__getattribute__(self, name)
        
    
if __name__ == '__main__':
    a=random_gen()
    print(a)

    
