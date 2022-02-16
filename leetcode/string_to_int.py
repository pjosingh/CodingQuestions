

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """


        mul = 1
        final_val = 0

        map = {}
        map['0'] = 0
        map['1'] = 1
        map['2'] = 2
        map['3'] = 3
        map['4'] = 4
        map['5'] = 5
        map['6'] = 6
        map['7'] = 7
        map['8'] = 8
        map['9'] = 9
        
        to_convert = ""
        neg = 0
        pos = 0
        number_started = False
        for ch in s:
            if ch == ' ':
                if number_started:
                    break
                if neg != 0 or pos != 0:
                    break
                if to_convert == "":
                    continue
                break

            if ch == '-':
                if number_started:
                    break

                if to_convert == "":
                    neg += 1
                continue

            if ch == "+":
                
                if number_started:
                    break
                pos += 1
                
                continue

            if ch not in map:
                break
            to_convert += ch
            number_started = True

        if neg != 0 and pos != 0:
            return 0
        
        if neg >1 or pos > 1:
            return 0
        for ch in reversed(to_convert):

            val = map[ch]
            final_val += val * mul
            mul = mul*10
            
        
        #print(to_convert, final_val)
        if final_val > 2147483647 and not neg:
            final_val = 2147483647
        elif final_val > 2147483647 and neg:
            final_val = -2147483648
        elif neg:
            final_val = -final_val
        
        print(final_val)
        return final_val
        
        

sol = Solution() 
assert sol.myAtoi("42") == 42
assert sol.myAtoi("    42") == 42
assert sol.myAtoi("42   ") == 42
assert sol.myAtoi("42   abc") == 42
assert sol.myAtoi("4193 with words") == 4193
assert sol.myAtoi("-42") == -42
assert sol.myAtoi("   - 42") == 0
assert sol.myAtoi("  -42  ") == -42
assert sol.myAtoi("-91283472332") == -2147483648
assert sol.myAtoi("42333333333333333") == 2147483647
assert sol.myAtoi("2147483647") == 2147483647
assert sol.myAtoi("-2147483647") == -2147483647
assert sol.myAtoi("0") == 0
assert sol.myAtoi("-1") == -1
assert sol.myAtoi("+1") == 1
assert sol.myAtoi("+-42") == 0
assert sol.myAtoi("-+42") == 0
assert sol.myAtoi("+-12") == 0
assert sol.myAtoi("++-12") == 0
assert sol.myAtoi("++- 12") == 0
assert sol.myAtoi("00000-42a1234") == 0
assert sol.myAtoi("-13+8") == -13
assert sol.myAtoi("++1") == 0




