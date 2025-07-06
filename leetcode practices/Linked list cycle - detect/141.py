class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Keep moving fast and slow until fast reaches the end
        while fast and fast.next:
            slow = slow.next          # 1 step
            fast = fast.next.next     # 2 steps

            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle


# Want to Test It?

# Create a cycle for testing
# def createCycleList(values, pos):
#     nodes = [ListNode(val) for val in values]
#     for i in range(len(values) - 1):
#         nodes[i].next = nodes[i+1]
#     if pos != -1:
#         nodes[-1].next = nodes[pos]
#     return nodes[0]

