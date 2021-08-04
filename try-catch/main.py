thinkers = ["Plato", "Aristotle", "Gumby"]
while True:
    try:
        thinker = thinkers.pop()
        print(f"thinker popped: {thinker}")
    except IndexError as e:
        print("We tried to pop too many thinkers!")
        print(e)
        break


def find_mid_value():
    thinkers = ["Plato", "Aristotle", "Torvald", "Gumby", "Mahomes"]
    if len(thinkers) > 1:
        try:
            calc_middle_value = round(len(thinkers) / 2)
            print(thinkers[calc_middle_value])
        except Exception as e:
            print(e)


find_mid_value()