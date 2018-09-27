'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        tmp = listNode
        ans = []
        while tmp:
            ans.append(tmp.val)
            tmp = tmp.next
        return ans[::-1]

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(Solution().printListFromTailToHead(head))
