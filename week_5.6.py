try:
    a = 10/0
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    a = int("Anurag")
except (ValueError,TypeError) as e:
    print(f"Error: {e}")

try:
    a = int("Anurag")
except:
    print("This will catch an error")

try:
    import anurag
except Exception as e:
    print(f"Error: {e}")

try:
    d = {"key":"Anurag",1:[12,3,4,5]}
    print(d["key2"])
except KeyError as e:
    print(f"Key is not present, Error:{e}")

try:
    "sah".test()
except Exception as e:
    print(f"Error :{e}")

try:
    l = [2,3,4,5]
    print(l[9])
except IndexError as e:
    print(f"Index Error Occurs: {e}")

try:
    a = 1+"int"
except Exception as e:
    print(f"Error: {e}")

def test(file):
    try:
        with open(file,"r") as f:
            file = f.read()
    except ValueError as e:
        print(f"Error1: {e}")
    except Exception as e:
        print(f"Error2: {e}")
test("text.txt")

# print(dir(Exception))


