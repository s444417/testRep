from Api.Related import Related

class RelatedCollection:
    def __init__(self):
        self.relatedItems = []

    def toString(self):
        result = ' = { ' +  ( self.relatedItems[0].toString() if (0 < len( self.relatedItems)) else '')
        index = 1
        while index < len(self.relatedItems):
            result += ', ' +  self.relatedItems[index].toString()
            index += 1
        result += ' }'    
        return result       
 
    def canAdd(self, left, right):
        result = True
        for item in self.relatedItems:
            result = item.left != left or item.right != right
            if(not result): break
        return result

    def doAdd(self, left, right):
        self.relatedItems.append(Related(left, right))

    def __add__(self, item):
        self.relatedItems.append(item)

    def getComposition(self, other):
        result = RelatedCollection()
        for itemR in self.relatedItems:
            for itemS in other.relatedItems:
                if(itemR.right == itemS.left):
                    result.doAdd(itemR.left, itemS.right)
        return result
    
    def __mul__(self, other):
        return self.getComposition(other)
        
    def clear(self):
        self.relatedItems.clear()
