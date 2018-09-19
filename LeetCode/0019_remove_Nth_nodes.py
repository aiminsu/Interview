'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # get the size of the linked list
        tmp, length = head, 0
        while tmp:
            tmp = tmp.next
            length += 1
        # if only one element, return
        if length<=1:
            return None

        # compute which node to delete
        nodeToDelete = length-n+1
        print('node to delete:', nodeToDelete)
        if nodeToDelete == 1:
            return head.next

        # traverse till that node
        tmp, idx = head, 1
        while idx<nodeToDelete-1:
            tmp = tmp.next
            idx += 1
        tmp.next = tmp.next.next
        return head

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, val):
        # append a node to the end.
        node = ListNode(val)
        # if the linked list is None
        if not self.head:
            self.head = node
            return

        # if not None, traverse the linked list till the last node
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def printnodes(self):
        # print each node in the linked list.
        tmp = self.head
        while tmp:
            print(tmp.val)
            tmp = tmp.next


if __name__ == '__main__':
    nums = [1, 2]
    ll = LinkedList()
    for val in nums:
        ll.append(val)
    print('Nodes in linked list')
    ll.printnodes()

    solution = Solution()
    print('After remove Nth node from the end')
    res = solution.removeNthFromEnd(ll.head, 2)
    LinkedList(res).printnodes()
