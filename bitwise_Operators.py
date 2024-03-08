print(5 >> 4)
print(5 << 1)
print(8 & 5)
print(9 | 5)
print(12 ^ 42)
print(~88)

print(0b1)
print(0b10)
print(0b11)
print(0b100)
print(0b101)
print(0b110)
print(0b111)
print(0b1 + 0b11)
print(0b11 * 0b11)

#Hack
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))
print(bin(6))
print(bin(7))
print(bin(8))
print(bin(9))

def check_bit14(inp):
    mask = 0b1000
    desired = inp & mask
    if desired > 0:
        return "on"
    else:
        return "off"
    
a = 0b10111011
mask = 0b100
desired = a | mask

print(bin(desired))

a_one = 0b11101110
mask = 0b11111111
desired = a_one ^ mask 

print(bin(desired))

#output 
# 0b10001

def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)
