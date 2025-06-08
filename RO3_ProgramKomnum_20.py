

#nomor 20
def f(x): return x**3 + 6*x**2 - 19*x - 84
def df(x): return 3*x**2 + 12*x - 19
def d2f(x): return 6*x + 12

x = 1
x_true = 4

print("\nMetode Newton-Raphson - Soal 20")
print("Iterasi |     x    |     Et  |     Ea    ")
print("--------------------------------------------")

for i in range(1, 4):
    fx = f(x)
    dfx = df(x)
    d2fx = d2f(x)
    x_new = x - (fx * dfx) / (dfx**2 - fx * d2fx)
    
    Et = x_true - x_new
    Ea = abs(x_new - x)
    
    print(f"{i:^7} | {x_new:8.2f} | {Et:8.2f} | {Ea:8.2f}")
    x = x_new
