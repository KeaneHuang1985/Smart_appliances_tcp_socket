# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python_code\temp\Smart_appliances_tcp_socket\UI\MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 831)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_Time = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Time.sizePolicy().hasHeightForWidth())
        self.label_Time.setSizePolicy(sizePolicy)
        self.label_Time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Time.setObjectName("label_Time")
        self.gridLayout.addWidget(self.label_Time, 0, 0, 1, 1)
        self.btn_connect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connect.setObjectName("btn_connect")
        self.gridLayout.addWidget(self.btn_connect, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setObjectName("btn_close")
        self.gridLayout.addWidget(self.btn_close, 5, 0, 1, 1)
        self.label_tcp_socket_state = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tcp_socket_state.sizePolicy().hasHeightForWidth())
        self.label_tcp_socket_state.setSizePolicy(sizePolicy)
        self.label_tcp_socket_state.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tcp_socket_state.setObjectName("label_tcp_socket_state")
        self.gridLayout.addWidget(self.label_tcp_socket_state, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.GB_Commom = QtWidgets.QGroupBox(self.centralwidget)
        self.GB_Commom.setEnabled(False)
        self.GB_Commom.setAlignment(QtCore.Qt.AlignCenter)
        self.GB_Commom.setObjectName("GB_Commom")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.GB_Commom)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.GB_Commom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btn_read_list = QtWidgets.QPushButton(self.groupBox)
        self.btn_read_list.setObjectName("btn_read_list")
        self.verticalLayout_7.addWidget(self.btn_read_list)
        self.cb_Generated_id = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_Generated_id.sizePolicy().hasHeightForWidth())
        self.cb_Generated_id.setSizePolicy(sizePolicy)
        self.cb_Generated_id.setMaxCount(30)
        self.cb_Generated_id.setObjectName("cb_Generated_id")
        self.verticalLayout_7.addWidget(self.cb_Generated_id)
        self.label_type = QtWidgets.QLabel(self.groupBox)
        self.label_type.setAlignment(QtCore.Qt.AlignCenter)
        self.label_type.setObjectName("label_type")
        self.verticalLayout_7.addWidget(self.label_type)
        self.label_mac = QtWidgets.QLabel(self.groupBox)
        self.label_mac.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mac.setObjectName("label_mac")
        self.verticalLayout_7.addWidget(self.label_mac)
        self.label_targetid = QtWidgets.QLabel(self.groupBox)
        self.label_targetid.setAlignment(QtCore.Qt.AlignCenter)
        self.label_targetid.setObjectName("label_targetid")
        self.verticalLayout_7.addWidget(self.label_targetid)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(self.GB_Commom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.spinBox_LB_Count = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_LB_Count.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_LB_Count.setMinimum(1)
        self.spinBox_LB_Count.setMaximum(9999)
        self.spinBox_LB_Count.setProperty("value", 1)
        self.spinBox_LB_Count.setObjectName("spinBox_LB_Count")
        self.verticalLayout_8.addWidget(self.spinBox_LB_Count)
        self.btn_auto_LB_Switch = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_auto_LB_Switch.setObjectName("btn_auto_LB_Switch")
        self.verticalLayout_8.addWidget(self.btn_auto_LB_Switch)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.btn_ac_find = QtWidgets.QPushButton(self.GB_Commom)
        self.btn_ac_find.setObjectName("btn_ac_find")
        self.verticalLayout.addWidget(self.btn_ac_find)
        self.btn_ota_available = QtWidgets.QPushButton(self.GB_Commom)
        self.btn_ota_available.setObjectName("btn_ota_available")
        self.verticalLayout.addWidget(self.btn_ota_available)
        self.btn_force_read_all = QtWidgets.QPushButton(self.GB_Commom)
        self.btn_force_read_all.setObjectName("btn_force_read_all")
        self.verticalLayout.addWidget(self.btn_force_read_all)
        self.btn_start_rssi_scan = QtWidgets.QPushButton(self.GB_Commom)
        self.btn_start_rssi_scan.setObjectName("btn_start_rssi_scan")
        self.verticalLayout.addWidget(self.btn_start_rssi_scan)
        self.GB_Setting = QtWidgets.QGroupBox(self.GB_Commom)
        self.GB_Setting.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GB_Setting.sizePolicy().hasHeightForWidth())
        self.GB_Setting.setSizePolicy(sizePolicy)
        self.GB_Setting.setObjectName("GB_Setting")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.GB_Setting)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.GB_Setting)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.lineEdit_Generated = QtWidgets.QLineEdit(self.GB_Setting)
        self.lineEdit_Generated.setMaxLength(22)
        self.lineEdit_Generated.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Generated.setObjectName("lineEdit_Generated")
        self.verticalLayout_2.addWidget(self.lineEdit_Generated)
        self.label_2 = QtWidgets.QLabel(self.GB_Setting)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_onboard_mac = QtWidgets.QLineEdit(self.GB_Setting)
        self.lineEdit_onboard_mac.setMaxLength(12)
        self.lineEdit_onboard_mac.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_onboard_mac.setObjectName("lineEdit_onboard_mac")
        self.verticalLayout_2.addWidget(self.lineEdit_onboard_mac)
        self.label_5 = QtWidgets.QLabel(self.GB_Setting)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.lineEdit_Report_interval = QtWidgets.QLineEdit(self.GB_Setting)
        self.lineEdit_Report_interval.setMaxLength(3)
        self.lineEdit_Report_interval.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Report_interval.setObjectName("lineEdit_Report_interval")
        self.verticalLayout_2.addWidget(self.lineEdit_Report_interval)
        self.btn_add_dev = QtWidgets.QPushButton(self.GB_Setting)
        self.btn_add_dev.setObjectName("btn_add_dev")
        self.verticalLayout_2.addWidget(self.btn_add_dev)
        self.btn_remove_dev = QtWidgets.QPushButton(self.GB_Setting)
        self.btn_remove_dev.setObjectName("btn_remove_dev")
        self.verticalLayout_2.addWidget(self.btn_remove_dev)
        self.verticalLayout.addWidget(self.GB_Setting)
        self.horizontalLayout.addWidget(self.GB_Commom)
        self.GB_SP = QtWidgets.QGroupBox(self.centralwidget)
        self.GB_SP.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GB_SP.sizePolicy().hasHeightForWidth())
        self.GB_SP.setSizePolicy(sizePolicy)
        self.GB_SP.setObjectName("GB_SP")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.GB_SP)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_sp_on = QtWidgets.QPushButton(self.GB_SP)
        self.btn_sp_on.setObjectName("btn_sp_on")
        self.verticalLayout_3.addWidget(self.btn_sp_on)
        self.btn_sp_off = QtWidgets.QPushButton(self.GB_SP)
        self.btn_sp_off.setObjectName("btn_sp_off")
        self.verticalLayout_3.addWidget(self.btn_sp_off)
        self.label_13 = QtWidgets.QLabel(self.GB_SP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setTextFormat(QtCore.Qt.PlainText)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.spinBox_sp_boiler_value = QtWidgets.QSpinBox(self.GB_SP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_sp_boiler_value.sizePolicy().hasHeightForWidth())
        self.spinBox_sp_boiler_value.setSizePolicy(sizePolicy)
        self.spinBox_sp_boiler_value.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_sp_boiler_value.setObjectName("spinBox_sp_boiler_value")
        self.verticalLayout_3.addWidget(self.spinBox_sp_boiler_value)
        self.btn_sp_boiler_auot_Switch = QtWidgets.QPushButton(self.GB_SP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sp_boiler_auot_Switch.sizePolicy().hasHeightForWidth())
        self.btn_sp_boiler_auot_Switch.setSizePolicy(sizePolicy)
        self.btn_sp_boiler_auot_Switch.setObjectName("btn_sp_boiler_auot_Switch")
        self.verticalLayout_3.addWidget(self.btn_sp_boiler_auot_Switch)
        self.groupBox_2 = QtWidgets.QGroupBox(self.GB_SP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.spinBox_sp_power = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_sp_power.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_sp_power.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_sp_power.setMaximum(500)
        self.spinBox_sp_power.setObjectName("spinBox_sp_power")
        self.verticalLayout_4.addWidget(self.spinBox_sp_power)
        self.cb_sp_enable = QtWidgets.QCheckBox(self.groupBox_2)
        self.cb_sp_enable.setObjectName("cb_sp_enable")
        self.verticalLayout_4.addWidget(self.cb_sp_enable)
        self.btn_SP_OPC = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_SP_OPC.setObjectName("btn_SP_OPC")
        self.verticalLayout_4.addWidget(self.btn_SP_OPC)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.GB_SP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cb_Action = QtWidgets.QCheckBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_Action.sizePolicy().hasHeightForWidth())
        self.cb_Action.setSizePolicy(sizePolicy)
        self.cb_Action.setObjectName("cb_Action")
        self.verticalLayout_6.addWidget(self.cb_Action)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.spinBox_tx = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_tx.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_tx.setMaximum(999999)
        self.spinBox_tx.setObjectName("spinBox_tx")
        self.verticalLayout_5.addWidget(self.spinBox_tx)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.spinBox_rx = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_rx.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_rx.setMaximum(999999)
        self.spinBox_rx.setObjectName("spinBox_rx")
        self.verticalLayout_5.addWidget(self.spinBox_rx)
        self.btn_set_interval = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_set_interval.setObjectName("btn_set_interval")
        self.verticalLayout_5.addWidget(self.btn_set_interval)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout.addWidget(self.GB_SP)
        self.GB_LB = QtWidgets.QGroupBox(self.centralwidget)
        self.GB_LB.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GB_LB.sizePolicy().hasHeightForWidth())
        self.GB_LB.setSizePolicy(sizePolicy)
        self.GB_LB.setObjectName("GB_LB")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.GB_LB)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_10 = QtWidgets.QLabel(self.GB_LB)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)
        self.dial_br = QtWidgets.QDial(self.GB_LB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial_br.sizePolicy().hasHeightForWidth())
        self.dial_br.setSizePolicy(sizePolicy)
        self.dial_br.setMinimum(0)
        self.dial_br.setMaximum(255)
        self.dial_br.setProperty("value", 50)
        self.dial_br.setObjectName("dial_br")
        self.gridLayout_5.addWidget(self.dial_br, 8, 0, 1, 1)
        self.btn_lb_white_brghtness = QtWidgets.QPushButton(self.GB_LB)
        self.btn_lb_white_brghtness.setObjectName("btn_lb_white_brghtness")
        self.gridLayout_5.addWidget(self.btn_lb_white_brghtness, 9, 0, 1, 1)
        self.label_red = QtWidgets.QLabel(self.GB_LB)
        self.label_red.setAlignment(QtCore.Qt.AlignCenter)
        self.label_red.setObjectName("label_red")
        self.gridLayout_5.addWidget(self.label_red, 10, 0, 1, 1)
        self.label_white_br = QtWidgets.QLabel(self.GB_LB)
        self.label_white_br.setAlignment(QtCore.Qt.AlignCenter)
        self.label_white_br.setObjectName("label_white_br")
        self.gridLayout_5.addWidget(self.label_white_br, 0, 1, 1, 1)
        self.lb_pb_brightness = QtWidgets.QProgressBar(self.GB_LB)
        self.lb_pb_brightness.setStyleSheet("")
        self.lb_pb_brightness.setMinimum(0)
        self.lb_pb_brightness.setMaximum(255)
        self.lb_pb_brightness.setProperty("value", 50)
        self.lb_pb_brightness.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_pb_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.lb_pb_brightness.setObjectName("lb_pb_brightness")
        self.gridLayout_5.addWidget(self.lb_pb_brightness, 2, 0, 1, 1)
        self.label_red_val = QtWidgets.QLabel(self.GB_LB)
        self.label_red_val.setAlignment(QtCore.Qt.AlignCenter)
        self.label_red_val.setObjectName("label_red_val")
        self.gridLayout_5.addWidget(self.label_red_val, 10, 1, 1, 1)
        self.dial_red = QtWidgets.QDial(self.GB_LB)
        self.dial_red.setMinimum(0)
        self.dial_red.setMaximum(255)
        self.dial_red.setObjectName("dial_red")
        self.gridLayout_5.addWidget(self.dial_red, 11, 0, 1, 1)
        self.label_green = QtWidgets.QLabel(self.GB_LB)
        self.label_green.setObjectName("label_green")
        self.gridLayout_5.addWidget(self.label_green, 12, 0, 1, 1)
        self.btn_auto_rgb_br_test = QtWidgets.QPushButton(self.GB_LB)
        self.btn_auto_rgb_br_test.setObjectName("btn_auto_rgb_br_test")
        self.gridLayout_5.addWidget(self.btn_auto_rgb_br_test, 33, 0, 1, 1)
        self.label_blue = QtWidgets.QLabel(self.GB_LB)
        self.label_blue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_blue.setObjectName("label_blue")
        self.gridLayout_5.addWidget(self.label_blue, 14, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.GB_LB)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 22, 0, 1, 1)
        self.dial_rgb_br = QtWidgets.QDial(self.GB_LB)
        self.dial_rgb_br.setMaximum(100)
        self.dial_rgb_br.setProperty("value", 50)
        self.dial_rgb_br.setObjectName("dial_rgb_br")
        self.gridLayout_5.addWidget(self.dial_rgb_br, 24, 0, 1, 1)
        self.label_blue_val = QtWidgets.QLabel(self.GB_LB)
        self.label_blue_val.setAlignment(QtCore.Qt.AlignCenter)
        self.label_blue_val.setObjectName("label_blue_val")
        self.gridLayout_5.addWidget(self.label_blue_val, 14, 1, 1, 1)
        self.btn_lb_rgb_light_setting = QtWidgets.QPushButton(self.GB_LB)
        self.btn_lb_rgb_light_setting.setObjectName("btn_lb_rgb_light_setting")
        self.gridLayout_5.addWidget(self.btn_lb_rgb_light_setting, 20, 0, 1, 1)
        self.btn_lb_rgb_brightness = QtWidgets.QPushButton(self.GB_LB)
        self.btn_lb_rgb_brightness.setObjectName("btn_lb_rgb_brightness")
        self.gridLayout_5.addWidget(self.btn_lb_rgb_brightness, 25, 0, 1, 1)
        self.btn_lb_light_on = QtWidgets.QPushButton(self.GB_LB)
        self.btn_lb_light_on.setObjectName("btn_lb_light_on")
        self.gridLayout_5.addWidget(self.btn_lb_light_on, 30, 0, 1, 1)
        self.label_green_val = QtWidgets.QLabel(self.GB_LB)
        self.label_green_val.setAlignment(QtCore.Qt.AlignCenter)
        self.label_green_val.setObjectName("label_green_val")
        self.gridLayout_5.addWidget(self.label_green_val, 12, 1, 1, 1)
        self.dial_green = QtWidgets.QDial(self.GB_LB)
        self.dial_green.setMaximum(255)
        self.dial_green.setObjectName("dial_green")
        self.gridLayout_5.addWidget(self.dial_green, 13, 0, 1, 1)
        self.dial_blue = QtWidgets.QDial(self.GB_LB)
        self.dial_blue.setMaximum(255)
        self.dial_blue.setObjectName("dial_blue")
        self.gridLayout_5.addWidget(self.dial_blue, 15, 0, 1, 1)
        self.lb_pb_rgbbrightness = QtWidgets.QProgressBar(self.GB_LB)
        self.lb_pb_rgbbrightness.setProperty("value", 50)
        self.lb_pb_rgbbrightness.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_pb_rgbbrightness.setObjectName("lb_pb_rgbbrightness")
        self.gridLayout_5.addWidget(self.lb_pb_rgbbrightness, 23, 0, 1, 1)
        self.btn_auto_rgb_test = QtWidgets.QPushButton(self.GB_LB)
        self.btn_auto_rgb_test.setObjectName("btn_auto_rgb_test")
        self.gridLayout_5.addWidget(self.btn_auto_rgb_test, 32, 0, 1, 1)
        self.btn_lb_light_off = QtWidgets.QPushButton(self.GB_LB)
        self.btn_lb_light_off.setObjectName("btn_lb_light_off")
        self.gridLayout_5.addWidget(self.btn_lb_light_off, 31, 0, 1, 1)
        self.label_10.raise_()
        self.btn_lb_light_on.raise_()
        self.btn_lb_rgb_light_setting.raise_()
        self.label_red.raise_()
        self.label_green.raise_()
        self.label_blue.raise_()
        self.label_red_val.raise_()
        self.label_green_val.raise_()
        self.label_blue_val.raise_()
        self.lb_pb_brightness.raise_()
        self.dial_br.raise_()
        self.dial_red.raise_()
        self.dial_green.raise_()
        self.dial_blue.raise_()
        self.btn_lb_white_brghtness.raise_()
        self.dial_rgb_br.raise_()
        self.lb_pb_rgbbrightness.raise_()
        self.label_9.raise_()
        self.btn_lb_rgb_brightness.raise_()
        self.label_white_br.raise_()
        self.btn_auto_rgb_test.raise_()
        self.btn_auto_rgb_br_test.raise_()
        self.btn_lb_light_off.raise_()
        self.horizontalLayout.addWidget(self.GB_LB)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_send = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_send.setObjectName("textEdit_send")
        self.gridLayout_2.addWidget(self.textEdit_send, 3, 0, 1, 1)
        self.btn_send_json = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_json.setEnabled(False)
        self.btn_send_json.setObjectName("btn_send_json")
        self.gridLayout_2.addWidget(self.btn_send_json, 4, 0, 1, 1)
        self.textEdit_rec = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_rec.setEnabled(True)
        self.textEdit_rec.setObjectName("textEdit_rec")
        self.gridLayout_2.addWidget(self.textEdit_rec, 3, 1, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout_2.addWidget(self.btn_clear, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TCP_Socket"))
        self.label_Time.setText(_translate("MainWindow", "Time"))
        self.btn_connect.setText(_translate("MainWindow", "Connect"))
        self.lineEdit.setInputMask(_translate("MainWindow", "000.000.000.000"))
        self.lineEdit.setText(_translate("MainWindow", "192.168.137.0"))
        self.btn_close.setText(_translate("MainWindow", "Disconnect"))
        self.label_tcp_socket_state.setText(_translate("MainWindow", "Disconnect"))
        self.label.setText(_translate("MainWindow", "TCP Socket State"))
        self.GB_Commom.setTitle(_translate("MainWindow", "Commom"))
        self.groupBox.setTitle(_translate("MainWindow", "Select Devices Info"))
        self.btn_read_list.setText(_translate("MainWindow", "Read List"))
        self.label_type.setText(_translate("MainWindow", "null"))
        self.label_mac.setText(_translate("MainWindow", "null"))
        self.label_targetid.setText(_translate("MainWindow", "null"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Light Bulb Auto Test"))
        self.label_12.setText(_translate("MainWindow", "Auto Test Count"))
        self.btn_auto_LB_Switch.setText(_translate("MainWindow", "Auto Switch Test"))
        self.btn_ac_find.setText(_translate("MainWindow", "Find AC Device"))
        self.btn_ota_available.setText(_translate("MainWindow", "OTA Available"))
        self.btn_force_read_all.setText(_translate("MainWindow", "Force Read All"))
        self.btn_start_rssi_scan.setText(_translate("MainWindow", "RSSI(AC)"))
        self.GB_Setting.setTitle(_translate("MainWindow", "Add Devces"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Generated ID</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Onboard Mac"))
        self.label_5.setText(_translate("MainWindow", "Report Interval"))
        self.btn_add_dev.setText(_translate("MainWindow", "Add Devices"))
        self.btn_remove_dev.setText(_translate("MainWindow", "Remove_devices"))
        self.GB_SP.setTitle(_translate("MainWindow", "SP / Boiler"))
        self.btn_sp_on.setText(_translate("MainWindow", "General_ON"))
        self.btn_sp_off.setText(_translate("MainWindow", "General OFF"))
        self.label_13.setText(_translate("MainWindow", "Auto Test Count"))
        self.btn_sp_boiler_auot_Switch.setText(_translate("MainWindow", "Auto_Switch_Test"))
        self.groupBox_2.setTitle(_translate("MainWindow", "SP OPC Control"))
        self.label_11.setText(_translate("MainWindow", "POWER THRESHOLD"))
        self.cb_sp_enable.setText(_translate("MainWindow", "OPC Enable"))
        self.btn_SP_OPC.setText(_translate("MainWindow", "SP OPC"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Report Interval"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Guard"))
        self.cb_Action.setText(_translate("MainWindow", "Action"))
        self.label_7.setText(_translate("MainWindow", "Tx interval"))
        self.label_8.setText(_translate("MainWindow", "Wakeup interval"))
        self.btn_set_interval.setText(_translate("MainWindow", "Report interval"))
        self.GB_LB.setTitle(_translate("MainWindow", "LB"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">White Brightness</span></p></body></html>"))
        self.btn_lb_white_brghtness.setText(_translate("MainWindow", "White Brghtness"))
        self.label_red.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Red</span></p></body></html>"))
        self.label_white_br.setText(_translate("MainWindow", "50"))
        self.label_red_val.setText(_translate("MainWindow", "0"))
        self.label_green.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Green</span></p></body></html>"))
        self.btn_auto_rgb_br_test.setText(_translate("MainWindow", "Auto RGB Brightness Test"))
        self.label_blue.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">Blue</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "RGB Brightness"))
        self.label_blue_val.setText(_translate("MainWindow", "0"))
        self.btn_lb_rgb_light_setting.setText(_translate("MainWindow", "RGB Setting "))
        self.btn_lb_rgb_brightness.setText(_translate("MainWindow", "RGB Brightness "))
        self.btn_lb_light_on.setText(_translate("MainWindow", "Light ON"))
        self.label_green_val.setText(_translate("MainWindow", "0"))
        self.btn_auto_rgb_test.setText(_translate("MainWindow", "Auto RGB light Test"))
        self.btn_lb_light_off.setText(_translate("MainWindow", "Light OFF"))
        self.btn_send_json.setText(_translate("MainWindow", "Send Msg"))
        self.btn_clear.setText(_translate("MainWindow", "Clear Msg"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Receive Json Format:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Send Json Format :</span></p></body></html>"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
