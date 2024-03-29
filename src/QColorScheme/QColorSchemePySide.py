"""Classdocs
"""
import PySideImporter

import ConfigParser
from PyQt4.QtCore import  SIGNAL
from PyQt4.QtGui import QColor, QPalette, QApplication, QMainWindow, QBrush
#import PyQt4.uic

class QColorScheme():
    """Class to ease custom colors of PyQt apps
    baseColor: This is the main background color.
    highlightColor: Typically contrasting the baseColor (e.g. used to highlight current focus)
    spread: Float value indicating the brightness range generated by generateColors (1.5-2.0 seems most reasonable)
    """
    
    def __init__(self,baseColor=QColor(50,50,50), highlightColor=QColor(247,147,30), spread=2.5, monochromeText=False, apply=True):
        """Constructor
        By default a nuke-like color scheme (dark slate + orange highlight) is created
        This can be overriden by either supplying colors or by loading a different
        scheme from disc via the load settings
        """
        self.palette = QPalette()
        self.baseColor = baseColor
        self.highlightColor = highlightColor
        self.spread = spread
        self.generateScheme(apply=apply, monochromeText=monochromeText)
        QApplication.setStyle("Plastique")
    
    def __lightness(self, color):
        """Returns simple averaged lightness of a QColor
        Newer Qt Versions implement this as part of QColor
        Reimplemented for backwards-compatibility
        """
        hsv = color.toHsv()
        return hsv.valueF()
    
#    def setColor(self, target=QApplication, Group=None, Role=None, Color=QColor()):
#        """Override any color in the given widget's palette
#        """
#        palette = target.palette()
#        palette.setBrush(getattr(QPalette, Role),Color)
#        target.setPalette(palette)
    
    def generateScheme(self, apply=True, monochromeText=True):
        """Generate color palette
        By default the generated palette is also applied to the whole application
        To override supply the apply=False argument
        """
        BASE_COLOR = self.baseColor
        HIGHLIGHT_COLOR = self.highlightColor
        BRIGHTNESS_SPREAD = self.spread
        
        if self.__lightness(BASE_COLOR) > 0.5:
            SPREAD = 100/BRIGHTNESS_SPREAD
        else:
            SPREAD = 100*BRIGHTNESS_SPREAD
        
        if self.__lightness(HIGHLIGHT_COLOR)>0.6:
            HIGHLIGHTEDTEXT_COLOR= BASE_COLOR.darker(SPREAD*2)
        else:
            HIGHLIGHTEDTEXT_COLOR= BASE_COLOR.lighter(SPREAD*2)
        
        self.palette.setBrush(QPalette.Window, QBrush(BASE_COLOR))
        
        self.palette.setBrush(QPalette.WindowText, QBrush(BASE_COLOR.lighter(SPREAD)))
        self.palette.setBrush(QPalette.Foreground, QBrush(BASE_COLOR.lighter(SPREAD)))
        self.palette.setBrush(QPalette.Base, QBrush(BASE_COLOR))
        self.palette.setBrush(QPalette.AlternateBase, QBrush(BASE_COLOR.darker(SPREAD)))
        self.palette.setBrush(QPalette.ToolTipBase, QBrush(BASE_COLOR))
        self.palette.setBrush(QPalette.ToolTipText, QBrush(BASE_COLOR.lighter(SPREAD)))
        self.palette.setBrush(QPalette.Text, QBrush(BASE_COLOR.lighter(SPREAD*1.2)))
        self.palette.setBrush(QPalette.Button, QBrush(BASE_COLOR))
        self.palette.setBrush(QPalette.ButtonText, QBrush(BASE_COLOR.lighter(SPREAD)))
        self.palette.setBrush(QPalette.BrightText, QBrush(QColor(240, 240, 240)))
        
        self.palette.setBrush(QPalette.Light, QBrush(BASE_COLOR.lighter(SPREAD)))
        self.palette.setBrush(QPalette.Midlight, QBrush(BASE_COLOR.lighter(SPREAD/2)))
        self.palette.setBrush(QPalette.Dark, QBrush(BASE_COLOR.darker(SPREAD)))
        self.palette.setBrush(QPalette.Mid, QBrush(BASE_COLOR))    
        self.palette.setBrush(QPalette.Shadow, QBrush(BASE_COLOR.darker(SPREAD*2)))    
        
        self.palette.setBrush(QPalette.Highlight, QBrush(HIGHLIGHT_COLOR))
        self.palette.setBrush(QPalette.HighlightedText, QBrush(HIGHLIGHTEDTEXT_COLOR))
        
        if monochromeText:
            lightness = self.__lightness(BASE_COLOR.lighter(SPREAD*1.2))
            textColor = QColor(lightness*255,lightness*255,lightness*255)
            self.palette.setBrush(QPalette.WindowText, QBrush(textColor))
            self.palette.setBrush(QPalette.Text, QBrush(textColor))
            self.palette.setBrush(QPalette.ButtonText, QBrush(textColor))
            self.palette.setBrush(QPalette.ToolTipText, QBrush(textColor))

        if apply:
            QApplication.setPalette(self.palette)   
    
    def applyScheme(self, target=QApplication):
        """Apply the color scheme in self.palette
        When called without arguments the whole application will be styled
        If a widget is supplied as argument only this widget will be styled
        """
        target.setPalette(self.palette)
    
    def colorFromStringTuple(self,tuple):
        return QColor(int(tuple[0]),int(tuple[1]),int(tuple[2]))
        
    def loadSimpleScheme(self, file, apply=True):
        scheme = ConfigParser.ConfigParser()
        scheme.read(file)
        self.baseColor = self.colorFromStringTuple(scheme.get("AutoColors", "baseColor").split(","))
        self.highlightColor = self.colorFromStringTuple(scheme.get("AutoColors", "highlightColor").split(","))
        self.spread = float(scheme.get("AutoColors", "spread"))
        if apply:
            self.generateScheme()
        else:
            self.generateScheme(apply=False)
    
    def loadScheme(self, file):
        """TODO: Implement
        """
        raise NotImplementedError     
    
