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

