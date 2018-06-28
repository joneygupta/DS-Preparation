
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def segreGate(head):
    if not head:
        return

    cur = head
    evenList = Node(0)
    dummyEven = evenList
    oddList = Node(0)
    dummyOdd = oddList
    while(cur):
        if (cur.data % 2 == 0):
            evenList.next = Node(cur.data)
            evenList = evenList.next

        else:
            oddList.next = Node(cur.data)
            oddList = oddList.next

        cur = cur.next
    return dummyEven.next, dummyOdd.next


def main():
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(2)
    head1.next.next.next = Node(9)
    head1.next.next.next.next = Node(6)
    head1.next.next.next.next.next = Node(10)


    evenlist, oddlist = segreGate(head1)
    print("EvenList is: ")
    while(evenlist):
        print(evenlist.data)
        evenlist = evenlist.next

    print("OddList is: ")
    while (oddlist):
        print(oddlist.data)
        oddlist = oddlist.next

main()