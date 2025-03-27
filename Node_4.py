# week 6, Session 1, Advanced 1
class Node_4:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# For testing
def print_linked_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def edit_dna_sequence(dna_strand, m, n):
    head = dna_strand
    current = head
    current_pos = 1
    while current:
        for _ in range(m-1):
            if current:
                current = current.next
            else:
                return head
        if not current:
            return head

        last_kept = current
        for _ in range(n):
            if current and current.next:
                current = current.next
            else:
                last_kept.next = None
                return head
            
        if current:
            last_kept.next = current.next
            current = last_kept.next
        else:
            last_kept.next = None
            return head
        
    return head

def cycle_length(protein):
    
    if not protein or not protein.next:
        return []
    
    slow = protein
    fast = protein
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return []
    
    res = []
    current = slow
    while True:
        res.append(current.value)
        current=current.next
        if current==slow:
            break
    
    return res


def split_protein_chain(protein, k):
    if k<=0:
        return []
    if not protein:
        return [None]*k
    
    length = 0
    current= protein
    while current:
        length+=1
        current=current.next

    base_size = length//k
    extra = length % k

    result=[]
    current = protein
    remaining = length

    for i in range(k):
        segment_size = base_size +(1 if i <extra else 0)

        if segment_size==0 or not current:
            result.append(None)
            continue

        segment_head = current
        prev=None

        for _ in range(segment_size):
            prev=current
            current=current.next

        if prev:
            prev.next = None
        result.append(segment_head)
        remaining-=segment_size

    return result

def max_protein_pair_stability(head):
    if not head or not head.next:
        return 0
    
    slow = head
    fast = head
    prev = None

    current = head
    while fast and fast.next:
        prev= slow
        slow = slow.next
        fast = fast.next.next
    
    second_half = slow
    prev.next = None
    prev_node = None
    current=second_half

    while current:
        next_node = current.next
        current.next = prev_node
        prev_node=current
        current= next_node
    
    first_half = head
    second_half = prev_node
    max_sum = 0
    
    while first_half and second_half:
        twin_sum = first_half.value + second_half.value
        max_sum = max(max_sum, twin_sum)
        first_half = first_half.next
        second_half = second_half.next
    
    return max_sum


# pb_1
# dna_strand = Node_4(1, Node_4(2, Node_4(3, Node_4(4, Node_4(5, Node_4(6, Node_4(7, Node_4(8, Node_4(9, Node_4(10, Node_4(11, Node_4(12, Node_4(13)))))))))))))
# print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

# pb_2
# protein_head = Node_4('Ala', Node_4('Gly', Node_4('Leu', Node_4('Val'))))
# protein_head.next.next.next.next = protein_head.next 

# print(cycle_length(protein_head))

# pb_3
# protein1 = Node_4('Ala', Node_4('Gly', Node_4('Leu', Node_4('Val', Node_4('Pro', Node_4('Ser', Node_4('Thr', Node_4('Cys'))))))))
# protein2 = Node_4('Ala', Node_4('Gly', Node_4('Leu', Node_4('Val'))))

# parts = split_protein_chain(protein1, 3)
# for part in parts:
#     print_linked_list(part)

# parts = split_protein_chain(protein2, 5)
# for part in parts:
#     print_linked_list(part)


# pb_4
head1 = Node_4(5, Node_4(4, Node_4(2, Node_4(1))))
head2 = Node_4(4, Node_4(2, Node_4(2, Node_4(3))))

print(max_protein_pair_stability(head1))
print(max_protein_pair_stability(head2))


