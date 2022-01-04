#!python3
'''
This is a challenging problem!

x06. Determine the factored form
You may use the functions you created in previous assignments
'''

def Factored(a,b,c):
  '''
  input parameters:
  a, b, c: signed float
  These are the coefficients in the quadratic function ax^2 + bx + c = 0
  
  Write the equation in a nicely formatted factored form. This means no fractions
  
  return:
  list : 2 string literals representing the factors.  The order does not matter
  None if the quadratic can not be factored
  '''
  x=None
  g= a*x**2+b*x+c
  if a==1:
    for i in range(c):
      i=i+1
      f=c/i
      v=f+c
      if v==b:
        t=i
        pass
  
  elif a>1:
      n=c*a
      for i in range(n):
        i=i+1
        f=n/i
        v=f+n
        if v==b:
          t=i
          pass
      try: 
        t2=int(t/a)
        s=True

      except:
        s=False
      if s==True:
        x=f"(x+{t2})"
      else:
        for i in range(f):
          i=i+1
          m=f/i
          j=a/i
          try:
            m==int(m) 
            j==int(j)
            continu=True
          except:
            continu=False
          if continu==True:
            x=f"({j}x+{m})"
      try: 
        f2=int(f/a)
        l=True
      except:
        l=False
      if l==True:
        x=f"(x+{f2})"
      else:
        for i in range(f):
          i=i+1
          m=f/i
          j=a/i
          try:
            m==int(m) 
            j==int(j)
            continu=True
          except:
            continu=False
          if continu==True:
            x=f"({j}x+{m})"
          
      pass
  return None

def main():
  assert "(x + 3)" in Factored(1,1,-6) == True
  assert "(x - 2)" in Factored(1,1,-6) == True
  assert "(x + 2)" in Factored(1,7,10) == True
  assert "(2x + 1)" in Factored(2,5,2) == True
  assert "(x + 2)" in Factored(2,5,2) == True
  assert "(3x + 1)" in Factored(6,-7,-3) == True
  assert Factored(1,4,7) == None
  assert Factored(2,4,4) == None
  
if __name__ == "__main__":
  main()
  
