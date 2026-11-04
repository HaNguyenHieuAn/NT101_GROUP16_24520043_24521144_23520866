import hashlib, sys

def md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def check(f1, f2):
    a = open(f1, "rb").read()
    b = open(f2, "rb").read()
    diff = [i for i in range(min(len(a), len(b))) if a[i] != b[i]]
    print(f"{f1}: {len(a)} byte | MD5 = {md5(f1)}")
    print(f"{f2}: {len(b)} byte | MD5 = {md5(f2)}")
    print("Cung MD5     :", md5(f1) == md5(f2))
    print("Noi dung khac:", a != b)
    print("So byte khac :", len(diff))
    print("Vi tri khac  :", diff)

check(sys.argv[1], sys.argv[2])
