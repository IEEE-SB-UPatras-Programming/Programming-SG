def main():

    n  = 0

    c = 'p'

    while ( c != 'q' ):

        c = input("What do you want to do: ")

        if c == 'n':

            n = int(input(">> "))

        elif c == 'p':
            
            print(n)

        elif c == 'm':

            print(hex(id(n)))

    print(n)

main()
