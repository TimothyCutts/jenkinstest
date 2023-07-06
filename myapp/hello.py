import fire

def hello(name="World"):
  return "Hello %s!" % name

def add(num1, num2):
  total = num1+num2
  return total

if __name__ == '__main__':
  fire.Fire(hello)
  fire.Fire(add)