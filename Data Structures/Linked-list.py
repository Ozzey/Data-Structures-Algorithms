class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Time Complexity: O(N)
def takeInput() -> ListNode:
    dataList = [int(nums) for nums in input().split() if nums != "-1"]

    head = None
    tail = None

    # Iterate through the list
    for currData in dataList:
        # Creating new node in the linkedlist
        newNode = ListNode(currData)

        # Assigning new node as head if head is none
        if head is None:
            head = newNode
            # Assigning most recent node as the tail
            tail = newNode

        # if head is not none
        else:
            tail.next = newNode
            tail = newNode

    return head


# Time Complexity O(N)
def printLL(head: ListNode) -> None:
    out = ""
    while head is not None:
        out += f'{head.val}'
        out += " -> "
        head = head.next
    print(out[:-4])


# Time Complexity: O(N)
def inputLL(dataList):
    head = None
    tail = None

    # Iterate through the list
    for currData in dataList:
        # Creating new node in the linkedlist
        newNode = ListNode(currData)

        # Assigning new node as head if head is none
        if head is None:
            head = newNode
            # Assigning most recent node as the tail
            tail = newNode

        # if head is not none
        else:
            tail.next = newNode
            tail = newNode
    return head


def copy(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return inputLL(arr)


# Time Complexity : O(N)
def lengthLL(head: ListNode) -> int:
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length


# Time Complexity : O(i)
def getNode(head: ListNode, index: int) -> ListNode:
    ind = 0
    while head is not None:
        if ind == index:
            return head
        else:
            ind += 1
            head = head.next
    raise Exception("Index of out range")


# Time Complexity : O(1)
def insertNodeAtHead(head: ListNode, data: int) -> ListNode:
    newNode = ListNode(data)
    if head:
        newNode.next = head
    return newNode


# Time Complexity : O(n)
def insert(head, index, data):
    # Check if the index is out of range (negative or greater than the length of the linked list)
    if index < 0 or index > lengthLL(head):
        return Exception("Index of out range")

    # Store a reference to the original head of the linked list
    org_head = head

    # If the index is 0, insert the node at the head of the list
    if index == 0:
        return insertNodeAtHead(head, data)

    else:
        ind = 0  # Initialize an index counter
        newNode = ListNode(data)  # Create a new node with the given data

        # Traverse the linked list
        while head is not None:
            # Check if the current index is one less than the desired index
            if ind == index - 1:
                curr = head.next  # Save the reference to the next node
                head.next = newNode  # Update the next pointer of the current node to point to the new node
                newNode.next = curr  # Update the next pointer of the new node to point to the next node
                return org_head  # Return the original head of the linked list

            else:
                head = head.next  # Move to the next node in the linked list
                ind += 1  # Increment the index counter


# Time Complexity : O(N)
def insertRec(head, index, data):
    if index < 0:
        raise ValueError("Index out of range")

    if index == 0:
        newNode = ListNode(data)
        newNode.next = head
        return newNode

    if head is None:
        raise ValueError("Index out of range")

    tempHead = insertRec(head.next, index - 1, data)
    head.next = tempHead
    return head


# Time Complexity: O(N)
def deleteNode(head, index):
    idx = 0
    prev = None
    curr = head
    next = head.next

    if index < 0:
        raise Exception("Index of out range")

    # 1 -> 2 -> 3 -> 4
    while head is not None:
        if index == 0:
            return next
        elif idx == index:
            prev.next = next
            return curr
        else:
            idx += 1
            prev = head
            head = head.next
            try :
                next = head.next
            except Exception as e:
                raise ValueError("Index out of range")


# Time Complexity: O(N)
def deleteRec(head,index):

    if index < 0:
        raise ValueError("Index out of range")

    if index == 0:
        return head.next
    tempNode = deleteNode(head.next, index - 1)

    if head is None:
        return ValueError("Index out of range")

    head.next = tempNode
    return head


# Time Complexity: O(N)
def reverseLL(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    current = head
    prev = None

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


# Time Complexity: O(N)
def deleteElement(head, value):
    prev = None
    first = head

    while head and head.val == value:
        head = head.next
        first = head

    while head:
        if head.val == value:
            prev.next = head.next
            head = head.next
        else:
            prev = head
            head = head.next

    return first
