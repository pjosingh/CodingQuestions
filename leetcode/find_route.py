from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:

        reverse_mapping = defaultdict(list)
        for i in range(len(routes)):

            for el in routes[i]:
                reverse_mapping[el].append(i)

    
    
        print(reverse_mapping)
        path = []
        self.get_path(reverse_mapping, target, source, routes, path)

    def get_path(self, mapping, dest, current, routes, path):

        print(f'call {mapping} {dest} {current}')

        if current == dest:
            return

        for el in mapping[current]:
            path.append(el)
            self.get_path(mapping, dest, )
        return 2


assert Solution().numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6) == 2

