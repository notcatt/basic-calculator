from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt, Signal
from utils import isEmpty, isNumOrDot

class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)
    negativePressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
       margins = [TEXT_MARGIN for _ in range(4)]
       self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
       self.setMinimumHeight(BIG_FONT_SIZE * 1.75)
       self.setMinimumWidth(MINIMUM_WIDTH)
       self.setAlignment(Qt.AlignmentFlag.AlignRight)
       self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key


        if key == KEYS.Key_Return:
            self.eqPressed.emit()
            return event.ignore()

        if key == KEYS.Key_Backspace:
            self.clearPressed.emit()
            return event.ignore()

        if key == KEYS.Key_Delete:
            self.delPressed.emit()
            return event.ignore()
        
        if isEmpty(text):
            return event.ignore()
        
        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()
        
        if key in [KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P]:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()
        
        if key == KEYS.Key_N:
            self.negativePressed.emit()
            return event.ignore()