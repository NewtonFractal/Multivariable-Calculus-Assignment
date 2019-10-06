from scipy.integrate import quad

def f(t):
    return (4*(t**2)+9*(t**4))**(1/2)

lenght = quad(f,-2,1)

print(lenght)
