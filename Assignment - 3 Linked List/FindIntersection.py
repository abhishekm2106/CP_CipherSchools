class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

def findIntersection(head1,head2):
    l1 = 0
    copy1 = head1
    while copy1:
        l1+=1
        copy1 = copy1.next
    
    l2 = 0
    copy2 = head2
    while copy2:
        l2+=1
        copy2 = copy2.next
    
    if l1>l2:
        dif = l1-l2
        while dif:
            head1=head1.next
            dif-=1

    elif l2>l1:
        dif = l2-l1
        while dif:
            head2 = head2.next
            dif -=1
    
    while(head2 and head1):
        if head2==head1:
            return head1.val
        head1 = head1.next
        head2 = head2.next
    
    return -1
        


a = ListNode(13)
b = ListNode(15)
a.next = b

l1 = ListNode(5)
l1.next = a



l2 = ListNode(8)
l2.next = ListNode(4)
l2.next.next = a




print(findIntersection(l1,l2))
