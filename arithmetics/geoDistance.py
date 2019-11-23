from constants import*
from math import pi, cos, sqrt

def degsToRad(degs):
    return degs*pi/180

def geoDistance(list_A_Pos, list_B_Pos):
    delta_x = abs(list_A_Pos[0] - list_B_Pos[0])
    delta_x = degsToRad(delta_x)
    delta_x *= earth_radius*cos(degsToRad(list_A_Pos[1]))

    delta_y = abs(list_A_Pos[1] - list_B_Pos[1])
    delta_y = degsToRad(delta_y)
    delta_y *= earth_radius

    return sqrt(delta_x**2 + delta_y**2)

def isCovered(list_A_Pos, list_B_Pos, range):
    return geoDistance(list_A_Pos, list_B_Pos) <= range
