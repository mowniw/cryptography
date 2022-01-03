def main():
  S = 79
  S = ((((S >> 7)^ (S >> 6) ^ (S >> 5) ^ (S >> 2) ^ (S >> 1)^S) & 0b000001) << 7) | (S >> 1)
  print(bin(S))
  print(S)
  
def main2():
  S = 79
  S = ((((S >> 7) ^ (S >> 4) ^ (S >> 2) ^ S) & 0b00000001) << 7) | (S >> 1)
  print(bin(S))
  print(S)

main()

main2()





#print(int(10001011,10))
