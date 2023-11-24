class Point :
  def __init__(self, abscisse=0, ordonne=0) :
    self.__abscisse = abscisse
    self.__ordonne = ordonne

  def get_abscisse():
    return self._abscisse

  def set_abscisse(self,x) :
    self._abscisse = x

  def get_ordonne():
    return self._ordonne

  def set_abscisse(self,y) :
    self._ordonne = y

  def Distance (self) :
    d = 1/2 * ((get_abscisse() - self.__abscisse) ** 2 + (get_ordonne() - self.__ordonnee)**2)
    return d

  def Norm (self) :
    n = 1/2 (self__abscisse ** 2 + self.__ordonnee**2)
    return n
  


  
  
  
