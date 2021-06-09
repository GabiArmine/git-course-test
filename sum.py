
class SumNumber:
  def __init__(self, val):
    self.val = val

  def __call__(self, val):
    self.val += val
    return self

  def __str__(self):
      return self.val

a = SumNumber(1)(2)(3)
print('{}'.format(a))
