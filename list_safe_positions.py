class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_circular_list(n):
    if n == 0:
        return None
    head = Node(1)
    current = head
    for i in range(2, n + 1):
        current.next = Node(i)
        current = current.next
    current.next = head 
    return head

def get_safe_positions(total, start_m, step_k, to_throw):
    head = create_circular_list(total)
    current = head
    # мы ищем тюк, с которого начинается выбрасывание
    while current.value != start_m:
        current = current.next
    prev = head
    while prev.next != current:
        prev = prev.next
    thrown = []
    while len(thrown) < to_throw:
        thrown.append(current.value)
        prev.next = current.next
        current = current.next
        for i in range(step_k - 1):
            prev = current
            current = current.next
    all_positions = set(range(1, total + 1))
    safe = sorted(all_positions - set(thrown))
    return safe