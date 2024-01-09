import traceback


# ZeroDivisionError : UpperCamelCase, PascalCase => class
# helloWorld : camelCase
# hello_world : snack_case

# hello-world : kebab-case


def div(a,b):
    return a/b

def call_div(a,b):
    try:
        print("open log")
        c = div(a,b)
    finally:
        print("close log")

    return c


def main():


    try:
        a = 2
        b = int(input("Valeur de b: ") )
        c = call_div(a,b)
        print(c)
    # except ZeroDivisionError as e:
    #     print(e)
    #     traceback.print_exc()
    # except TypeError as e:
    #     print(e)
    #     traceback.print_exc()
    # except ValueError as e:
    #     print(e)
    #     traceback.print_exc()
    except Exception as e:
        print(e)
        traceback.print_exc()
    
    else:
        print("pas d'erreur")
    finally:
        print("finally")

    print("après")

if __name__ == '__main__':
    main()