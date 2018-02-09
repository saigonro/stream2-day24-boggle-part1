def sumlist(l):
   if l == []:
       return 0
   else:
       return l[0] + sumlist(l[1:])

def maxinlist(l):
   if len(l) == 1:
       return l[0]
   else:
       firstinthis = l[0]
       maxinrest = maxinlist(l[1:])
       return firstinthis if firstinthis > maxinrest else maxinrest