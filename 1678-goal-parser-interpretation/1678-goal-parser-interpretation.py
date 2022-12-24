class Solution(object):
    def interpret(self, command):
        
        ret = ""
        itr = 0
        command = list(command)
        while itr < len(command):
            if command[itr] == "G":
                ret += "G"
                itr += 1
            elif command[itr] == "(":
                if command[itr + 1] == ")":
                    ret += "o"
                    itr += 2
                else:
                    ret += "al"
                    itr += 4
        return ret
        
        """
        :type command: str
        :rtype: str
        """
        