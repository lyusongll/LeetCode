class Solution:
	def removeElement(self, head, val):
		dummy = ListNode(0)
		dummy.next = head
		pre, cur = dummy, head
		while cur:
			if cur.val == val:
				pre.next = cur.next
			else:
				pre = cur
			cur = cur.next
		return dummy.next