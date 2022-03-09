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


    