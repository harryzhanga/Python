def radixsort(lst):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
  maxInt = max(lst)
  while placement > maxInt:
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]

    # split lst between lists
    for i in lst:
      tmp = int((i / placement) % RADIX)
      buckets[tmp].append(i)

    # empty lists into lst array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        lst[a] = i
        a += 1

    # move to next
    placement *= RADIX
