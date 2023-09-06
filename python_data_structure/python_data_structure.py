from collections import deque, defaultdict, OrderedDict, Counter

# sorted vs. sort
test_list = [3, 2, 1, 6, 5]

print(sorted(test_list))  # return O
print(test_list)  # 기존 값 그대로

print(test_list.sort())  # return X
print(test_list)  # 기존 값이 변함.

# deque rotate
deque_list = deque([12, 1, 2, 5, 7])

deque_list.rotate(1)
print(deque_list)
deque_list.rotate(2)
print(deque_list)

# defaultDict
default_dict = defaultdict(lambda: 0)  # 값이 없으면 기본적으로 0
print(default_dict['first'])  # 키를 따로 지정하지 않았음에도 지정하지 않은 키 값에 대해서는 default 값 출력

# defaultdict - text mining _ Vector Space Model
text = """A press release is the quickest and easiest way to get free publicity. If
well written, a press release can result in multiple published articles about your
firm and its products. And that can mean new prospects contacting you asking you to
sell to them. ....""".lower().split()  # 단어를 분할 (대소문자 통일)
word_count = defaultdict(lambda: 0)

for word in text:
    word_count[word] += 1  # 동일한 단어가 등장할 때 마다 1씩 증가

default_dict_list = []
for key, value in word_count.items():  # 기존의 dict를 리스트화
    default_dict_list.append([key, value])
# print(default_dict_list)

for i, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items():
    print(i, v)  # 아이템을 갯수에 따라 내린차순 출력

# Counter
c = Counter(['B', 'B', 'S', 'S', 'S'])
print(c)

# Counter은 set 연산을 확장하여 사용 가능
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
print(c + d)  # 합산
print(c & d)  # intersection
print(c | d)  # union

# Counter - word counter
text = """A press release is the quickest and easiest way to get free publicity. If
well written, a press release can result in multiple published articles about your
firm and its products. And that can mean new prospects contacting you asking you to
sell to them. ....""".lower().split()

print(Counter(text))
print(Counter(text)["a"])

# namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=11, y=22)
print(p[0] + p[1])
x, y = p
print(x, y)
print(p.x + p.y)
print(Point(x=11, y=22))