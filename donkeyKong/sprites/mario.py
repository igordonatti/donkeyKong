class Mario():
  def __init__(self):
    self.__posX = 50
    self.__posY = 700

  def plat_move(self, range: int):
    self.__posX += range 

  @property
  def posX(self):
    return self.__posX
  
  @property
  def posY(self):
    return self.__posY
  

