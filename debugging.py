def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError("Haz el número positivo")
        else:
            for i in range(1, num +1):
                if num % i == 0:
                    divisors.append(i)
            return divisors
    except ValueError as ve:
        print(ve)
        return str (num) + " no es un numero positivo"


def run():
    try:
        num = int(input('Ingresa un número: '))
        #if num < 0:
        #    num = num * -1
        print(divisors(num))
        
        print('Hasta aquí voy')
    except ValueError:
        print("Ingresa un número")


if __name__ == "__main__":
    run()