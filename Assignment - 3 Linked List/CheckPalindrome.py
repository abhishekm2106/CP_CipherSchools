class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

def traverse(linkedList):
    if linkedList==None:
        print(None)
        return
    print(linkedList.val,end='-->')
    traverse(linkedList.next)

def reverse(linkedList):
    if linkedList.next == None:
        return linkedList
    
    root = linkedList
    prev = None
    while(linkedList):
        temp=linkedList.next
        linkedList.next = prev
        prev = linkedList
        linkedList = temp
    
    return prev

def findMid(linkedList):
    slow = linkedList
    fast = linkedList
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    
    return slow




def checkPalindrome(linkedList):
    second = findMid(linkedList)
    first = linkedList
    prev = ListNode()
    prev.next = linkedList
    while True:
        if linkedList==second:
            prev.next = None
            break
        linkedList=linkedList.next
        prev = prev.next
    
    
    second = reverse(second)
    traverse(first)
    traverse(second)
    while(first and second):
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True


l1 = ListNode(7)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(7)



print(checkPalindrome(l1))
    


