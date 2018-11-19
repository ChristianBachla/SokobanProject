import sys
import os
import SokoMap

if __name__ == '__main__':

    filename = "test1.txt"

    smap = SokoMap.SokoMap()

    smap.getLineInfoandMap(filename)

    #smap.printMap()

    pos = (6,3)
    smap.getTile(pos)


    smap.printMap()

    smap.GetGoalCoordinates()



    #smap.GetRobotCoordinate()
    #spot = (7,3)

    #smap.moveRobot(spot)

    #smap.printMap()

