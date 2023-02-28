class Solution: 
    
    def decodeString(self, s,counter = 0,st = [],result = "") -> str:
        # print(result)
        if counter >= len(s):
            # ans = "".join(result)
            # result = []
            return  result
        if s[counter].isdigit():
            c = counter
            while counter < len(s) and s[counter].isdigit():
                counter += 1
            st.append([int(s[c:counter])])
            return self.decodeString(s,counter + 1,st,result)
        if s[counter] == "]":
            print(st)
            temp = st.pop()
            temp = temp[0] * temp[1:]
            
            if not st:
                result += "".join(temp)
            else:
                st[-1].extend(temp)
            return  self.decodeString(s,counter + 1,st,result)
        if st:
            st[-1].append(s[counter])
        else:
            result += (s[counter])
        return self.decodeString(s,counter + 1,st,result)