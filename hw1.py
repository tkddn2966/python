def get_radius(prompt):
 r = int(input(prompt))
 return r

def get_circle_area(n):
  print("반지름",n,"인 원의 넓이 =","3.14 x",n,"x",n,"=",n*n*3.14)


result = get_radius("넓이를 구하고자 하는 반지름의 길이는 ? ")
get_circle_area(result)
