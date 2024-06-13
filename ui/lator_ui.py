# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_kalkulator(object):
    def setupUi(self, kalkulator):
        if not kalkulator.objectName():
            kalkulator.setObjectName(u"kalkulator")
        kalkulator.resize(877, 653)
        kalkulator.setMinimumSize(QSize(600, 200))
        self.gridLayout = QGridLayout(kalkulator)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.frame = QFrame(kalkulator)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 200))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setPointSize(20)
        self.lineEdit.setFont(font1)
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font1)
        self.pushButton_11.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.pushButton_19 = QPushButton(self.frame_2)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setFont(font1)
        self.pushButton_19.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_19, 4, 2, 1, 2)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_17 = QPushButton(self.frame_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFont(font1)
        self.pushButton_17.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_17, 4, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_10, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.frame_2)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setFont(font1)
        self.pushButton_1.setFocusPolicy(Qt.NoFocus)
        self.pushButton_1.setAutoDefault(False)
        self.pushButton_1.setFlat(False)

        self.gridLayout_2.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font1)
        self.pushButton_12.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_12, 2, 3, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_8, 1, 3, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font1)
        self.pushButton_13.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_13, 3, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font1)
        self.pushButton_14.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_14, 3, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font1)
        self.pushButton_15.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_15, 3, 2, 1, 1)

        self.pushButton_16 = QPushButton(self.frame_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font1)
        self.pushButton_16.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_16, 3, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.frame_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font1)
        self.pushButton_18.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_18, 4, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)


        self.retranslateUi(kalkulator)

        self.pushButton_1.setDefault(False)


        QMetaObject.connectSlotsByName(kalkulator)
    # setupUi

    def retranslateUi(self, kalkulator):
        kalkulator.setWindowTitle(QCoreApplication.translate("kalkulator", u"lator", None))
        self.label.setText(QCoreApplication.translate("kalkulator", u"Kalkulator", None))
        self.pushButton_11.setText(QCoreApplication.translate("kalkulator", u"3", None))
        self.pushButton_19.setText(QCoreApplication.translate("kalkulator", u"=", None))
        self.pushButton_2.setText(QCoreApplication.translate("kalkulator", u"8", None))
        self.pushButton_3.setText(QCoreApplication.translate("kalkulator", u"9", None))
        self.pushButton_17.setText(QCoreApplication.translate("kalkulator", u"AC", None))
        self.pushButton_10.setText(QCoreApplication.translate("kalkulator", u"2", None))
        self.pushButton_6.setText(QCoreApplication.translate("kalkulator", u"5", None))
        self.pushButton_1.setText(QCoreApplication.translate("kalkulator", u"7", None))
        self.pushButton_7.setText(QCoreApplication.translate("kalkulator", u"6", None))
        self.pushButton_12.setText(QCoreApplication.translate("kalkulator", u"\u2212", None))
        self.pushButton_8.setText(QCoreApplication.translate("kalkulator", u"x", None))
        self.pushButton_13.setText(QCoreApplication.translate("kalkulator", u"0", None))
        self.pushButton_14.setText(QCoreApplication.translate("kalkulator", u"00", None))
        self.pushButton_15.setText(QCoreApplication.translate("kalkulator", u",", None))
        self.pushButton_16.setText(QCoreApplication.translate("kalkulator", u"+", None))
        self.pushButton_4.setText(QCoreApplication.translate("kalkulator", u"\u00F7", None))
        self.pushButton_5.setText(QCoreApplication.translate("kalkulator", u"4", None))
        self.pushButton_18.setText(QCoreApplication.translate("kalkulator", u"\u232b", None))
        self.pushButton_9.setText(QCoreApplication.translate("kalkulator", u"1", None))
    # retranslateUi

