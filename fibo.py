def recursive_nht_fibo(n):
    if n== 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (recursive_nht_fibo(n-1) + recursive_nht_fibo(n-2))



def main():
    number = int(input("kolik prvků chceš"))
    fs = [recursive_nht_fibo(n) for i in range(number)]
    print(fs)


if __name__ == '__main__':
    main()
