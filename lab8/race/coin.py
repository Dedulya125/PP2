import settings
import obstacle

class Coin(obstacle.Obstacle):
  def __init__(self):
    super().__init__(20, 1, "/Users/Nurbek/Desktop/pp2/lab8/race/images/coin.png", settings.SPEED)