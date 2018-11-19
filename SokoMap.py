import sys
import operator
import numpy as np
from copy import deepcopy


class SokoMap:
    WALL = 'X'
    DIAMOND = 'J'
    GOAL = 'G'
    WALKABLE_AREA = '.'
    ROBOT = 'M'
    AREA_OUTSIDE_MAP = ' '


    def __init__(self):
        self.sm = []
        self.coordinatemap = []

        self.map = []


        self.gval = 0
        self.fval = 0

        self.parant = 0
        self.movelist = []

        self.xmax = 0
        self.ymax = 0
        self.nDiamonds = 0

    def getLineInfoandMap(self, filename):
        mapFile = open(filename, 'r')
        temp = mapFile.readlines()
        mapFile.close()

        for line in temp:

            self.xmax = (int(line[0]) * 10) + int(line[1])
            #print("Width: ",self.xmax)
            self.ymax = (int(line[3]) *10) + int(line[4])
            #print("Height: ",self.ymax)
            self.nDiamonds = (int(line[6]) *10) + int(line[7])
            #print("Diamonds: ",self.nDiamonds)
            break


        del temp[0:1]
        self.sm = temp

        for i in range(self.ymax):
            temprow = []

            for j in range(self.xmax):
                item = self.sm[i][j]
                temprow.append(item)
            self.map.append(temprow)

    def getTileCoordinate(self, something):
        pos = 0
        things = []
        y = 0
        for y in range(self.ymax):
            x = 0
            for x in range(self.xmax):
                if self.map[y][x] == something:
                    pos = (y,x)
                    things.append(pos)

        if len(things) > 1:
            return things
        else:
            return pos

    def getNeighBours(self, something):
        neighbours = [(-1,0),(0,1),(1,0),(0,-1)]

        coordinateOFNeighcours = []
        coordinateOfInterest = self.getTileCoordinate(something)
        for n in range(4):
            cy, cx = coordinateOfInterest
            ny, nx = neighbours[n]
            l = (cy + ny, cx + nx)
            coordinateOFNeighcours.append(l)

        #for i in coordinateOFNeighcours:
         #   print(i)
        return coordinateOFNeighcours

    def printNeighbourChars(self, char):
        chars = []
        neighbourchars = self.getNeighBours(self.ROBOT)
        for i in range(4):
            y, x = neighbourchars[i]
            chars.append(self.map[y][x])

        for l in chars:
            print(l)

    def printMap(self):
        for line in self.map:
            print(line)

    def GetDiamondCoordinates(self):
        diamonds = self.getTileCoordinate(self.DIAMOND)
        return diamonds

    def GetRobotCoordinate(self):
        robot = self.getTileCoordinate(self.ROBOT)
        self.getNeighBours(self.ROBOT)
        return robot

    def GetGoalCoordinates(self):
        goals = self.getTileCoordinate(self.GOAL)
        print(goals)
        return goals

    def getTile(self,coordinate):
        y,x = coordinate
        print(self.map[y][x])

    def setTile(self, pos, tile):
        y,x = pos
        self.map[y][x] = tile

        








