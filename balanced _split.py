
import time


class paginate_base:

    def __init__(self,items,ls1,ls2):
        # page = page
        self.items = items
        self.total_items = 2*self.items
        if self.items < 1:
            raise Exception('page shoud be greater than or equal to one')
        self.ls1 = ls1
        self.ls2 = ls2
        self.ls1len = self.ls1.__len__()
        self.ls2len = self.ls2.__len__()
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
        
        self.s1,self.e1 = self.get_indices(page,self.max_page1,self.ls1len)
        self.s2,self.e2 = self.get_indices(page,self.max_page2,self.ls2len)

        return self.balance( self.s1, self.e1, self.s2, self.e2, self.items,page)

    def balance(self,s1,e1,s2,e2,items,page):

        e1s1diff = e1-s1
        e2s2diff = e2 -s2
        if page <= self.max_page_limit:

            e1 = e1+items - e2s2diff
            e2 = e2+items - e1s1diff 
        else:
            mul_factor = page - self.max_page_limit if self.max_page_limit % 2 == 0 else page - self.max_page_limit -1

  
            if self.get_indices(page,self.max_page1,self.ls1len) == (0,0) :
                s2 = self.maxe2 + self.total_items*mul_factor
                e2 = s2 + self.total_items

            elif self.get_indices(page,self.max_page2,self.ls2len) == (0,0):
                s1 = self.maxe1 + self.total_items*mul_factor
                e1 = s1 + self.total_items

     
        return s1,e1,s2,e2
    
    @staticmethod
    def max_page(items,llen):


        maxpage = llen//items if llen % items == 0  else (llen//items)+1

        return maxpage

l1 = list(range(80))
l2 = list(range(1000))

# start = time.time()
a = paginate_base(74,l2,l1)
# end = time.time()

# print((end-start))

print(a.get_balanced_indices(2),a.max_page_limit)



# print(a.__dict__)
# print(a.max_page_limit)
# print(a.add_Factor)

# [1,2,3,4,,,5,6,7,8],[1,2,3,4,,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]