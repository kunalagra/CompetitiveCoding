class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        if l1 is not None:
            while l1.next!=None:
                a.append(l1.val)
                l1=l1.next
            a.append(l1.val)
        b=[]
        if l2 is not None:
            while l2.next!=None:
                b.append(l2.val)
                l2=l2.next
            b.append(l2.val)
        c = sorted(a+b,reverse=True)
        o = ListNode()
        if len(c)!=0:
            for i in range (0,len(c)):
                if i == len(c)-1:
                    o.val=c[i]
                else:
                    temp = ListNode()
                    temp.val =c[i]
                    temp.next = o.next
                    o.next = temp  
            return o
        else:
            o.val=""
            return o