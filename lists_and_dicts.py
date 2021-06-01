def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Nicolas", "lastname":"Córdoba"}

    super_list = [
        {"firstname": "Nicolas", "lastname":"Córdoba"},
        {"firstname": "Santiago", "lastname":"Córdoba"},
        {"firstname": "Andrea", "lastname":"Gonzalez"},
        {"firstname": "Raymond", "lastname":"Mansell"},
        {"firstname": "Diana", "lastname":"Salazar"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.2, 4.7, 2.4, 3.8, 4.2]
    }

    for i in super_list:
        for key, value in i.items():
            print(key, "-", value)


if __name__ == '__main__':
    main()