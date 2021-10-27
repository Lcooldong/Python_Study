# 원래 것에 상관없이 원하는 것 0으로 변경
result1 = 0xFF & 0xAA
print('And1 : 0x%x' % result1)
result1 = 0xFF & ~0x12
print('And2 : 0x%x' % result1)
print(bin(0b1111 & 0b0010))
print(bin(0b1011 & ~0b1101))

print('-----------------')
# 원하는 것 1으로 변경

result2 = 0xF1 | 0xA3
print('or : 0x%x' % result2)
print(bin(0b1010 | 0b1101))
print(bin(0b0001 | ~0b0011))    # 0b1101(2의 보수) -> 0010 + 1 = 0011 = 3
print(f'{-0b11}')
print(bin(0b0001 | ~0b1101))    # 1101 = 13 -> ~1101 = -14
print(f'{~0b1101}')
print(f'{-0b1101}')

print('-----------------')
# 반전(서로 다른 것만 출력)

result3 = 0x03 ^ 0x02
print('xor : 0x%x' % result3)
print(bin(0b1010 ^ 0b0110))


