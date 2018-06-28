class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def mergeLists(head1, head2):
    if not head1.next:
        head1.next = head2
        return head1


    cur1 = head1
    cur2 = head2
    next1 = head1.next
    next2 = head2.next

    while(next1 and next2):

        if (cur2.data > cur1.data) and (cur2.data < next1.data):
            next2 = cur2.next
            cur1.next = cur2
            cur2.next = next1

            cur1 = cur2
            cur2 = next2
        else:
            if next1.next:
                cur1 = cur1.next
                next1 = next1.next

            else:
                next1.next = cur2
                return head1


    return head1



def main():
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(7)
    head1.next.next.next = Node(9)

    head2 = Node(2)
    head2.next = Node(8)
    head2.next.next = Node(10)
    head2.next.next.next = Node(11)

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data < head2.data:
        res = mergeLists(head1, head2)
    else:
        res = mergeLists(head2, head1)

    while(res):
        print(res.data)
        res = res.next




main()