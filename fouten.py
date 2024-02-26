import math

def discriminant(a, b, c):
    D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
    D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)
    uitvoer = [D1, D2]
    return uitvoer

print("Voor de formule ax^2 + bx + c, geef a, b en c:")

a = int(input("Waarde a: "))
b = int(input("Waarde b: "))
c = int(input("Waarde c: "))

uitkomst = discriminant(a, b, c)

D1 = uitkomst[0]
D2 = uitkomst[1]

print(f"Waarde A = {a} waarde B = {b} waarde C = {c}, uitkomst D1 = {D1} en D2 = {D2}.")
