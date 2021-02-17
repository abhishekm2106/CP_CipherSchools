class ListNode:
    def __init__(self,val=0,next = None) -> None:
        self.val = val
        self.next = next


def merge(l1,l2):
    if l1.val<l2.val:
        primary = ret =  l1
        secondary = l2
    else:
        primary = ret = l2
        secondary = l1
    
    while(primary.next and secondary):
        if primary.next.val<=secondary.val:
            primary=primary.next
        else:
            temp = secondary
            secondary = secondary.next
            temp.next = primary.next
            primary.next = temp
    
    if secondary:
        primary.next = secondary

        
    return ret
        





l1 = ListNode(2)
l1.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(5)
l2.next.next = ListNode(7)

final = merge(l1,l2)
while(final):
    print(final.val,end='->')
    final = final.next
print(None)