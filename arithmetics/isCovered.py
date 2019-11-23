from constants import*
from math import pi, cos, sqrt

def degsToRad(degs):
    return degs*pi/180

def isCovered(list_P_Pos, list_Cam_Pos):
    delta_x = abs(list_P_Pos[0] - list_Cam_Pos[0])
    delta_x = degsToRad(delta_x)
    delta_x *= earth_radius*cos(degsToRad(list_P_Pos[1]))

    delta_y = abs(list_P_Pos[1] - list_Cam_Pos[1])
    delta_y = degsToRad(delta_y)
    delta_y *= earth_radius

    return sqrt(delta_x**2 + delta_y**2) < cam_coverage
    