

def do_log(prefix=""):

    def wrapper_deco(func):

        def wrapper(*args, **kwargs):
            print(prefix,"params", *args, **kwargs)
            # t = args[0].upper() # FRED
            r = func(*args, **kwargs)
            print(prefix,"return", r)
            return r

        return wrapper
    
    return wrapper_deco


@do_log('LOG')
def say_hello(name):
    r = f"Hello {name}"
    return r


def main():
    h = say_hello('Fred')

    print(h)


if __name__ == '__main__':
    main()
