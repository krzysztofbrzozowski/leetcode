class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = ''.join(l1[::-1])
        l2 = ''.join(l2[::-1])

        out = int(l1) + int(l2)
        out = [num for num in out][::-1]