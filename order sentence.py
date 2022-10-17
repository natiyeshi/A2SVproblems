class Solution(object):
    def sortSentence(self, s):       
            arr = s.split()
            dict = {}
            for itr in arr:
                ex = list(itr)
                st = ""
                num = ""
                for i in ex:
                    try:
                       int(i)
                       num += str(i)
                    except ValueError:
                        st += str(i)  

                dict[int(num)] = st
            sortedict = collections.OrderedDict(sorted(dict.items()))
            ret = ""
            for i in sortedict:
                ret += sortedict[i] + " "
            ret = ret[:-1]
            return ret
