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
    
    
    
    #3/30
    
    matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]

    list(zip(*matrix))\
    #zipは入力したものから一つずつとってタプルを作る
    Out[2]: [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

    list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
    Out[3]: [(0, 'fee'), (1, 'fi'), (2, 'fo')]

    a = [-1, 1, 66.25, 333, 333, 1234.5]

    del a[0]\
    #popと違い値を返さない

    a
    Out[6]: [1, 66.25, 333, 333, 1234.5]

    del a[2:4]

    a
    Out[8]: [1, 66.25, 1234.5]

    del a

    #消えたのでaを入力するとエラーが出る

    t = 12345, 54321, 'hello'

    t[0]
    Out[12]: 12345

    t[0]=88888\
    #tapleは不変
    Traceback (most recent call last):

      File "C:\Users\81906\AppData\Local\Temp/ipykernel_24296/1213624705.py", line 1, in <module>
        t[0]=88888\

    TypeError: 'tuple' object does not support item assignment


    t
    Out[14]: (12345, 54321, 'hello')

    u = t, (1, 2, 3, 4, 5)

    u
    Out[16]: ((12345, 54321, 'hello'), (1, 2, 3, 4, 5))

    v = ([1, 2, 3], [3, 2, 1])\
    #可変なオブジェクトを含むことはできる

    v
    Out[18]: ([1, 2, 3], [3, 2, 1])

    empty = ()\
    #空のタプル

    singleton = 'hello', \
    #一つの項目からなるタプルはコンマが必要

    len(empty)
    Out[21]: 0

    len(singleton)
    Out[22]: 1

    singleton
    Out[23]: ('hello',)

    x, y, z = t\
    #シーケンスのアンパック

    x
    Out[25]: 12345

    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

    print(basket)
    {'pear', 'orange', 'banana', 'apple'}

    'orange' in basket
    Out[28]: True

    'crabgrass' in basket
    Out[29]: False

    a = set('abracadabra')\
    #setというオブジェクトができ、可変

    b = set('alacazam')

    a
    Out[32]: {'a', 'b', 'c', 'd', 'r'}

    a - b
    Out[33]: {'b', 'd', 'r'}

    a | b#a or b
    Out[34]: {'a', 'b', 'c', 'd', 'l', 'm', 'r', 'z'}

    a & b
    Out[35]: {'a', 'c'}

    a ^ b#対称差
    Out[36]: {'b', 'd', 'l', 'm', 'r', 'z'}

    a = {x for x in 'abracadabra' if x not in 'abc'}

    a
    Out[38]: {'d', 'r'}

    tel = {'jack':4098, 'sape':4139}\
    #辞書

    tel['guido'] = 4127

    tel
    Out[41]: {'jack': 4098, 'sape': 4139, 'guido': 4127}

    tel['jack']
    Out[42]: 4098

    del tel['sape']

    tel['irv'] = 4127

    tel
    Out[45]: {'jack': 4098, 'guido': 4127, 'irv': 4127}

    list(tel)
    Out[46]: ['jack', 'guido', 'irv']

    'guido' in tel
    Out[47]: True

    'jack' not in tel
    Out[48]: False

    dict([('sape',4139), ('guido', 4127), ('jack', 4098)])\
    #dictはキーと値のペアのタプルを含むリストから辞書を作る
    Out[49]: {'sape': 4139, 'guido': 4127, 'jack': 4098}

    {x: x**2 for x in (2, 4, 6)}\
    #辞書内包表現
    Out[50]: {2: 4, 4: 16, 6: 36}

    dict(sape=4139, guido=4127, jack = 4098)
    Out[51]: {'sape': 4139, 'guido': 4127, 'jack': 4098}
    
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}

    for k,v in knights.items():
        print(k,v)
        #itemメソッドを使うとキーと対応する値を同時に取り出す
        
    gallahad the pure
    robin the brave
    
    for i,v in enumerate(['tic', 'tac', 'toe']):
        print(i,v)
        
    0 tic
    1 tac
    2 toe

    #要素とインデックスを同時に取り出す

    questions = ['name', 'quest', 'favorite color']

    answers = ['lancelot', 'the holy grail', 'blue']

    for q,a in zip(questions, answers):
        print('What is your {0}? It is {1}.'.format(q, a))
        
    What is your name? It is lancelot.
    What is your quest? It is the holy grail.
    What is your favorite color? It is blue.

    #zipを使うと2つ以上のシーケンス型を同時にループできる

    for i in reversed(range(1, 10, 2)):
        print(i)
        
    9
    7
    5
    3
    1

    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

    for i in sorted(basket):
        print(i)
        
    apple
    apple
    banana
    orange
    orange
    pear

    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

    for f in sorted(set(basket)):
        print(f)
        
    apple
    banana
    orange
    pear

    import math

    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

    filtered_data = []
    
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)
            

    filtered_data
    Out[17]: [56.2, 51.7, 55.3, 52.5, 47.8]

    string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'

    non_null = string1 or string2 or string3

    non_null
    Out[20]: 'Trondheim'
    


    
#4/4

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    #printをwhileにそろえると結果が改行なしで出力される
    

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
    #returnをwhileの方に揃えないと0
    

cd Desktop
C:\Users\81906\Desktop

cd intro_py
C:\Users\81906\Desktop\intro_py

import fibo

fibo.fib(100)\
#関数にアクセス
0 1 1 2 3 5 8 13 21 34 55 89 

fibo.fib2(100)
Out[7]: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

fibo.__name__
Out[8]: 'fibo'

fib = fibo.fib

fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 

from fibo import fib, fib2

fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 

from fibo import *\
#モジュールで定義されている名前を全てimport

fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 

import fibo as fib

fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 

from fib import fib as fibonacci
Traceback (most recent call last):

  File "C:\Users\81906\AppData\Local\Temp/ipykernel_10400/1335766475.py", line 1, in <module>
    from fib import fib as fibonacci

ModuleNotFoundError: No module named 'fib'


from fibo import fib as fibonacci

fibonacci (500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 

run -i fibo.py 50
0 1 1 2 3 5 8 13 21 34 

#IPythonのコマンドを使う

import sys 

sys.ps1 #1次プロンプトに表示する文字列
Out[23]: 'In : '

sys.ps2 #2次プロンプトに表示する文字列
Out[24]: '...: '

import fibo, sys

dir(fibo)
Out[26]: 
['__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'fib',
 'fib2']

a = [1, 2, 3, 4, 5]

import fibo

fib = fibo.fib

dir() #定義してる名前を列挙
Out[30]: 
['In',
 'Out',
 '_',
 '_23',
 '_24',
 '_26',
 '_7',
 '_8',
 '__',
 '___',
 '__builtin__',
 '__builtins__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_dh',
 '_i',
 '_i1',
 '_i10',
 '_i11',
 '_i12',
 '_i13',
 '_i14',
 '_i15',
 '_i16',
 '_i17',
 '_i18',
 '_i19',
 '_i2',
 '_i20',
 '_i21',
 '_i22',
 '_i23',
 '_i24',
 '_i25',
 '_i26',
 '_i27',
 '_i28',
 '_i29',
 '_i3',
 '_i30',
 '_i4',
 '_i5',
 '_i6',
 '_i7',
 '_i8',
 '_i9',
 '_ih',
 '_ii',
 '_iii',
 '_oh',
 'a',
 'exit',
 'fib',
 'fib2',
 'fibo',
 'fibonacci',
 'get_ipython',
 'quit',
 'sys']

import builtins

dir(builtins) #組み込みの関数や変数をリストするにはbuiltins
Out[32]: 
['ArithmeticError',
 'AssertionError',
 'AttributeError',
 'BaseException',
 'BlockingIOError',
 'BrokenPipeError',
 'BufferError',
 'BytesWarning',
 'ChildProcessError',
 'ConnectionAbortedError',
 'ConnectionError',
 'ConnectionRefusedError',
 'ConnectionResetError',
 'DeprecationWarning',
 'EOFError',
 'Ellipsis',
 'EnvironmentError',
 'Exception',
 'False',
 'FileExistsError',
 'FileNotFoundError',
 'FloatingPointError',
 'FutureWarning',
 'GeneratorExit',
 'IOError',
 'ImportError',
 'ImportWarning',
 'IndentationError',
 'IndexError',
 'InterruptedError',
 'IsADirectoryError',
 'KeyError',
 'KeyboardInterrupt',
 'LookupError',
 'MemoryError',
 'ModuleNotFoundError',
 'NameError',
 'None',
 'NotADirectoryError',
 'NotImplemented',
 'NotImplementedError',
 'OSError',
 'OverflowError',
 'PendingDeprecationWarning',
 'PermissionError',
 'ProcessLookupError',
 'RecursionError',
 'ReferenceError',
 'ResourceWarning',
 'RuntimeError',
 'RuntimeWarning',
 'StopAsyncIteration',
 'StopIteration',
 'SyntaxError',
 'SyntaxWarning',
 'SystemError',
 'SystemExit',
 'TabError',
 'TimeoutError',
 'True',
 'TypeError',
 'UnboundLocalError',
 'UnicodeDecodeError',
 'UnicodeEncodeError',
 'UnicodeError',
 'UnicodeTranslateError',
 'UnicodeWarning',
 'UserWarning',
 'ValueError',
 'Warning',
 'WindowsError',
 'ZeroDivisionError',
 '__IPYTHON__',
 '__build_class__',
 '__debug__',
 '__doc__',
 '__import__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'abs',
 'all',
 'any',
 'ascii',
 'bin',
 'bool',
 'breakpoint',
 'bytearray',
 'bytes',
 'callable',
 'cell_count',
 'chr',
 'classmethod',
 'compile',
 'complex',
 'copyright',
 'credits',
 'debugcell',
 'debugfile',
 'delattr',
 'dict',
 'dir',
 'display',
 'divmod',
 'enumerate',
 'eval',
 'exec',
 'execfile',
 'filter',
 'float',
 'format',
 'frozenset',
 'get_ipython',
 'getattr',
 'globals',
 'hasattr',
 'hash',
 'help',
 'hex',
 'id',
 'input',
 'int',
 'isinstance',
 'issubclass',
 'iter',
 'len',
 'license',
 'list',
 'locals',
 'map',
 'max',
 'memoryview',
 'min',
 'next',
 'object',
 'oct',
 'open',
 'ord',
 'pow',
 'print',
 'property',
 'range',
 'repr',
 'reversed',
 'round',
 'runcell',
 'runfile',
 'set',
 'setattr',
 'slice',
 'sorted',
 'staticmethod',
 'str',
 'sum',
 'super',
 'tuple',
 'type',
 'vars',
 'zip']



#4/5

year = 2016

event = 'Referendum'

f'Result of the {year} {event}'\
#{}の中にpythonの式を書ける
Out[3]: 'Result of the 2016 Referendum'

yes_votes = 42_572_654

no_votes = 43_132_495

percentage = yes_votes / (yes_votes + no_votes)

'{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)\
#{index:最小幅, .小数点以下の桁数 型}
Out[7]: ' 42572654 YES votes 49.67%'

s = 'Hello, world.'

str(s)
Out[9]: 'Hello, world.'

repr(s)
Out[10]: "'Hello, world.'"

str(1/7)
Out[11]: '0.14285714285714285'

x = 10 * 3.25

y = 200 * 200

s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'

print(s)
The value of x is 32.5, and y is 40000...

hello = 'hello, world\n'

hellos = repr(hello)

print(hellos)
'hello, world\n'

repr(hello)
Out[19]: "'hello, world\\n'"

repr((x, y, ('spam', 'eggs')))\
#reprはpython objectでもいい
Out[20]: "(32.5, 40000, ('spam', 'eggs'))"

import math

print(f'The valueof pi is apporoximately {math.pi:.3f}.')
The valueof pi is apporoximately 3.142.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
    #:の後ろに整数を着けると最小幅を指定できる
    
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678

animals = 'eels'

print(f'My hovecraft is full of {animals}.')
My hovecraft is full of eels.

print(f'My hovecraft is full of {animals!r}.')\
#書式指定ミニ言語仕様　'!a' は ascii() を、 '!s' は str() を、 '!r' は repr() を適用
My hovecraft is full of 'eels'.

print('We are the {} who say "{}"!'.format('knights', 'Ni'))
We are the knights who say "Ni"!

print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs

print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

print('This {food} is {adjective}.'.format(food='spam', adjective= 'absolutely horrible'))
This spam is absolutely horrible.

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other = 'Georg'))
The story of Bill, Manfred, and Georg.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '\
'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'\
.format(**table))\
#キーワード引数として渡す
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

for x in range (1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3)\
    , end = ' ')
    print(repr(x*x*x).rjust(4))
    
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

'12'.zfill(5)\
#数値文字の左側をゼロ詰め
Out[38]: '00012'

'-3.14'.zfill(7)
Out[39]: '-003.14'

'3.14159265359'.zfill(5)\
#長すぎるとそのまま返す
Out[40]: '3.14159265359'

import math

print('The value of pi is apporoximately %5.3f.'% math.pi)\
#%最小幅.小数点以下の桁数だと思う
The value of pi is apporoximately 3.142.

#4/6



with open('workfile.txt') as f:
...     read_data = f.read()
    

f.closed
Out[2]: True

f = open('workfile.txt', 'rb+')

f.read()
Out[4]: b"0123456789abcdefer', 42)"

f.read()
Out[5]: b''

f.readline()
Out[6]: b''

for line in f:
...     print(line, end='')
...


f.write('This is a test\n')
Traceback (most recent call last):

  File "C:\Users\81906\AppData\Local\Temp/ipykernel_4152/1403935874.py", line 1, in <module>
    f.write('This is a test\n')

TypeError: a bytes-like object is required, not 'str'


f.write(b'0123456789abcdef')
Out[9]: 16

f.seek(5)
Out[10]: 5

f.read(1)
Out[11]: b'5'

f.seek(-3, 2)  # Go to the 3rd byte before the end
Out[12]: 37

#aaa