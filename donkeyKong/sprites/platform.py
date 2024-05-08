class Platform: 
  def __init__(self, x: int, y: int):
    self.__posX = x
    self.__posY = y

  @property
  def posX(self):
    return self.__posX
  
  @property
  def posY(self):
    return self.__posY