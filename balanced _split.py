class paginate_base:

    def __init__(self,items,ls1,ls2):
        # page = page
        self.items = items
        self.total_items = 2*self.items
        if self.items < 1:
            raise Exception('items shoud be greater than or equal to one')
        self.ls1 = ls1
        self.ls2 = ls2
        self.ls1len = len(self.ls1)
        self.ls2len = len(self.ls2)
        self.max_page1 = self.max_page(self.items,self.ls1len)
        self.max_page2 = self.max_page(self.items,self.ls2len)
        self.max_page_limit = self.max_page1 if self.max_page1 < self.max_page2 else self.max_page2
        self.maxs1,self.maxe1,self.maxs2,self.maxe2 = self.get_balanced_indices(self.max_page_limit)


        
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
        if page < 1:
            raise Exception('Page should be greater than or equal to one.')
        
        self.s1,self.e1 = self.get_indices(page,self.max_page1,self.ls1len)
        self.s2,self.e2 = self.get_indices(page,self.max_page2,self.ls2len)

        return self.balance( self.s1, self.e1, self.s2, self.e2, self.items,page)

    def balance(self,s1,e1,s2,e2,items,page):

        e1s1diff = e1 - s1
        e2s2diff = e2 - s2
        if page <= self.max_page_limit:

            e1 = e1+items - e2s2diff 
            e2 = e2+items - e1s1diff
        else:
            mul_factor = page - self.max_page_limit - 1
            l1index = self.get_indices(page,self.max_page1,self.ls1len)
            l2index = self.get_indices(page,self.max_page2,self.ls2len)

            if  l1index == (0,0) and l2index != (0,0):

                s2 = self.maxe2+self.total_items*mul_factor
                e2 = s2+self.total_items

            elif l2index == (0,0) and l1index != (0,0):
             
                s1 = self.maxe1+self.total_items*mul_factor
                e1 = s1+self.total_items

     
        return s1,e1,s2,e2
    
    @staticmethod
    def max_page(items,llen):


        maxpage = llen//items if llen % items == 0  else (llen//items)+1

        return maxpage

