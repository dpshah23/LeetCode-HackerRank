class Solution(object):
    def fibrecur(self,n):
            if n <= 1:
              return n
            else:
              return(self.fibrecur(n-1) + self.fibrecur(n-2))
    def fib(self, n):
        return self.fibrecur(n)