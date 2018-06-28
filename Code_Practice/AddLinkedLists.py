
class Add:

    def __init__(self,val):
        self.val = val
        self.next = None

    def addLinkedList(self,list1,list2):
        carry  = 0
        dummy = Add(0)
        head = dummy
        while(list1 or list2):
            val = carry
            if list1:
                val += list1.val
                list1= list1.next
            if list2:
                val += list2.val
                list2 = list2.next

            carry,val = divmod(val,10)
            head.next = Add(val)
            head = head.next
        if carry == 1:
            head.next = Add(1)
        return dummy.next

    def addLinkedList2(self,list1,list2):
        stack1 = []
        stack2 = []
        carry = 0
        dummy = Add(0)
        head = dummy
        prev = None
        while(list1):
            stack1.append(list1.val)
            list1 = list1.next

        while (list2):
            stack2.append(list2.val)
            list2 = list2.next

        while(stack1 or stack2):
            val = carry
            if stack1:
                val += stack1.pop()
            if stack2:
                val += stack2.pop()

            carry, val = divmod(val, 10)
            head.next = Add(val)
            head = head.next

            current = Add(val)
            current.next = prev
            prev = current


        if carry == 1:
            current = Add(1)
            current.next = prev
        return current


    def reverseInBlock(self,head,k):
        count = 0
        curr = head
        prev  = next = None
        while(curr and count < k ):

            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if next is not None:
            head.next = self.reverseInBlock(next,k)
        return prev

    def detectAndRemoveLoop(self,list1):
        slow_ptr = list1
        fast_ptr = list1

        while(slow_ptr and fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                slow_ptr = list1
                while (slow_ptr.next != fast_ptr.next):
                    slow_ptr = slow_ptr.next
                    fast_ptr = fast_ptr.next
                fast_ptr.next = None  # Remove loop
                return 1
        return 0

    def createMapping(self,l1,l2):
        pair = {}
        while(l1 or l2):
            if l1:
                if l1.val not in pair:
                    pair[l1.val] = 1
                else:
                    pair[l1.val] += 1
                l1 = l1.next
            if l2:
                if l2.val not in pair:
                    pair[l2.val] = 1
                else:
                    pair[l2.val] += 1
                l2 = l2.next
        return pair

    def union(self, pair):
        dummy = Add(0)
        head = dummy
        for k,v in pair.items():
            head.next = Add(k)
            head = head.next
        return dummy.next

    def intersection(self,pair):
        dummy = Add(0)
        head = dummy
        for k, v in pair.items():
            if v == 2:
                head.next = Add(k)
                head = head.next
        return dummy.next

    def mergeLinkedlistOnAlternatePos(self,h1,h2):
        head = h1
        while(h1 and h2):
            h1Next = h1.next
            h2Next = h2.next

            h2.next = h1Next
            h1.next = h2

            h1 = h1Next
            h2 = h2Next
        return head, h2

def main():
    list1 = Add(5)
    list1.next = Add(6)
    list1.next.next = Add(3)

    list1.next.next.next = Add(1)
    list1.next.next.next.next = Add(6)
    list1.next.next.next.next.next = Add(7)
    list1.next.next.next.next.next.next = Add(2)

    list1.next.next.next.next.next.next.next = list1.next.next.next


    list2 = Add(8)
    list2.next = Add(4)
    list2.next.next = Add(2)

    #final = list1.addLinkedList(list1,list2)
    #result = list1.addLinkedList2(list1, list2)
    #printList(list1)
    #result = list1.reverseInBlock(list1,3)
    print('----------------------------------------------')
    #printList(result)

    #list1.detectAndRemoveLoop(list1)

    l1 = Add(1)
    l1.next = Add(2)
    l1.next.next = Add(3)
    l1.next.next.next = Add(4)
    l1.next.next.next.next = Add(5)

    l2 = Add(1)
    l2.next = Add(3)
    l2.next.next = Add(5)
    l2.next.next.next = Add(6)

    #pair = list1.createMapping(l1,l2)
    #res1 = list1.union(pair)
    #printList(res1)
    #res2 = list1.intersection(pair)
    print('------------------------------------')
    #printList(res2)

    h1 = Add(1)
    h1.next = Add(2)
    h1.next.next = Add(3)
    h1.next.next.next = Add(9)

    h2 = Add(4)
    h2.next = Add(5)
    h2.next.next = Add(6)
    h2.next.next.next = Add(7)
    h2.next.next.next.next = Add(8)
    h2.next.next.next.next.next = Add(10)

    #result1,result2 = list1.mergeLinkedlistOnAlternatePos(h1,h2)
    #printList(result1)
    print('------------------------------------')
    #printList(result2)

def printList(list):
    while(list):
        print (list.val)
        list = list.next
main()