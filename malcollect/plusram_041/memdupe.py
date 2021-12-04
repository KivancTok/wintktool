import random

import malcollect.withtaskrun

eng_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def start():
    with malcollect.withtaskrun.RunTask("Reading RAM"):
        for i in range(50):
            with open(str([random.choice(eng_alphabet) for _ in range(7)]), "w") as f:
                f.write(str([random.choice(eng_alphabet) for _ in range(100)]))

    with malcollect.withtaskrun.RunTask("Creating pagefile"):
        with open("C:\\CustPageFile\\pgf.pypage", "w"):
            f.write(str([random.choice(eng_alphabet) for _ in range(4 * (2 ** 20))]))
