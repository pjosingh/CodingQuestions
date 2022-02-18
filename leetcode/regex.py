import re

class Solution(object):
    def run(self, regex, target):
        # m = re.search(regex, target)
        # return m.group(0)
        prog = re.compile(regex)
        return prog.match(target)




sol = Solution()
print(sol.run('[0-9A-Z]{9}', 'CG21033556'))
print(sol.run('[0-9A-Z]{9}', '20407212869'))
print(sol.run('[0-9A-Z]{9}', '/NT1115ZQXDJ'))
print(sol.run('[0-9A-Z]{9}', '386367183'))
