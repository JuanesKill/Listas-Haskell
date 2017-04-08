def SumaDigitosPares(n):
   if(n==0):
        
        return (0)
   else:
        if(n%2==0):
            return n%10+SumaDigitosPares(n/10) 
        else:
            return SumaDigitosPares(n/10)
                            
                
print SumaDigitosPares(21111)
