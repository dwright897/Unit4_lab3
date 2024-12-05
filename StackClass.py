# Dalton Wright
# Array Stack
#12/5/24

class ArrayStack:
  def __init__(self):
    """initilize and empty stack"""
    self.__stack =[]
    self.__size = 0

  
  def top(self):
    """Return top of stack without modifying stack"""
    if self.__size == 0:
      raise IndexError("top from an empty stack")
    return self.__stack[-1]
  
  def push(self, element):
    """Adds a new element to the stack"""
    self.__stack.append(element)
    self.__size +=1

  def pop(self):
    """Remove top element and modify stack"""
    if self.__size == 0:
      raise IndexError("pop from an empty stack")
    self.__size -=1
    return self.__stack.pop()

  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out

  def __len__(self):
    """return size"""
    return self.__size

  def __is_empty(self):
    """Returns Boolean"""
    if self.size ==0:
      return True
    else: 
      return False
    