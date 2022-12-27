import textwrap

def wrap(string, max_width):
    c = 0
    st = ""
    for itr in (string):
        st += itr
        c += 1
        if c == max_width:
            c = 0
            st += "\n"   
    
    return st

if __name__ == '__main__':
