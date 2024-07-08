
def mydec(func):
    def wrap():
        print("@@@@@@")
        func()
        print("@@@@@@")
    return wrap



@mydec
def hello():
    print("helloooo")

hello()