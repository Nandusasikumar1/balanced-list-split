
l1 = list(range(35))
l2 = list(range(100))

class paginate_base:

    def __init__(self,items,ls1,ls2):
        # page = page
        self.items = items
        self.ls1 = ls1
        self.ls2 = ls2
        self.ls1len = self.ls1.__len__()
        self.ls2len = self.ls2.__len__()
        self.max_page1 = self.max_page(self.items,self.ls1len)
        self.max_page2 = self.max_page(self.items,self.ls2len)
        self.max_page_limit = self.max_page1 if self.max_page1 < self.max_page2 else self.max_page2
        self.maxs1,self.maxe1,self.maxs2,self.maxe2 = self.get_balanced_indices(self.max_page_limit)
        maxdiffe1s1 = self.maxe1 - self.maxs1
        maxdiffe2s2 = self.maxe2 - self.maxs2
        self.add_Factor = maxdiffe1s1-self.items if maxdiffe1s1 > maxdiffe2s2 else maxdiffe2s2 - self.items

        
    def get_indices(self,page,maxpage,llen):

        if 1 <= page < maxpage:
            start = (page-1)*self.items
            end = page * self.items
            
        elif page == maxpage:
        
            start = (maxpage-1)*self.items
            end = llen
        else:
            start,end = 0,0

        
        return start,end
    
        
    def get_balanced_indices(self,page):
        

        self.s1,self.e1 = self.get_indices(page,self.max_page1,self.ls1len)
        self.s2,self.e2 = self.get_indices(page,self.max_page2,self.ls2len)

        return self.balance( self.s1, self.e1, self.s2, self.e2, self.items,page)

    
    # @staticmethod
    def balance(self,s1,e1,s2,e2,items,page):

        
        e1s1diff = e1-s1
        e2s2diff = e2 -s2
        if page <= self.max_page_limit:
          
            e1 = e1+items - e2s2diff
            e2 = e2+items - e1s1diff 

            
        else:
  
            smult = self.max_page_limit+((page-self.max_page_limit-1)*2)
            emult = smult+2
            s,e = (smult*self.items)+self.add_Factor,(emult*self.items)+self.add_Factor
            if e1s1diff == 0 :
                s2,e2 = s,e
            elif e2s2diff == 0 :
                s1,e1 = s,e


        return s1,e1,s2,e2
    
    @staticmethod
    def max_page(items,llen):

        maxpage = llen//items if llen % items == 0  else (llen//items)+1
        return maxpage

# a = paginate_base(4,l2,l1)

# print(a.get_balanced_indices(11))
# print('sdsdsd',a.max_page_limit)
# print(a.add_Factor)

    