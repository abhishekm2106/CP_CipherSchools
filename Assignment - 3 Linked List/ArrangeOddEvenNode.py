class ListNode:
    def __init__(self,val=0,next = None) -> None:
        self.val = val
        self.next = next

def rearrangeEvenOdd(head):
    #code here
    x = head
    if head==None:
        return head
    
    if head.next==None:
        return head
    
    if head.next.next==None:
        return head
    
    odd = head
    even = head.next
    pointer = head.next.next
    oddflag = True
    while pointer:
        tempPointer = pointer
        pointer = pointer.next
        if oddflag:
            temp = odd.next
            odd.next = tempPointer
            odd.next.next = temp
            odd = odd.next
            even.next = pointer
            even = even.next
        oddflag = False if oddflag else True
        
    return x

l1 = ListNode(5)
l1.next = ListNode(6)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(1)

final = rearrangeEvenOdd(l1)
while(final):
    print(final.val,end='->')
    final = final.next
print(None)