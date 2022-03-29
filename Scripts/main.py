from vector import Vector


def run():
    # try:
    #     a = int(input("Give me a number: "))
    #     b = int(input("Now give me a number lower than the last one: "))
    #     if a > b:
    #         print(f"""
    #         MCD: {mcd(a, b)}
    #         MCM: {mcm(a, b)}
    #         """)
    # except:
    #     print("Try numeric values:")

    vector_1 = Vector([23, -6, 2])
    vector_2 = Vector([9, 3, -11, 10])

    print(vector_1.pp(vector_2))
    # print(vector_1.pe(5).values)

    # print(prime(int(input("Ingrese un numero: "))))

    # run()


if __name__ == "__main__":
    run()
