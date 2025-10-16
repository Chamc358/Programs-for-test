from graphix import Window, Circle, Point, Line

def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
    leg1 = Line(Point(300, 240), Point(200, 320))
    leg1.draw(win)
    
    
    
    
    win.get_mouse()
    win.close()

draw_stick_figure()
