import numpy as np

def circle(cx=300, cy=300, r=100, num_points=100):
    """
    Generate points for a circle path.
    """
    points = []
    for i in range(num_points):
        theta = 2 * np.pi * i / num_points
        x = int(cx + r * np.cos(theta))
        y = int(cy + r * np.sin(theta))
        points.append((x,y))
    return points

def square(cx=300, cy=300, side=200, num_points=100):
    """
    Generate points for a square path.
    """
    points = []
    half = side // 2
    corners = [(cx-half, cy-half), (cx+half, cy-half),
               (cx+half, cy+half), (cx-half, cy+half)]

    for i in range(4):
        x1, y1 = corners[i]
        x2, y2 = corners[(i+1)%4]
        for t in np.linspace(0, 1, num_points//4):
            x = int(x1 + t * (x2-x1))
            y = int(y1 + t * (y2-y1))
            points.append((x,y))
    return points

def line(x1=200, y1=200, x2=400, y2=400, num_points=50):
    """
    Generate points for a straight line.
    """
    points = []
    for t in np.linspace(0, 1, num_points):
        x = int(x1 + t * (x2-x1))
        y = int(y1 + t * (y2-y1))
        points.append((x, y))
    return points

def triangle(cx=300, cy=300, side=200, num_points=90):
    """
    Generate points for an equilateral triangle.
    """
    points = []
    h = int(np.sqrt(3) / 2 * side)
    corners = [(cx, cy-h//2), (cx-side//2, cy+h//2), (cx+side//2, cy+h//2)]
    for i in range(3):
        x1, y1 = corners[i]
        x2, y2 = corners[(i+1) % 3]
        for t in np.linspace(0, 1, num_points//3):
            x = int(x1 + t * (x2-x1))
            y = int(y1 + t * (y2-y1))
            points.append((x,y))
    return points