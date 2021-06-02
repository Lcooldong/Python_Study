def test1(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


test1(a=1, b=3, c=2)
