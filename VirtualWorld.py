VW_World_None = 0.1
VW_World_Neg = -VW_World_None
VW_World_True = 0.9999999999999999
# 上面两者的关联
i = 10
sums = 0
while i > 0:
    sums += VW_World_None
    i -= 1
print(sums)


if __name__ == '__main__':
    pass
