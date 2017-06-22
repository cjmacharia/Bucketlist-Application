
items=[]

class Item():


    def __init__(self,item=None):
        self.item=item
    def create(self,item):
        if item !='':
            data={}
            data['item']=item
            items.append(data)
            return 1
        else:
            return 2    
