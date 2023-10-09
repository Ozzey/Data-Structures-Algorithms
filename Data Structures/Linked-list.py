class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Time Complexity O(N)
def printLL(head : int) -> None:
    while head is not None:
        print(head.data)
        head = head.next

# Time Complexity: O(N)
def takeInput() -> Node:
    dataList = [int(nums) for nums in input().split() if nums != "-1"]

    head = None
    tail = None

    # Iterate through the list
    for currData in dataList:
        # Creating new node in the linkedlist
        newNode = Node(currData)

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


# Time Complexity : O(N)
def lengthLL(head : int) -> int:
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length


# Time Complexity : O(i)
def getNode(head : int, index : int) -> Node:
    ind = 0
    while head is not None:
        if ind == index:
            return head
        else:
            ind += 1
            head = head.next
    return Exception("Index of out range")


# Time Complexity : O(1)
def insertNodeAtHead(head : int ,data : int) -> Node:
    newNode = Node(data)
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
        newNode = Node(data)  # Create a new node with the given data

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


# head = takeInput()
# head = insert(head,5,100)
