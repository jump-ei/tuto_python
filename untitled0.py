print(2+2,17/3,17//3 #切り捨て 
      ,17%3 #余り
     ,5**2 #累乗
     )
width = 20 #代入
height = 5*9
print(width*height)
print((3+5j)*(3-5j) #複素数
      )

2+2
Out[1]: 4

3+_ #最後に表示した結果は_に代入される
Out[2]: 7

'"Yes,"they said.'
Out[3]: '"Yes,"they said.'

"\"Yes,\"they said." #引用符は\でエスケープ
Out[4]: '"Yes,"they said.'

'"Isn\'t ,"they said'
Out[5]: '"Isn\'t ,"they said'

print('"Isn\'t ,"they said')
"Isn't ,"they said

s='First line. \nSecond line.' # \n means newline

s # without print() , \n is included newline
Out[8]: 'First line. \nSecond line.'

print(_) # with print() , \n produce a newline
First line. 
Second line.

print('C:\some\name') #\n means newline
C:\some
ame

print(r'C:\some\name') # \に続く文字を特殊文字として解釈されないためには最初の引用符の前にrをつける
C:\some\name

print("""\
Usage:thingy[OPTIONS]
-h Display this usage message
-H hostname Hostname to connect to
""") #三連引用符を使うと複数行にまたがって書ける　改行文字は\を付けるとスキップ
Usage:thingy[OPTIONS]
-h Display this usage message
-H hostname Hostname to connect to


'Py''thon' #並んでると連結
Out[13]: 'Python'

text=('Put several strings within parentheses''to have them joined together')

text
Out[15]: 'Put several strings within parenthesesto have them joined together'

prefix='Py'

prefix+'thon' # 変数と連結するときは+を使う
Out[17]: 'Python'

3*'un'+'ium' #文字の連結と反復
Out[18]: 'unununium'

word='Python'

word[0]
Out[20]: 'P'

word[-1]
Out[21]: 'n'

'Python'[2]
Out[22]: 't'

word[0:2]
Out[23]: 'Py'

word[2:5]
Out[24]: 'tho'

word[:2]+word[2:]
Out[25]: 'Python'

word[4:42]
Out[26]: 'on'

s='supercalifragilisticexpialidocious'

len(s) #長さ
Out[28]: 34

squares = [1, 4, 9, 16, 25]

squares[-1]
Out[30]: 25

squares[-3:] #リストでもスライスができる
Out[31]: [9, 16, 25]

squares[:] #スライスは新しいリストを返す　例えばこれはリストの浅いコピー
Out[32]: [1, 4, 9, 16, 25]

squares + [36,49,64,81,100] #リストの連結
Out[33]: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

[1,2]+[3,4] #リストは並べただけでは連結できない
Out[34]: [1, 2, 3, 4]

cubes = [1,8,27,65,125]

cubes[3]=64

cubes #リストは可変型
Out[37]: [1, 8, 27, 64, 125]

cubes.append(216) #リストの末尾に要素を追加

cubes.append(7**3) #リストの末尾に要素を追加

cubes
Out[40]: [1, 8, 27, 64, 125, 216, 343]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters[2:5]=['C','D','E'] #スライスに代入できる

letters
Out[43]: ['a', 'b', 'C', 'D', 'E', 'f', 'g']

letters[2:5]=[] #スライス消せる

letters
Out[45]: ['a', 'b', 'f', 'g']

letters = ['a', 'b', 'c', 'd']

len(letters) #lenはリストにも使える
Out[47]: 4

a=['a','b','c']

n=[1,2,3]

x=[a,n]

x
Out[51]: [['a', 'b', 'c'], [1, 2, 3]]

x[0] #xはリストのリスト
Out[52]: ['a', 'b', 'c']

x[0][1]
Out[53]: 'b'

print("""s # without print() , \n is included newline
Out[32]: 'First line. \nSecond line.'

print(_) # with print() , \n produce a newline
First line. 
Second line."""
#実行結果を書くこともできる
)




#3/9

a,b=0,1    
while a<10: 
    print(a)
    a,b=b,a+b
    
0
1
1
2
3
5
8

i=256*256
print('The value of i is ',i)
#print関数では文字列は引用符なしで
#要素の間に空白が入り書式が整えられる
The value of i is  65536

a,b=0,1
while a<1000:
    print(a,end=',')
    a,b=b,a+b
    #endを使うと、末尾の改行を出力しないようにしたり
    #別の文字列を末尾に出力したりできる
    
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

x=int(input("Please enter an integer:"))
if x<0:
    x=0
    print('Negative changed to zero')
elif x==0:
    print('Zero')
elif x==1:
    print('Single')
else:print('More')

Please enter an integer:1
Single

words=['cat','window','defenestrate'] 
for w in words :    
    print(w,len(w))
    
cat 3
window 6
defenestrate 12

users = {'Hans':'active','Eleonore':'inactive','景太郎':'active'}
for user , status in users.copy().items():
    if status == 'inactive':
        del users[user]


active_users = {}
for user , status in users.items():
    if status == 'active':
        active_users[user] = status
        

for i in range(5):
    print(i)
    
0
1
2
3
4

for i in range(5,10):
    print(i)
    
5
6
7
8
9

for i in range(0,10,3):
    print(i) #他の増加量
    
0
3
6
9

for i in range(-10,-100,-30):
    print(i) #負の増加量
    
-10
-40
-70

a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i,a[i])
    
0 Mary
1 had
2 a
3 little
4 lamb

print(range(10))
range(0, 10)

sum(range(4))
Out[13]: 6

list(range(4)) #rangeが返すのはリストではなくイテラブル
Out[14]: [0, 1, 2, 3]

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break            
else: #elseの位置
                print(n,'is a prime number')
                
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
9 is a prime number

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break            
    else:
                print(n,'is a prime number')
                
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number",num)
        continue
        print("Found an odd number",num)
        
Found an even number 2
Found an even number 4
Found an even number 6
Found an even number 8

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number",num)
        continue
    print("Found an odd number",num)
    
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9

#continueはループの次のイテレーションを実行

while True:
    pass #文を書くことが要求されているが何もしない時に使う
    
Traceback (most recent call last):

  File "C:\Users\81906\AppData\Local\Temp/ipykernel_3940/2295348535.py", line 2, in <module>
    pass #文を書くことが要求されているが何もしない時に使う

KeyboardInterrupt


class MyEmptyClass:
    pass #最小のクラスを作る
    

def initlog(*args):
    pass #仮置きにも使える
    

def fib(n):\
#defは関数の定義を導く
    a,b = 0,1
    while a<n:
        print(a,end=' ')
        a,b = b,a+b
    pass
    

fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 




#3/22

    def ask_ok(prompt, retries=4, reminder='Please try again!'):
        while True:
            ok = input(prompt)
            if ok in ('y','ye','yes'):
                return True
            if ok in ('n','no','nop','nope'):
                return False
            retries = retries-1
            if retries < 0:
                raise ValueError('invalid user response')
                print(reminder)
                

    ask_ok('Do you really want to quit?')

    Do you really want to quit?y
    Out[2]: True

    ask_ok('s')

    sy
    Out[3]: True

    ask_ok('OK to overwrite the file?', 2)

    OK to overwrite the file?nope
    Out[4]: False

    i=5

    def f(arg=i):
        print(arg)
        #関数が定義された時点で、関数を定義している側のスコープで評価される
        

    i=6

    f()
    5

    def f(a,L=[]):
        L.append(a)
        return L
        

    print(f(1))
    [1]

    print(f(2))
    [1, 2]

    print(f(3)) #関数に渡されている引数を累積
    [1, 2, 3]

    def f(a,L=None):
        if L is None:
            L=[]
            L.append(a)
            return L
            #デフォルト値をき共有しない場合
            #append(a)はリストの末尾にaを追加する
            

    print(f(1))
    [1]

    print(f(2))
    [2]

    def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.")
        print("-- Lovely plumage, the", type)
        print("-- It's", state, "!")
        

    parrot('a thousand', state='pushing up the daisies') #キーワード引数（A＝Bみたいの）は位置引数の後
    -- This parrot wouldn't voom if you put a thousand volts through it.
    -- Lovely plumage, the Norwegian Blue
    -- It's pushing up the daisies !

    def cheeseshop(kind,*arguments,**keywords):
        print("--Do you have any",kind,"?")
        for arg in arguments :
            print(arg)
        print("-"*40)
        for kw in keywords:
            print(kw,":",keywords[kw])
            

    cheeseshop("Limburger","It's very runny sir","It's really runny",shopkeeper="Michael Palin",client="John Cleese",sketch="Cheese Shop Sketch")
    --Do you have any Limburger ?
    It's very runny sir
    It's really runny
    ----------------------------------------
    shopkeeper : Michael Palin
    client : John Cleese
    sketch : Cheese Shop Sketch

    def pos_only_arg(arg, /):
         print(arg)
         

    pos_only_arg(arg=1) #/の前は位置引数
    Traceback (most recent call last):

      File "C:\Users\81906\AppData\Local\Temp/ipykernel_14504/4088751949.py", line 1, in <module>
        pos_only_arg(arg=1) #/の前は位置引数

    TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'


    def kwd_only_arg(*, arg):
        print(arg)
        

    kwd_only_arg(arg=3) #*の直後はキーワード引数
    3

    def combined_example(pos_only, /, standard, *, kwd_only):
        print(pos_only, standard, kwd_only)
        

    combined_example(1, standard=2, kwd_only=3)
    1 2 3

    def foo(name, **kwds):
        return 'name' in kwds
        

    foo(1, **{'name': 2})
    Traceback (most recent call last):

      File "C:\Users\81906\AppData\Local\Temp/ipykernel_14504/396501844.py", line 1, in <module>
        foo(1, **{'name': 2})

    TypeError: foo() got multiple values for argument 'name'


    def foo(name, /, **kwds):
        return 'name' in kwds
        

    foo(1, **{'name': 2})
    Out[29]: True

    #位置専用引数にするとその名前を**kwdsの中で使用しても、曖昧にならない

    def concat(*args,sep="/"):
        return sep.join(args)
        

    concat("earth","mars","venus")
    Out[32]: 'earth/mars/venus'

    #'\n'.joinだと改行しながら結合される

    concat("earth","mars","venus",sep=".")
    Out[34]: 'earth.mars.venus'

    list(range(3, 6))
    Out[35]: [3, 4, 5]

    args = [3, 6]

    list(range(*args))
    Out[37]: [3, 4, 5]

    def parrot(voltage,state='a stiff',action='voom'):
        print("-- This parrot wouldn't",action,end=' ')
        print("if you put",voltage,"volts through it.",end='')
        print("E's",state,"!")
        

    d={"voltage":"four million","state":"bleedin'demised","action":"VOOM"}

    parrot(**d)
    -- This parrot wouldn't VOOM if you put four million volts through it.E's bleedin'demised !

    #*や**でアンパックできる

    def make_incrementor(n):
        return lambda x:x+n
        #lambda 変数:式　で関数を作れる
        

    f=make_incrementor(42)

    f(0)
    Out[44]: 42

    f(1)
    Out[45]: 43

    pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]

    pairs.sort(key=lambda pair: pair[1])

    pairs #list.sort(key=f)ではfの値が小さいものから並べられる　今回は辞書順
    Out[48]: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

    def my_function():
        """D.

        N.
        """
        pass
        

    print(my_function.__doc__)
    D.

        N.
        

    def f(ham:str,eggs:str='eggs')->str:
        print("Annotations:",f.__annotations__)
        print("Annotations:",ham,eggs)
        return ham + 'and' + eggs
        

    f('spam')
    Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
    Annotations: spam eggs
    Out[52]: 'spamandeggs'
    
    
    
    
    #3/23
    
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    fruits.count('apple')
    Out[2]: 2

    fruits.index('banana')
    Out[3]: 3

    fruits.index('banana',4) #4の次のバナナ
    Out[4]: 6

    fruits.reverse()

    fruits
    Out[6]: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

    fruits.sort()

    fruits
    Out[8]: ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']

    fruits.pop()#popは指定しなければ末尾を削除して返す
    Out[9]: 'pear'

    stack = [3, 4, 5]  #スタック（stack）はデータの並びが1次元的で、しかもデータアクセスにLIFO（Last-In First-Out）の制約がついたデータ構造.コマンドによってリストをスタックとして使える.

    stack.append(6)

    stack.append(7)

    stack
    Out[13]: [3, 4, 5, 6, 7]

    stack.pop()
    Out[14]: 7

    stack
    Out[15]: [3, 4, 5, 6]

    stack.pop()
    Out[16]: 6

    stack.pop()
    Out[17]: 5

    stack
    Out[18]: [3, 4]

    from collections import deque

    queue = deque(["Eric", "John", "Michael"])

    queue.append("Terry")

    queue.append("Graham")

    queue.popleft()
    Out[23]: 'Eric'

    queue.popleft()
    Out[24]: 'John'

    queue
    Out[25]: deque(['Michael', 'Terry', 'Graham'])

    squares = []

    for x in range(10):
        squares.append(x**2)
        

    squares #これだとxという変数を上書きしたりする
    Out[28]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    squares = list(map(lambda x: x**2, range(10))) #mapはイテレータを返すのでlistでlistにする　,の右を順番に入れるっぽい

    squares = [x**2 for x in range(10)]

    [(x,y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y] #リストの内包表記
    Out[31]: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    combs = []

    for x in [1, 2, 3]:
        for y in [3, 1,4]:
            if x != y:
                combs.append((x, y))
                

    combs
    Out[34]: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    vec = [-4, -2, 0, 2, 4]

    [x*2 for x in vec]
    Out[36]: [-8, -4, 0, 4, 8]

    [x for x in vec if x >= 0]
    Out[37]: [0, 2, 4]

    [abs(x) for x in vec]
    Out[38]: [4, 2, 0, 2, 4]

    freshfruit = [' banana', ' loganberry', ' passion fruit']

    freshfruit
    Out[40]: [' banana', ' loganberry', ' passion fruit']

    [weapon.strip() for weapon in freshfruit] #stripは空白を削除する
    Out[41]: ['banana', 'loganberry', 'passion fruit']

    [(x,x**2) for x in range(6)] #()が必要
    Out[42]: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

    vec = [[1, 2, 3],[4, 5, 6,],[7, 8, 9]]

    [num for elem in vec for num in elem]
    Out[44]: [1, 2, 3, 4, 5, 6, 7, 8, 9]

    from math import pi

    [str(round(pi, i)) for i in range(1,6)] #roundは右の桁数まで四捨五入する　strは数値を文字列に変換する
    Out[46]: ['3.1', '3.14', '3.142', '3.1416', '3.14159']

    matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]

    [[a[i] for a in matrix] for i in range(4)] #aのところは一致してればなんでもよい
    Out[48]: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    transposed = []

    for i in range(4):
        transposed.append([a[i] for a in matrix])
        

    transposed
    Out[51]: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    for i in range(4):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
        

    transposed
    Out[53]: 
    [[1, 5, 9],
     [2, 6, 10],
     [3, 7, 11],
     [4, 8, 12],
     [1, 5, 9],
     [2, 6, 10],
     [3, 7, 11],
     [4, 8, 12]]