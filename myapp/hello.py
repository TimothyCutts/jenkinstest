import fire

def hello(name="World"):
  return "Hello %s!" % name

def add(num1, num2):
  total = num1+num2
  return total

if __name__ == '__main__':
  num1 = 1
  num2 = 4
  fire.Fire(hello)
  fire.Fire(add)