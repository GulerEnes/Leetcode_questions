# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head):
        if not head.next:
            return head.next
        slow, fast = head, head
        while fast.next and fast.next.next and fast.next.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head


s = Solution()

arr = [1, 2, 3, 4, 5]

r = ListNode()
iter = r
for i in arr:
    n = ListNode(val=i)
    iter.next = n
    iter = iter.next

head = s.deleteMiddle(r.next)

result = []
while head:
    result.append(head.val)
    head = head.next
print(result)
