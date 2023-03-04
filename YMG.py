
import random
import string
characters = string.ascii_letters + string.digits+string.punctuation
prn = ''.join(random.choices(characters, k=3))
a = ''.join(random.choices(characters, k=1))
b = ''.join(random.choices(characters, k=1))
c = ''.join(random.choices(characters, k=1))
d = ''.join(random.choices(characters, k=1))
e = ''.join(random.choices(characters, k=1))
f = ''.join(random.choices(characters, k=1))
g = ''.join(random.choices(characters, k=1))
h = ''.join(random.choices(characters, k=1))
i = ''.join(random.choices(characters, k=1))
j = ''.join(random.choices(characters, k=1))
k = ''.join(random.choices(characters, k=1))
l = ''.join(random.choices(characters, k=1))
m = ''.join(random.choices(characters, k=1))
n = ''.join(random.choices(characters, k=1))
o = ''.join(random.choices(characters, k=1))
p = ''.join(random.choices(characters, k=1))
q = ''.join(random.choices(characters, k=1))
r = ''.join(random.choices(characters, k=1))
s = ''.join(random.choices(characters, k=1))
t = ''.join(random.choices(characters, k=1))
u = ''.join(random.choices(characters, k=1))
v = ''.join(random.choices(characters, k=1))
w = ''.join(random.choices(characters, k=1))
x = ''.join(random.choices(characters, k=1))
y = ''.join(random.choices(characters, k=1))
z = ''.join(random.choices(characters, k=1))
ob = ''.join(random.choices(characters, k=2))
cb = ''.join(random.choices(characters, k=2))
str = ''.join(random.choices(characters, k=2))
bs = ''.join(random.choices(characters, k=2))
fs = ''.join(random.choices(characters, k=2))
com = ''.join(random.choices(characters, k=2))
var = ''.join(random.choices(characters, k=3))
ocb = ''.join(random.choices(characters, k=2))
ccb = ''.join(random.choices(characters, k=2))
emar = ''.join(random.choices(characters, k=2))

print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,prn)

replacements_dict = {
    prn: "print",
    a: "a",
    b: "b",
    c: "c",
    d: "d",
    e: "e",
    f: "f",
    g: "g",
    h: "h",
    i: "i",
    j: "j",
    k: "k",
    l: "l",
    m: "m",
    n: "n",
    o: "o",
    p: "p",
    q: "q",
    r: "r",
    s: "s",
    t: "t",
    u: "u",
    v: "v",
    w: "w",
    x: "x",
    y: "y",
    z: "z",
    ob: "(",
    cb: ")",
    str: "\"",
    fs: "/",
    bs: "\\",
    com: ",",
    ocb: "{",
    ccb: "}",
    emar: "!",
    

}  # Dictionary of replacements
def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""

fl = input("Enter name of YMG File to run: ")

with open(fl, "r") as f:  # Open file for reading
    file_contents = f.read()  # Read file contents
    for old_val, new_val in replacements_dict.items():
        if old_val in file_contents:
            file_contents = file_contents.replace(old_val, new_val)  # Replace all occurrences of old value with new value
        splittin = file_contents.splitlines()


def anal():
    try:
        if "print(" in line:     
            print(eval(line))
        if var in line:
            varname = find_between(line,ob,cb)
            vardata = find_between(line,ocb,ccb)
            globals()[varname] = eval(vardata)

    except SyntaxError as e:
        print("\033[1;31mCaught Syntax Error\033[0m")
        print("")
        print("\033[1;31mFile: "+fl+"\033[0m")
        print("\033[1;31m     "+"^"*len(fl)+"\033[0m")
        print("\033[1;31m"+e.msg+"\033[0m")
        print("\033[1;31mLN:"+str(e.lineno)+"\nCOL:"+str(e.offset)+"\033[0m")
        print("\033[1;35;3mHelp, Your code has a "+e.msg+"\nYour code that is causing this issue is '"+str(e.args[1])+"'\033[0m")
        print("\033[1;35;3m                                         "+"^"*len(str(e.args[1]))+"\033[0m")
for i, line in enumerate(splittin):
    anal()