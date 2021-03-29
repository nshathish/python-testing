def add_this(x, y):
    import pdb; pdb.set_trace()
    print(f"x: {x}, type(x): {type(x)}")
    print(f"y: {y}, type(y): {type(y)}")

    try:
        result = x + y
    except TypeError:
        print(f"The wrong type parsed")
        result = int(x) + int(y)

    print(f"result: {result}")
    return result


print(add_this("1", 2))
