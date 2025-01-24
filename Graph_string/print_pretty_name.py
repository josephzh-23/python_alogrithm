
'''

// Alice
//   Bob
//     Emp3
//       Emp4
//         Emp5
//       Emp6
//   Emp7
'''
import collections


class Employee:
    def __init__(self, id, managerId, name):
        self.name = name
        self.managerId = managerId
        self.id = id


employees =  [Employee(8, 8, "Alice" ), Employee(2, 8, "Bob" ), Employee(3, 2, "Emp3" ), Employee(4, 3, "Emp4" ), Employee(5, 4, "Emp5" ), Employee(6, 3, "Emp6" ), Employee(7, 8, "Emp7" )]


def answers(employees):
    graph = collections.defaultdict(set)
    s = set()
    # this will hold the manager position here
    top = None
    for emp in employees:
        if emp.managerId == emp.id:

            top = emp
        graph[emp.managerId].add(emp)

    def dfs(graph, manager, level=0):
        if manager.id in s:
            return
        print(' ' * level, manager.name)
        for e in graph[manager.id]:
            s.add(manager.id)
            dfs(graph, e, level + 1)
    dfs(graph, top)
    '''
    '''
answers(employees)

