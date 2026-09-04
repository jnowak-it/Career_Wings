# 🇵🇱Stwórz funkcję equation, która przyjmuje współczynniki a, b, c równania kwadratowego i oblicza jego rozwiązania.
# Najpierw wyznacz deltę, a potem zwróć wynik zależnie od jej znaku.
# 1. delta > 0: dwa rozwiązania x1 i x2 (zwróć jako krotkę),
# 2. delta = 0: jedno rozwiązanie x0,
# 3. delta < 0: brak rozwiązań (zwróć tekst „Brak rozwiązań”).
import math


# 🇬🇧Create a function called equation that takes the coefficients a, b, c of a quadratic equation and calculates its
# solutions. First determine the delta, then return the result depending on its sign.
# 1. delta > 0: two solutions x1 and x2 (return as a tuple),
# 2. delta = 0: one solution x0,
# 3. delta < 0: no solutions (return the text "No solutions").

import math

def equation(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return round(x1, 2), round(x2, 2)
    elif delta == 0:
        x0 = (-b / (2*a))
        return x0
    else:
        return "No solutions"

print(equation(1,2,3))
print(equation(1,6,3))
print(equation(1,-2,1))
