# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FaceMaskDetection.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import icon
import sys

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QImage, QPixmap
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication
from astropy.utils import argparse
import argparse
import opencv_dnn_infer
# anchor configuration
from utils.anchor_decode import decode_bbox
from utils.anchor_generator import generate_anchors
from utils.nms import single_class_non_max_suppression


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1880, 993)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bg/images/maskIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vedio_1 = QtWidgets.QPushButton(self.centralwidget)
        self.vedio_1.setGeometry(QtCore.QRect(1480, 290, 81, 81))
        self.vedio_1.setIcon(QIcon(":/bg/images/vedio.png"))
        self.vedio_1.setStyleSheet("background:transparent;")
        self.vedio_1.setIconSize(QSize(70, 70))
        self.vedio_1.setToolTip("打开摄像头")
        self.vedio_1.setToolTipDuration(-1)
        self.vedio_1.setWhatsThis("")
        # self.vedio_1.setStyleSheet("border-image: url(:/bg/images/vedio.png);")
        self.vedio_1.setText("")
        self.vedio_1.setObjectName("vedio_1")
        self.vedio_2 = QtWidgets.QPushButton(self.centralwidget)
        self.vedio_2.setGeometry(QtCore.QRect(1480, 460, 81, 71))
        self.vedio_2.setIcon(QIcon(":/bg/images/vedio2.png"))
        self.vedio_2.setStyleSheet("background:transparent;")
        self.vedio_2.setIconSize(QSize(70, 70))
        self.vedio_2.setToolTip("切换摄像头")
        # self.vedio_2.setStyleSheet("border-image: url(:/bg/images/vedio2.png);")
        self.vedio_2.setText("")
        self.vedio_2.setObjectName("vedio_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(440, 80, 1000, 800))
        self.widget.setStyleSheet("border-radius:10px;\n"
                                  "border:4px solid rgb(100, 100,189)")
        self.widget.setObjectName("widget")
        self.show = QtWidgets.QLabel(self.widget)
        self.show.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.show.setStyleSheet("border-radius:10px;\n"
                                "border:4px solid rgb(100, 100,189)")
        self.show.setText("")
        self.show.setObjectName("show")
        # self.frame = QtWidgets.QFrame(self.centralwidget)
        # self.frame.setGeometry(QtCore.QRect(440, 80, 1000, 800))
        # self.frame.setStyleSheet("border-radius:10px;\n"
        # "border:4px solid rgb(100, 100,189)")
        # self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        # self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.frame.setLineWidth(3)
        # self.frame.setMidLineWidth(3)
        # self.frame.setObjectName("frame")
        self.shut_vedio = QtWidgets.QPushButton(self.centralwidget)
        self.shut_vedio.setGeometry(QtCore.QRect(1480, 620, 81, 71))
        self.shut_vedio.setIcon(QIcon(":/bg/images/shut_v.png"))
        self.shut_vedio.setStyleSheet("background:transparent;")
        self.shut_vedio.setIconSize(QSize(70, 70))
        self.shut_vedio.setToolTip("关闭摄像头")
        self.shut_vedio.setText("")
        self.shut_vedio.setObjectName("shut_vedio")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(630, 10, 621, 61))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 87 18pt \"Garamond\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(640, 910, 221, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(17, 224, 255);\n"
                                    "border-radius:5px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.img_rec = QtWidgets.QPushButton(self.centralwidget)
        self.img_rec.setGeometry(QtCore.QRect(550, 910, 61, 41))
        self.img_rec.setIcon(QIcon(":/bg/images/img_rec.png"))
        self.img_rec.setStyleSheet("background:transparent;")
        self.img_rec.setIconSize(QSize(50, 50))
        self.img_rec.setToolTip("图像识别")
        self.img_rec.setText("")
        self.img_rec.setObjectName("img_rec")
        self.img_rec.clicked.connect(self.run_on_image)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1110, 910, 221, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(17, 224, 255);\n"
                                      "border-radius:5px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.mp4_rec = QtWidgets.QPushButton(self.centralwidget)
        self.mp4_rec.setGeometry(QtCore.QRect(1010, 910, 51, 41))
        self.mp4_rec.setIcon(QIcon(":/bg/images/vedio_rec.png"))
        self.mp4_rec.setStyleSheet("background:transparent;")
        self.mp4_rec.setIconSize(QSize(50, 50))
        self.mp4_rec.setToolTip("视频识别")
        self.mp4_rec.setText("")
        self.mp4_rec.setObjectName("mp4_rec")
        self.mp4_rec.clicked.connect(self.run_on_video)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(-10, -10, 1881, 971))
        self.listView.setToolTip("")
        self.listView.setToolTipDuration(-1)
        self.listView.setStyleSheet("border-image: url(:/bg/images/bg.jpg);\n"
                                    "")
        self.listView.setFrameShape(QtWidgets.QFrame.Panel)
        self.listView.setLineWidth(4)
        self.listView.setMidLineWidth(3)
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.vedio_1.raise_()
        self.vedio_1.clicked.connect(self.run_on_video1)
        self.vedio_2.raise_()
        self.vedio_2.clicked.connect(self.run_on_video2)
        self.shut_vedio.raise_()
        self.shut_vedio.clicked.connect(self.shut_video)
        self.label.raise_()
        self.lineEdit.raise_()
        self.img_rec.raise_()
        self.lineEdit_2.raise_()
        self.mp4_rec.raise_()
        # self.frame.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸口罩识别系统"))
        self.label.setText(_translate("MainWindow", "基于深度神经网络的人脸口罩识别系统"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "图像识别"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "视频识别"))

    def run_on_image(self, Net, conf_thresh=0.5):
        parser = argparse.ArgumentParser(description="Face Mask Detection")
        parser.add_argument('--proto', type=str, default='models/face_mask_detection.prototxt', help='prototxt path')
        parser.add_argument('--model', type=str, default='models/face_mask_detection.caffemodel', help='model path')
        parser.add_argument('--video-path', type=str, default='0', help='path to your video, `0` means to use camera.')
        # parser.add_argument('--hdf5', type=str, help='keras hdf5 file')
        args = parser.parse_args()
        Net = cv2.dnn.readNet(args.model, args.proto)
        video_path = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./", "图片(*.jpg;*.png)")[0]
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            raise ValueError("Video open failed.")
            return
        status = True
        while status:
            status, img_raw = self.cap.read()
            if not status:
                # print("Done processing !!!")
                self.cap.release()
                break
            img_raw = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
            img_raw = opencv_dnn_infer.inference(Net, img_raw, target_shape=(260, 260), conf_thresh=conf_thresh)
            # cv2.imshow(img_raw[:,:,::-1])
            showImage = QImage(img_raw.data, img_raw.shape[1], img_raw.shape[0], QImage.Format_RGB888)
            # showImage = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGBA)
            self.show.setPixmap(QPixmap.fromImage(showImage))
            self.show.setScaledContents(True)
            cv2.waitKey(1)
        cv2.destroyAllWindows()

    def run_on_video(self, Net, conf_thresh=0.5):
        parser = argparse.ArgumentParser(description="Face Mask Detection")
        parser.add_argument('--proto', type=str, default='models/face_mask_detection.prototxt', help='prototxt path')
        parser.add_argument('--model', type=str, default='models/face_mask_detection.caffemodel', help='model path')
        parser.add_argument('--video-path', type=str, default='0', help='path to your video, `0` means to use camera.')
        # parser.add_argument('--hdf5', type=str, help='keras hdf5 file')
        args = parser.parse_args()
        Net = cv2.dnn.readNet(args.model, args.proto)
        video_path = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "./", "MP4 Files (*.mp4)")[0]
        self.cap = cv2.VideoCapture(video_path)
        width = 1000
        height = 1300
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        if not self.cap.isOpened():
            raise ValueError("Video open failed.")
            return
        status = True
        while status:
            status, img_raw = self.cap.read()
            if not status:
                # print("Done processing !!!")
                self.cap.release()
                break
            img_raw = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
            img_raw = opencv_dnn_infer.inference(Net, img_raw, target_shape=(260, 260), conf_thresh=conf_thresh)
            # cv2.imshow(img_raw[:,:,::-1])
            showImage = QImage(img_raw.data, img_raw.shape[1], img_raw.shape[0], QImage.Format_RGB888)
            # showImage = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGBA)
            self.show.setPixmap(QPixmap.fromImage(showImage))
            self.show.setScaledContents(True)
            cv2.waitKey(1)
        cv2.destroyAllWindows()

    # 槽函数
    def run_on_video1(self, Net, conf_thresh=0.5):
        parser = argparse.ArgumentParser(description="Face Mask Detection")
        parser.add_argument('--proto', type=str, default='models/face_mask_detection.prototxt', help='prototxt path')
        parser.add_argument('--model', type=str, default='models/face_mask_detection.caffemodel', help='model path')
        parser.add_argument('--video-path', type=str, default='0', help='path to your video, `0` means to use camera.')
        # parser.add_argument('--hdf5', type=str, help='keras hdf5 file')
        args = parser.parse_args()
        Net = cv2.dnn.readNet(args.model, args.proto)
        video_path = 0
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            raise ValueError("Video open failed.")
            return
        status = True
        while status:
            status, img_raw = self.cap.read()
            if not status:
                # print("Done processing !!!")
                self.cap.release()
                break
            img_raw = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
            img_raw = opencv_dnn_infer.inference(Net, img_raw, target_shape=(260, 260), conf_thresh=conf_thresh)
            # cv2.imshow(img_raw[:,:,::-1])
            showImage = QImage(img_raw.data, img_raw.shape[1], img_raw.shape[0], QImage.Format_RGB888)
            # showImage = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGBA)
            self.show.setPixmap(QPixmap.fromImage(showImage))
            self.show.setScaledContents(True)
            cv2.waitKey(1)
        cv2.destroyAllWindows()

    def run_on_video2(self, Net, conf_thresh=0.5):
        parser = argparse.ArgumentParser(description="Face Mask Detection")
        parser.add_argument('--proto', type=str, default='models/face_mask_detection.prototxt', help='prototxt path')
        parser.add_argument('--model', type=str, default='models/face_mask_detection.caffemodel', help='model path')
        parser.add_argument('--video-path', type=str, default='0', help='path to your video, `0` means to use camera.')
        # parser.add_argument('--hdf5', type=str, help='keras hdf5 file')
        args = parser.parse_args()
        Net = cv2.dnn.readNet(args.model, args.proto)
        video_path = args.video_path
        if (video_path != '0'):
            self.cap = cv2.VideoCapture(video_path)
            if not self.cap.isOpened():
                raise ValueError("Video open failed.")
                return
            status = True
            while status:
                status, img_raw = self.cap.read()
                if not status:
                    # print("Done processing !!!")
                    self.cap.release()
                    break
                img_raw = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
                img_raw = opencv_dnn_infer.inference(Net, img_raw, target_shape=(260, 260), conf_thresh=conf_thresh)
                # cv2.imshow(img_raw[:,:,::-1])
                showImage = QImage(img_raw.data, img_raw.shape[1], img_raw.shape[0], QImage.Format_RGB888)
                self.show.setPixmap(QPixmap.fromImage(showImage))
                cv2.waitKey(1)
            cv2.destroyAllWindows()

    def shut_video(self):
        self.cap.release()  # 释放视频流
        self.show.clear()  # 清空视频显示区域
        cv2.destroyAllWindows()


import icon
