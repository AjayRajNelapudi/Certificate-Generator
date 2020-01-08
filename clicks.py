import cv2 as cv

class MouseClickCapture:
    def __init__(self, certificate_template):
        self.certificate_template = certificate_template
        self.points = []

    def capture_clicks(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            self.points.append((x, y + 15))
            cv.line(self.template, (x, y), (x, y + 25), (0, 0, 0), 2)

    def display_template(self):
        self.template = cv.imread(self.certificate_template, cv.IMREAD_COLOR)
        cv.imshow('Template', self.template)
        cv.setMouseCallback('Template', self.capture_clicks)
        while True:
            cv.imshow('Template', self.template)
            if cv.waitKey(20) & 0xFF == 13:
                break
        cv.destroyAllWindows()
