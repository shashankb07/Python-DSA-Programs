def russianDoll(Doll):
    if Doll == 1:
        print('All the dolls are opened!')
    else:
        russianDoll(Doll - 1)
        print(Doll)
russianDoll(2)