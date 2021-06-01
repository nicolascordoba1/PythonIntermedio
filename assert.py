def divisors(num):
        divisors = []
        for i in range(1, num +1):
            if num % i == 0:
                divisors.append(i)
        return divisors


def run():
    num = input('Ingresa un número: ')
    assert int(num) > 0, "Ingresa números mayores a 0"
    assert num.isnumeric(), "Ingresa números"
    print(divisors(int(num)))
    print('Finalizo')

if __name__ == "__main__":
    run()