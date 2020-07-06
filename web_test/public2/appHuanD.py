
class TestSwipe():
    def __init__(self,driver):
        self.driver = driver
    def getsize(self):      #获取屏幕的大小
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x,y)
    #向上滑动(x值不变，y由大变小)
    def swipeup(self,t):
        l = self.getsize()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.8)
        y2 = int(l[1]*0.3)
        return self.driver.swipe(x1,y1,x1,y2,t)
    #向下滑动（x值不变，y值由小变大）
    def swipedown(self,t):
        l = self.getsize()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.25)
        y2 = int(l[1]*0.8)
        return self.driver.swipe(x1,y1,x1,y2,t)
    #向左滑动（y值不变，x值由大变小）
    def swipeleft(self,t):
        l = self.getsize()
        y = int(l[1]*0.5)
        x1 =int(l[0]*0.8)
        x2 =int(l[0]*0.1)
        return self.driver.swipe(x1,y,x2,y,t)
    #向右滑动（y值不变，x值由小变大）
    def swiperight(self,t):
        l = self.getsize()
        y = int(l[1]*0.5)
        x1 = int(l[0]*0.2)
        x2 = int(l[0]*0.8)
        return self.driver.swipe(x1,y,x2,y,t)