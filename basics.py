import re 

def tryCatchExample(a, b):
    try :
        x = a / b
        if b == 1:
            x = x / c
        if b == 2:
            x = x / int("abc")
        if b == 3:
            fileHandle = open("sample123")
            data = fileHandle.readlines()
            fileHandle.close()
        
        print("Output is: ", x)
    
    except ZeroDivisionError as e:
        print("ZeroDivisionError exception occurred: ", e)
    except NameError as e:
        print("NameError exception occurred: ", e)
    except ValueError as e:
        print("ValueError exception occurred: ", e)
    except TypeError as e:
        print("TypeError exception occurred: ", e)
    except OSError as e:
        print("OSError exception occurred: ", e)
    except RuntimeError as e:
        print("RuntimeError exception occurred: ", e)
    except Exception as e:
        print("An exception occurred:: ", e)
    else:
        print("No exception in case of  %s / %s :  %s" % (str(a), str(b), str(x)))
    finally:
        print("End of Function")


def searchString():
    txt = " 10.0.0.100 "
    x=re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", txt)

    if x:
        print("YES! We have a match: ", x.group(0))
    else:
        print("No match")
    
    
    


if __name__ == '__main__':
    
    '''
    print ("Excaptions: ZeroDivisionError, NameError, ValueError, TypeError, OSError, RuntimeError")
    tryCatchExample(10, 0)
    tryCatchExample(10, "abc")
    tryCatchExample(10, 1)
    tryCatchExample(10, 2)
    tryCatchExample(10, 3)
    tryCatchExample(10, 4)
    '''
    
    print ("Regular exceptions:")
    searchString()