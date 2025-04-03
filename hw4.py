def rep_char(c,n):
    return(c*n)
    
def draw_line_string(msg):
   
    msg1 = f'hello {msg}'
    msg2 = 'Welcome to Seoul'
    
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    line = rep_char('-', nstr)

    print(line)
    print(msg1 + '\n' + msg2)
    print(line)


char = input('input his/her name:')

draw_line_string(char)


