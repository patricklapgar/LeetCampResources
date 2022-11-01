from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if (not head) or (not head.next):
            return head

        next = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return next

    def print_list(self, head: Optional[ListNode]):
        # Print val of each node (with a next arrow)
        while head.next:
            print(str(head.val) + "->", end="")
            head = head.next  # increment head
        # Prints the very last node (that does not have a next)
        print(head.val)


if __name__ == "__main__":
    # Initialize nodes
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    # Initialize solution object
    s = Solution()
    print("Original Linked List: ", end="")
    s.print_list(head)

    # Call reverseList method
    reverse_head = s.reverseList(head)
    print("Reversed Linked List: ", end="")
    s.print_list(reverse_head)
