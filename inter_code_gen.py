ops = ['*','/','+','-','(',')']
pri = {'*':2,'/':2,'+':1,'-':1}

def gen_postfix(exp):
  stack=[]
  output=''
  
  for c in exp:
    if c not in ops:
      output+=c
    elif c == '(':
      stack.append(c)
    elif c == ')':
      while stack and stack[-1]!='(':
        output+=stack.pop()
      stack.pop()
    else:
      while stack and stack[-1]!='(' and pri[c]<=pri[stack[-1]]:
        output += stack.pop()
      stack.append(c)
      
  while stack: output += stack.pop()
    
  return output
  
def gen_code(pos):
  stack=[]
  t=1
  for c in pos:
    if c not in ops:
      stack.append(c)
    else:
      print(f't{t} = {stack.pop(-2)} {c} {stack.pop()}')
      stack.append(f't{t}')
      t+=1
      
exp = "a=3+4*(8-7*(c-b)+2)"
pos = gen_postfix(exp)
print(f'Postfix = {pos}')
gen_code(pos)
