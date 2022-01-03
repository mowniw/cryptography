def main():
  #S = bin(79)
  S=100111
  A = ((((S >> 7)^ (S >> 6) ^ (S >> 3) ^ (S >> 2) ^ S) & 0b000001) << 7) | (S >> 1)
  B = ((((S >> 5) ^ (S >> 3) ^ (S >> 2) ^ S) & 0b000001) << 7) | (S >> 1)
  print(bin(A))
  print(A)
  print(bin(B))
  print(B)


main()
