class BidirectNode:
    def __init__(self, newitem, prevNode = "bidirect", nextNode = "bidirect"):
        self.item = {
            'marketplace': None, 'customer_id': None, 'review_id': None, 'product_id':None,
       'product_parent':None, 'product_title':None, 'product_category':None, 'star_rating':None,
       'helpful_votes':None, 'total_votes':None, 'vine':None, 'verified_purchase':None,
       'review_headline':None, 'review_body':None, 'review_date':None
        }
        i = 0
        for k in self.item.keys():
            self.item[k] = newitem[i]
            i += 1
        self.prev = prevNode
        self.next = nextNode