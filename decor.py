def greet(fx):
    def mfx(*args,**kwargs):
        fx(*args,**kwargs)
        print("Good Morning")
        print("thanks for using this function")
    return mfx
@greet
def hello():
    print("hello World")
hello()