class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def reverseList(linkedList):
    prev = None
    root = after = linkedList
    while(after):
        after = after.next
        root.next = prev
        prev = root
        root = after
    
    return prev

l1 = ListNode(8)
l1.next = ListNode(4)
l1.next.next = ListNode(2)

final = reverseList(l1)
while(final):
    print(final.val,end=' -> ')
    final = final.next
print(None)