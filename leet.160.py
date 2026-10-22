
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def print_list(head):
    res = []
    cur = head
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print(" -> ".join(res))

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA=headA
        pB=headB
        while pA!=pB:
            pA=pA.next if pA else headB
            pB=pB.next if pB else headA
        return pA
if __name__ == "__main__":
    listA = build_list([4, 1, 8, 4, 5])
    listB = build_list([5, 6, 1, 8, 4,5])
    

    intersection = ListNode(8)
    intersection.next = ListNode(4)
    intersection.next.next = ListNode(5)
    listA.next.next = intersection
    listB.next.next = intersection
    
    print("List A:")
    print_list(listA)
    print("List B:")
    print_list(listB)
    
    solution = Solution()
    result = solution.getIntersectionNode(listA, listB)
    
  
    if result:
        print(f"Intersection at node with value: {result.val}")
    else:
        print("No intersection.")
