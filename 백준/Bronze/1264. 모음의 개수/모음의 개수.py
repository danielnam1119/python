while True:
    a=input()
    if a=="#":
        break
    else:
        a=a.lower()
        print(a.count("a")+a.count("e")+a.count("i")+a.count("o")+a.count("u"))