import argparse

parser = argparse.ArgumentParser(
    description="SUm tow integers."
)

parser.add_argument(
    '-a', '--a_value',
    dest='a', help='A integers', type=int,
    required=True
)

parser.add_argument(
    '-b', '--b_value',
    dest='b', help='B integers', type=int,
    required=True
)

# 이러한 코드를 통해 사전에 실험(test)가 가능하다...
args = parser.parse_args()
print(args)
print(args.a)
print(args.b)
print(args.a + args.b)
