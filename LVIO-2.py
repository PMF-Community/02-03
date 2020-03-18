a = float(input())
b = float(input())

brojnik = (a+b)
nazivnik = 1 + ((a**2+b**2)/(a**2-b**2))

razlomak = brojnik/nazivnik

#no format
print(razlomak)

#with format
print('{:4.4f}'.format(razlomak))

#ako korisnik unese dva jednaka broja,
#terminal izbaci sljedeci error:
#ZeroDivisionError: float division by zero
