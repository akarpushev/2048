from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QIcon, QFont, QColor, QPainter, QPen
from PySide6.QtCore import Qt, QRect, QPoint
import random
import os
import copy


class GameForm(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.colors = {0: (204, 192, 179), 2: (238, 228, 218), 4: (237, 224, 200),
                       8: (242, 177, 121), 16: (245, 149, 99), 32: (246, 124, 95),
                       64: (246, 94, 59), 128: (237, 207, 114), 256: (237, 207, 114),
                       512: (237, 207, 114), 1024: (237, 207, 114), 2048: (237, 207, 114),
                       4096: (237, 207, 114), 8192: (237, 207, 114), 16384: (237, 207, 114),
                       32768: (237, 207, 114), 65536: (237, 207, 114), 131072: (237, 207, 114),
                       262144: (237, 207, 114), 524288: (237, 207, 114), 1048576: (237, 207, 114)}
        #self.initGameOpt()???????????????????????????????????????????????????????
        self.initGameData()
        self.grid

    def initUi(self):
        """Инициализация интерфейса"""
        self.setWindowTitle("2048")
        self.setWindowIcon(QIcon('2048.png'))
        self.initGameOpt()  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.grid = 0
        msg = QMessageBox()
        msg.setWindowTitle("Добро пожаловать")
        msg.setWindowIcon(QIcon('2048.png'))
        msg.setText("Выберите размер поля")
        Button3 = msg.addButton("3X3", QMessageBox.ButtonRole.AcceptRole)
        Button4 = msg.addButton("4X4", QMessageBox.ButtonRole.AcceptRole)
        Button5 = msg.addButton("5X5", QMessageBox.ButtonRole.AcceptRole)
        msg.setDefaultButton(Button4)
        msg.exec()
        if msg.clickedButton() == Button3:
            self.grid = 3
            self.resize(550, 550)
        elif msg.clickedButton() == Button4:
            self.grid = 4
            self.resize(520, 670)
        elif msg.clickedButton() == Button5:
            self.grid = 5
            self.resize(620, 760)  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def initGameOpt(self):
        """Инициализация шрифтов"""
        self.lbFont = QFont('Colibri', 8)  # текст
        self.lgFont = QFont('Times', 38)  # логотип
        self.nmFont = QFont('SimSun', 36)  # числа на фишках

    def initGameData(self):
        """Инициализация данных игры"""
        #self.data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        if self.grid == 3:
            self.data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        elif self.grid == 4:
            self.data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        else:
            self.data = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        count = 0
        while count < 2:
            row = random.randint(0, len(self.data) - 1)
            col = random.randint(0, len(self.data[0]) - 1)
            if self.data[row][col] != 0:
                continue
            self.data[row][col] = 2 if random.randint(0, 1) else 4
            count += 1

        self.curScore = 0
        self.bstScore = 0
        # Загрузить рекорд
        if os.path.exists("bestscore.txt"):
            with open("bestscore.txt", "r") as f:
                self.bstScore = int(f.read())

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawGameGraph(qp)
        qp.end()

    def keyPressEvent(self, event) -> None:
        """
        Действие при нажатии клавиш.
        :param event: event
        :return: None
        """
        keyCode = event.key()
        ret = False
        if keyCode == Qt.Key.Key_Left:
            ret = self.move("Left")
        elif keyCode == Qt.Key.Key_Right:
            ret = self.move("Right")
        elif keyCode == Qt.Key.Key_Up:
            ret = self.move("Up")
        elif keyCode == Qt.Key.Key_Down:
            ret = self.move("Down")
        else:
            pass

        if ret:
            self.repaint()

    def closeEvent(self, event) -> None:
        """
        Сохранение рекорда.
        :param event: event
        :return: None
        """
        with open("bestscore.txt", "w") as f:
            f.write(str(self.bstScore))

    def drawGameGraph(self, qp):
        """Графика игры"""
        self.drawLog(qp)
        self.drawLabel(qp)
        self.drawScore(qp)
        self.drawBackground(qp)
        self.drawTiles(qp)

    def drawScore(self, qp):
        """Окно со счётом в игре"""
        qp.setFont(self.lbFont)
        fontsize = self.lbFont.pointSize()
        scoreLabelSize = len("СЧЁТ") * fontsize
        bestLabelSize = len("РЕКОРД") * fontsize
        curScoreBoardMinW = 15 * 2 + scoreLabelSize  # минимальная ширина столбца "Счет"
        bstScoreBoardMinW = 15 * 2 + bestLabelSize  # ширина столбца "рекорд"
        curScoreSize = len(str(self.curScore)) * fontsize
        bstScoreSize = len(str(self.bstScore)) * fontsize
        curScoreBoardNedW = 10 + curScoreSize
        bstScoreBoardNedW = 10 + bstScoreSize
        curScoreBoardW = max(curScoreBoardMinW, curScoreBoardNedW)
        bstScoreBoardW = max(bstScoreBoardMinW, bstScoreBoardNedW)
        qp.setBrush(QColor(187, 173, 160))
        qp.setPen(QColor(187, 173, 160))
        qp.drawRect(505 - 15 - bstScoreBoardW, 40, bstScoreBoardW, 50)
        qp.drawRect(505 - 15 - bstScoreBoardW - 5 - curScoreBoardW, 40, curScoreBoardW, 50)

        bstLabelRect = QRect(505 - 15 - bstScoreBoardW, 40, bstScoreBoardW, 25)
        bstScoreRect = QRect(505 - 15 - bstScoreBoardW, 65, bstScoreBoardW, 25)
        scoerLabelRect = QRect(505 - 15 - bstScoreBoardW - 5 - curScoreBoardW, 40, curScoreBoardW, 25)
        curScoreRect = QRect(505 - 15 - bstScoreBoardW - 5 - curScoreBoardW, 65, curScoreBoardW, 25)

        qp.setPen(QColor(238, 228, 218))
        qp.drawText(bstLabelRect, Qt.AlignmentFlag.AlignCenter, "РЕКОРД")
        qp.drawText(scoerLabelRect, Qt.AlignmentFlag.AlignCenter, "СЧЁТ")

        qp.setPen(QColor(255, 255, 255))
        qp.drawText(bstScoreRect, Qt.AlignmentFlag.AlignCenter, str(self.bstScore))
        qp.drawText(curScoreRect, Qt.AlignmentFlag.AlignCenter, str(self.curScore))

    def drawBackground(self, qp) -> None:
        """
        Отображение фона.
        :param qp: QPainter()
        :return: None
        """
        col = QColor(187, 173, 160)
        qp.setPen(col)

        qp.setBrush(QColor(187, 173, 160))
        if self.grid == 3:
            qp.drawRect(15, 150, 360, 360)
        elif self.grid == 4:
            qp.drawRect(15, 150, 475, 475)
        elif self.grid == 5:
            qp.drawRect(15, 150, 590, 590)

    def drawLog(self, qp) -> None:
        """
        Отображение названия игры.
        :param qp: QPainter()
        :return: None
        """
        pen = QPen(QColor(255, 93, 29), 15)
        qp.setFont(self.lgFont)
        qp.setPen(pen)
        qp.drawText(QRect(10, 0, 150, 130), Qt.AlignmentFlag.AlignCenter, "2048")

    def drawLabel(self, qp) -> None:
        """
        Отображение информации как играть.
        :param qp: QPainter()
        :return: None
        """
        qp.setFont(self.lbFont)
        qp.setPen(QColor(119, 110, 101))
        qp.drawText(5, 134, "Совмещайте таблички с одинаковыми числами, чтобы получить 2048!")
        qp.drawText(5, 760, "Как играть:")
        qp.drawText(15, 780, "Используйте клавиши со стрелками, чтобы переместить квадрат")
        qp.drawText(15, 800, "Два квадрата с одинаковым числом объединяются в один")


    def drawTiles(self, qp):
        """Нарисовать клетки"""
        qp.setFont(self.nmFont)
        for row in range(self.grid):  #self.grid
            for col in range(self.grid):  #self.grid
                value = self.data[row][col]
                color = self.colors[value]

                qp.setPen(QColor(*color))
                qp.setBrush(QColor(*color))
                qp.drawRect(30 + col * 115, 165 + row * 115, 100, 100)
                size = self.nmFont.pointSize() * len(str(value))  # Получить длину числа
                # Подгоняем размер шрифта в соответствии с размером числа
                while size > 100 - 15 * 2:
                    self.nmFont = QFont('SimSun', self.nmFont.pointSize() * 4 // 5)
                    qp.setFont(self.nmFont)
                    size = self.nmFont.pointSize() * len(str(value))   # Получить длину числа в текущем шрифте
                print("[%d][%d]: value[%d] weight: %d" % (row, col, value, size))

                if value == 2 or value == 4:
                    qp.setPen(QColor(119, 110, 101))  # Установим цвет чисел 2 и 4 (из-за фона)
                else:
                    qp.setPen(QColor(255, 255, 255))  # Установим цвет остальных чисел
                # Рисуем все числа, кроме нулей
                if value != 0:
                    rect = QRect(30 + col * 115, 165 + row * 115, 100, 100)
                    qp.drawText(rect, Qt.AlignmentFlag.AlignCenter, str(value))

    def putTile(self) -> bool:
        """
        Заполнение пустой позиции 2 или 4.
        :return: bool
        """
        available = []
        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                if self.data[row][col] == 0:
                    available.append((row, col))
        if available:
            row, col = available[random.randint(0, len(available) - 1)]
            self.data[row][col] = 2 if random.randint(0, 1) else 4
            return True
        return False

    def merge(self, row) -> list:
        """
        Объединение строк и столбцов.
        :param row:
        :return: list
        """
        pair = False
        newRow = []
        for i in range(len(row)):
            if pair:
                newRow.append(2 * row[i])
                self.curScore += 2 * row[i]
                pair = False
            else:
                if i + 1 < len(row) and row[i] == row[i + 1]:
                    pair = True
                else:
                    newRow.append(row[i])
        return newRow

    def slideUpDown(self, isUp) -> bool:
        """
        Перемещение сетки с числами вверх - вниз.
        :param isUp: True если нажата кнопка вверх, False если нажата кнопка вниз
        :return: bool
        """
        numRows = len(self.data)
        numCols = len(self.data[0])
        oldData = copy.deepcopy(self.data)

        for col in range(numCols):
            cvl = []
            for row in range(numRows):
                if self.data[row][col] != 0:
                    cvl.append(self.data[row][col])  # Извлекаем ненулевые элементы в столбце
            if len(cvl) >= 2:
                cvl = self.merge(cvl)  # Объединение одинаковых чисел
            # Заполнение 0 в соответствии с направлением движения
            for i in range(numRows - len(cvl)):
                if isUp:
                    cvl.append(0)
                else:
                    cvl.insert(0, 0)
            for row in range(numRows):
                self.data[row][col] = cvl[row]

        return oldData != self.data  # Возвращаем, изменились ли данные

    def slideLeftRight(self, isLeft) -> bool:
        """
        Перемещение сетки с числами вправо - влево.
        :param isLeft: True если нажата кнопка налево, False если нажата кнопка направо
        :return: bool
        """
        numRows = len(self.data)
        numCols = len(self.data[0])
        oldData = copy.deepcopy(self.data)

        for row in range(numRows):
            rvl = []
            for col in range(numCols):
                if self.data[row][col] != 0:
                    rvl.append(self.data[row][col])  # Извлекаем ненулевые элементы в строке
            if len(rvl) >= 2:
                rvl = self.merge(rvl)  # Объединение одинаковых чисел
            # Заполнение 0 в соответствии с направлением движения
            for i in range(numCols - len(rvl)):
                if isLeft:
                    rvl.append(0)
                else:
                    rvl.insert(0, 0)
            for col in range(numCols):
                self.data[row][col] = rvl[col]

        return oldData != self.data  # Возвращаем, изменились ли данные

    def move(self, direction) -> bool:
        """
        Перемещение числовой сетки.
        :param direction: self.move
        :return: bool
        """
        is_move = False
        if direction == "Up":
            is_move = self.slideUpDown(True)
        elif direction == "Down":
            is_move = self.slideUpDown(False)
        elif direction == "Left":
            is_move = self.slideLeftRight(True)
        elif direction == "Right":
            is_move = self.slideLeftRight(False)
        else:
            pass
        if not is_move:
            return False

        self.putTile()  # Заполнение пустой позиции.
        if self.curScore > self.bstScore:
            self.bstScore = self.curScore

        if self.isGameOver():
            button = QMessageBox.warning(self, "Игра окончена",
                                        f"Ваш счёт: {self.curScore}, начать заново?",
                                        QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No)

            if button == QMessageBox.StandardButton.Ok:
                self.initGameOpt()
                bstScore = self.bstScore
                self.initGameData()
                self.bstScore = bstScore
                return True
            else:
                self.close()
                return False
        else:
            return True

    def isGameOver(self) -> bool:
        """
        Определение возможности продолжить игру.
        :return: bool
        """
        copyData = copy.deepcopy(self.data)  # Сначала временно сохраняем значения данных
        curScore = self.curScore

        flag = False
        if not self.slideUpDown(True) and not self.slideUpDown(False) and \
                not self.slideLeftRight(True) and not self.slideLeftRight(False):
            flag = True  # Больше не может двигаться во всех направлениях
        self.curScore = curScore
        if not flag:
            self.data = copyData  # Все еще можно переместить, а затем восстановить исходные данные
        return flag


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    form = GameForm()
    form.show()
    app.exec()
