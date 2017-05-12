import random

class Propgation:
  def Identy(iden):
    return iden
  def TanH(tan):
    e = 2.71828
    return (2 / 1+e**(-2 * tan)) -1
  def Binary(bin):
    if bin < 0:
      return 0
    elif bin >= 0:
      return 1
  def Logistic(sig):
    e = 2.71828
    return 1 / 1 + e**-sig
  def Relu(rel):
    if rel < 0:
      return 0
    elif rel >= 0:
      return rel
      
class NN:
  def GetWeights(type, howmany):
    a = []
    if type == 'zero':
      for i in range(0, howmany):
        a.append(0)
      return a
    elif type == 'rand':
      for i in range(0, howmany):
        a.append(random.random())
      return a
  def Proc(arr1, arr2, b):
    procarr = []
    for i in range(0, len(arr1)):
      procarr.append(arr1[i] * arr2[i])
    return sum(procarr) + b
    
