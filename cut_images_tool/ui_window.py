# -*- coding: utf-8 -*-
import sys
import PyQt5
from PyQt5.QtCore import QSize, QRect, Qt, QMetaObject, QCoreApplication, QPoint
from PyQt5.QtGui import QFont, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QSizePolicy, QWidget, QFrame, QGroupBox, QLabel, QPushButton, QMenuBar, QStatusBar, QScrollArea, \
    QAbstractScrollArea, QLineEdit
from pyqt5_plugins.examplebuttonplugin import QtGui


class BorderLabel(QLabel):
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawRect(self.rect())

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1378, 908)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 60, 1211, 801))
        self.label_img_show = BorderLabel(self.groupBox)   # QLabel(self.groupBox)
        self.label_img_show.setObjectName(u"label_img_show")
        self.label_img_show.setGeometry(QRect(5, 10, 1201, 786))
        font = QFont()
        font.setPointSize(12)
        self.label_img_show.setFont(font)
        self.lineEdit_imgread_path = QLineEdit(self.centralwidget)
        self.lineEdit_imgread_path.setObjectName(u"lineEdit_imgread_path")
        self.lineEdit_imgread_path.setGeometry(QRect(130, 18, 401, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_imgread_path.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 7, 121, 31))
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(17, 34, 121, 20))
        self.label_2.setFont(font1)
        self.pushButton_start_system = QPushButton(self.centralwidget)
        self.pushButton_start_system.setObjectName(u"pushButton_start_system")
        self.pushButton_start_system.setGeometry(QRect(540, 14, 75, 40))
        self.pushButton_start_system.setFont(font)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(620, 2, 135, 62))
        self.pushButton_aboveimg = QPushButton(self.groupBox_2)
        self.pushButton_aboveimg.setObjectName(u"pushButton_aboveimg")
        self.pushButton_aboveimg.setGeometry(QRect(57, 4, 71, 25))
        self.pushButton_aboveimg.setFont(font)
        self.pushButton_nextimg = QPushButton(self.groupBox_2)
        self.pushButton_nextimg.setObjectName(u"pushButton_nextimg")
        self.pushButton_nextimg.setGeometry(QRect(57, 33, 71, 25))
        self.pushButton_nextimg.setFont(font)
        self.pushButton_autonext = QPushButton(self.groupBox_2)
        self.pushButton_autonext.setObjectName(u"pushButton_autonext")
        self.pushButton_autonext.setGeometry(QRect(10, 4, 41, 55))
        self.pushButton_autonext.setFont(font)
        # def dd(): print('===')
        # self.pushButton_autonext.clicked.connect(dd)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(770, 14, 101, 31))
        self.label_3.setFont(font)
        self.lineEdit_imgsave_path = QLineEdit(self.centralwidget)
        self.lineEdit_imgsave_path.setObjectName(u"lineEdit_imgsave_path")
        self.lineEdit_imgsave_path.setGeometry(QRect(850, 17, 341, 31))
        self.lineEdit_imgsave_path.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(786, 42, 91, 20))
        self.label_4.setFont(font1)
        self.pushButton_aboveimg_cut = QPushButton(self.centralwidget)
        self.pushButton_aboveimg_cut.setObjectName(u"pushButton_aboveimg_cut")
        self.pushButton_aboveimg_cut.setGeometry(QRect(1260, 130, 71, 31))
        self.pushButton_aboveimg_cut.setFont(font)
        self.pushButton_nextimg_cut = QPushButton(self.centralwidget)
        self.pushButton_nextimg_cut.setObjectName(u"pushButton_nextimg_cut")
        self.pushButton_nextimg_cut.setGeometry(QRect(1260, 170, 71, 31))
        self.pushButton_nextimg_cut.setFont(font)
        self.pushButton_autosave = QPushButton(self.centralwidget)
        self.pushButton_autosave.setObjectName(u"pushButton_autosave")
        self.pushButton_autosave.setGeometry(QRect(1210, 12, 121, 41))
        self.pushButton_autosave.setFont(font)
        self.pushButton_saveimg = QPushButton(self.centralwidget)
        self.pushButton_saveimg.setObjectName(u"pushButton_saveimg")
        self.pushButton_saveimg.setGeometry(QRect(1260, 230, 71, 41))
        self.pushButton_saveimg.setFont(font)
        self.pushButton_cancel = QPushButton(self.centralwidget)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(1260, 280, 71, 41))
        self.pushButton_cancel.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1230, 60, 121, 31))
        self.label_5.setFont(font1)
        self.lineEdit_imgsave_name = QLineEdit(self.centralwidget)
        self.lineEdit_imgsave_name.setObjectName(u"lineEdit_imgsave_name")
        self.lineEdit_imgsave_name.setGeometry(QRect(1230, 90, 121, 31))
        self.lineEdit_imgsave_name.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1236, 795, 131, 31))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1233, 820, 140, 31))
        self.label_8.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1378, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_img_show.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u8f93\u5165\u8def\u5f84\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939 / \u6587\u4ef6", None))
        self.pushButton_start_system.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6", None))
        self.groupBox_2.setTitle("")
        self.pushButton_aboveimg.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
        self.pushButton_nextimg.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
        self.pushButton_autonext.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939", None))
        self.pushButton_aboveimg_cut.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
        self.pushButton_nextimg_cut.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
        self.pushButton_autosave.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u4fdd\u5b58\u6a21\u5f0f", None))
        self.pushButton_saveimg.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6587\u4ef6\u540d(.jpg)\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Make by\uff1aKingbiu", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"1780126040@qq.com", None))
    # retranslateUi

import cv2 as cv
import threading

class myWindow(QWidget):

    def getImg(self, img=None, imgpath=None, path=None, **kwargs):
        self.imgPixmap = None
        if img is not None:
            img = img.astype("uint8")
            self.original_img = img.copy()
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            # print('myWindow: get image shape=', img.shape )
            img = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
            self.imgPixmap = QPixmap(img)  # 载入图片
            # self.imgPixmap = QPixmap.fromImage(img)  # 载入图片
        else:
            if path: imgpath = path
            if imgpath:
                self.imgPixmap = QPixmap(imgpath)  # 载入图片
                self.original_img = cv.imread(imgpath)
                self.image_path = imgpath
        if not self.imgPixmap: return
        # print('image size:', self.imgPixmap.size())
        if not self.imgPixmap.isNull():
            pixmap = self.imgPixmap
            self.aspect_ratio = pixmap.width() / pixmap.height()
            self.repaint()
        self.calc_img_to_widget()

    def calc_img_to_widget(self):
        imgx, imgy = self.imgPixmap.width(), self.imgPixmap.height()
        widgetx, widgety = self.width(), self.height()
        # print(f'img=[{imgx, imgy}], widgt=[{widgetx, widgety}] ' )
        ratiox = widgetx/imgx
        ratioy = widgety / imgy
        if ratiox<ratioy: self.img_widget_ratio = ratiox
        else: self.img_widget_ratio = ratioy

    def set_image(self, img):
        # 将新的img转换为QPixmap，并更新self.imgPixmap
        # image = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)  # .rgbSwapped()
        # self.imgPixmap = QPixmap.fromImage(image)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
        self.imgPixmap = QPixmap(img)  # 载入图片
        self.repaint()  # 重新绘制窗口

    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_path = None  # 图片路径
        self.scale_factor = 1.0  # 缩放因子
        self.offset = QPoint(0, 0)  # 偏移量
        self.aspect_ratio = 1.0  # 宽高比
        self.img_widget_ratio = 1.0

        self.mask_pos_start = None
        self.mask_pos_end = None
        self.state_lock = threading.Lock()
        self.state_ready = False
        self.mouse_is_drag = False

        # self.paint_outline()
    def set_state_ready(self, sta):
        with self.state_lock: self.state_ready = sta

    def get_state_ready(self):
        with self.state_lock: return self.state_ready

    def get_mask_positon(self):
        if not self.state_ready: return None
        x1, y1 = self.calc_pos(self.mask_pos_start)
        x2, y2 = self.calc_pos(self.mask_pos_end)
        self.mask_pos_start = None
        self.mask_pos_end = None
        self.set_state_ready(False)
        return [[x1,y1], [x2, y2]]

    def paint_outline(self):
        painter = QPainter(self)  # 创建画家对象
        """ 绘制外框线 """
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawRect(self.rect())
        self.repaint()

    def paintEvent(self, event):
        if self.imgPixmap is not None:
            painter = QPainter(self)  # 创建画家对象
            # painter.begin(self)  # 无需手动调用begin和end
            painter.translate(self.offset)  # 根据偏移量进行平移
            painter.scale(self.scale_factor, self.scale_factor)  # 根据缩放因子进行缩放坐标轴
            # painter.scale(1., 1.)  # 根据缩放因子进行缩放坐标轴
            pixmap = self.imgPixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 缩放图片
            painter.drawPixmap(0, 0, pixmap)  # 在窗口绘制图片
            # painter.end()  # 无需手动调用begin和end
            """ 绘制外框线 """
            painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(self.rect())
            # print('paintEvent:', f'scale_factor={self.scale_factor}, width={self.width()}, {self.aspect_ratio}, '
            #                      f'offset={self.offset}, size={self.size()}, imgPixmap={self.imgPixmap.size()}, , ')


    # def resizeEvent(self, event):
    #     if self.imgPixmap is not None:
    #         # scaled_width = self.height() * self.aspect_ratio  # 按照宽高比计算缩放后的宽度
    #         # if scaled_width > self.width():  # 如果缩放后的宽度大于窗口宽度
    #         #     self.scale_factor = self.width() / (self.height() * self.aspect_ratio)  # 计算缩放因子
    #         # else:
    #         #     # self.scale_factor = 1.0  # 不需要缩放，缩放因子为1
    #         #     self.scale_factor = self.height() / (self.width() / self.aspect_ratio)  # 计算缩放因子
    #         # print('resize:', self.scale_factor, scaled_width, self.width(), self.height(), self.aspect_ratio)
    #         self.scale_factor = 1.0  # 不需要缩放，缩放因子为1
    #         self.repaint()  # 重绘窗口

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # 如果是鼠标左键点击
            self.last_pos = event.pos()  # 记录点击位置
            ''' 记录 mask 区域 '''
            self.mouse_is_drag = False
            # if not self.mouse_is_drag and self.mask_pos_start is None:
            #     self.mask_pos_start = event.pos()-self.offset  # 记录到原点的相对距离，以适应变动
            #     print('\t start making mask.')
            # print('button down.')

        if event.button() == Qt.RightButton:
            self.offset = QPoint(0, 0)  # 偏移量
            self.scale_factor = 1.0
            self.repaint()  # 重绘窗口

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:  # 如果是鼠标左键点击
            ''' 记录 mask 区域 '''
            if not self.mouse_is_drag and self.mask_pos_start is None:
                self.mask_pos_start = event.pos()-self.offset  # 记录到原点的相对距离，以适应变动
                self.set_state_ready(False)
                self.mask_pos_end = None

            elif not self.mouse_is_drag and self.mask_pos_start is not None and self.mask_pos_end is None :
                self.mask_pos_end = event.pos() - self.offset  # 记录到原点的相对距离，以适应变动
                self.set_state_ready(True)
            self.image_mask_dynamic(event)
                

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:  # 如果是鼠标左键拖动
            self.mouse_is_drag = True
            diff = event.pos() - self.last_pos  # 计算鼠标移动的距离
            self.offset += diff  # 更新偏移量
            self.last_pos = event.pos()  # 更新上一次鼠标位置
            self.repaint()  # 重绘窗口


        if self.mask_pos_start is not None:
            self.image_mask_dynamic(event)
        #     mouse_pos = event.pos()
        #     print("Mouse Position:", mouse_pos.x(), mouse_pos.y())

    def wheelEvent(self, event):
        scroll_amount = event.angleDelta().y() / 120  # 计算滚动量
        scale_factor = 1.1 ** scroll_amount  # 根据滚动量计算缩放因子
        pivot = event.pos()  # 获取滚动中心点位置
        self.offset = scale_factor * (self.offset - pivot) + pivot  # 根据缩放因子更新偏移量
        self.scale_factor *= scale_factor  # 更新缩放因子
        self.repaint()  # 重绘窗口
        # self.mask_pos_start = scale_factor * (self.mask_pos_start - pivot) + pivot

    def enterEvent(self, event):
        self.setMouseTracking(True) # 触发mouseMoveEvent实时跟踪

    def leaveEvent(self, event):
        self.setMouseTracking(False)

    def calc_pos(self, pos):
        click_pos = pos  # 获取点击位置  event.pos()  # 获取点击位置
        image_pos = (click_pos - self.offset) / self.scale_factor / self.img_widget_ratio  # 根据偏移量和缩放因子计算图片位置
        image_x, image_y = int(image_pos.x()), int(image_pos.y())  # 转换为整数坐标
        return image_x, image_y

    def image_mask_dynamic(self, event):
        calc_pos = self.calc_pos
        if self.mask_pos_start is not None and self.mask_pos_end is None:
            # click_pos = event.pos()  # 获取点击位置
            # image_pos = (click_pos - self.offset) / self.scale_factor / self.img_widget_ratio  # 根据偏移量和缩放因子计算图片位置
            # image_x, image_y = int(image_pos.x()), int(image_pos.y())  # 转换为整数坐标
            # print('click_pos', click_pos, ',  image_pos', image_pos, ',  offset', self.offset, ',\n\t  scale_factor', self.scale_factor,
            #       ',  img size', self.imgPixmap.size())
            image_x, image_y = calc_pos(event.pos())
            # 使用OpenCV绘制圆形标记
            img = self.original_img.copy()
            cv.drawMarker(img, (image_x, image_y), (0, 255, 0), markerSize=int(8/self.scale_factor))

            image_x2, image_y2 = calc_pos(self.offset + self.mask_pos_start*self.scale_factor)  # 转换为整数坐标
            cv.drawMarker(img, (image_x2, image_y2), (0, 255, 0), markerSize=int(8/self.scale_factor))

            if image_x-image_x2==0 and image_y-image_y2==0: pass
            elif image_x-image_x2==0 or image_y-image_y2==0:
                cv.line(img, (image_x2, image_y2), (image_x, image_y), (0,255,0, 1), int(1/self.scale_factor))
            else:
                cv.rectangle(img, (image_x2, image_y2), (image_x, image_y), (0,255,0, 1), int(1/self.scale_factor))
            self.set_image(img)





