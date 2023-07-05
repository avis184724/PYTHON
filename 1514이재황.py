#스택에 원소 추가
stack = [1,2,3]
stack.append(4)

stack # [1,2,3,4]


#스택에 원소 제거
stack = [1,2,3]
top = stack.pop()

print(top) # 3
stack # [1,2]


#스택의 top 가져오기
stack = [1,2,3]
top = stack[-1]

top # 3