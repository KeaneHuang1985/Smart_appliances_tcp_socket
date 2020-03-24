# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python_code\tcp_client\UI\MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_connect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connect.setObjectName("btn_connect")
        self.gridLayout.addWidget(self.btn_connect, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setObjectName("btn_close")
        self.gridLayout.addWidget(self.btn_close, 5, 0, 1, 1)
        self.label_tcp_socket_state = QtWidgets.QLabel(self.centralwidget)
        self.label_tcp_socket_state.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tcp_socket_state.setObjectName("label_tcp_socket_state")
        self.gridLayout.addWidget(self.label_tcp_socket_state, 2, 0, 1, 1)
        self.label_Time = QtWidgets.QLabel(self.centralwidget)
        self.label_Time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Time.setObjectName("label_Time")
        self.gridLayout.addWidget(self.label_Time, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.GB_Commom = QtWidgets.QGroupBox(self.centralwidget)
        self.GB_Commom.setEnabled(False)
        self.GB_Commom.setObjectName("GB_Commom")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.GB_Commom)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_read_mesh_dev = QtWidgets.QPushButton(self.GB_Commom)
        self.btn_read_mesh_dev.setEnabled(False)
        self.btn_read_mesh_dev.setObjectName("btn_read_mesh_dev")
        self.verticalLayout.addWidget(self.btn_read_mesh_dev)
        self.cb_Generated_id = QtWidgets.QComboBox(self.GB_Commom)
        self.cb_Generated_id.setObjectName("cb_Generated_id")
        self.verticalLayout.addWidget(self.cb_Generated_id)
        self.btn_ac_find = QtWidgets.QPushButton(self.GB_Commom)
        self.btn_ac_find.setObjectName("btn_ac_find")
        self.verticalLayout.addWidget(self.btn_ac_find)
        self.btn_ota_available = QtWidgets.QPushButton(self.GB_Commom)
        self.btn_ota_available.setObjectName("btn_ota_available")
        self.verticalLayout.addWidget(self.btn_ota_available)
        self.btn_ready_for_ota = QtWidgets.QPushButton(self.GB_Commom)
        self.btn_ready_for_ota.setObjectName("btn_ready_for_ota")
        self.verticalLayout.addWidget(self.btn_ready_for_ota)
        self.btn_force_read_all = QtWidgets.QPushButton(self.GB_Commom)
        self.btn_force_read_all.setObjectName("btn_force_read_all")
        self.verticalLayout.addWidget(self.btn_force_read_all)
        self.btn_start_rssi_scan = QtWidgets.QPushButton(self.GB_Commom)
        self.btn_start_rssi_scan.setObjectName("btn_start_rssi_scan")
        self.verticalLayout.addWidget(self.btn_start_rssi_scan)
        self.btn_send_json = QtWidgets.QPushButton(self.GB_Commom)
        self.btn_send_json.setEnabled(False)
        self.btn_send_json.setObjectName("btn_send_json")
        self.verticalLayout.addWidget(self.btn_send_json)
        self.groupBox = QtWidgets.QGroupBox(self.GB_Commom)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.lineEdit_Generated = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Generated.setMaxLength(22)
        self.lineEdit_Generated.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Generated.setObjectName("lineEdit_Generated")
        self.verticalLayout_2.addWidget(self.lineEdit_Generated)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_onboard_mac = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_onboard_mac.setMaxLength(12)
        self.lineEdit_onboard_mac.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_onboard_mac.setObjectName("lineEdit_onboard_mac")
        self.verticalLayout_2.addWidget(self.lineEdit_onboard_mac)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.lineEdit_Report_interval = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Report_interval.setMaxLength(3)
        self.lineEdit_Report_interval.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Report_interval.setObjectName("lineEdit_Report_interval")
        self.verticalLayout_2.addWidget(self.lineEdit_Report_interval)
        self.btn_add_dev = QtWidgets.QPushButton(self.groupBox)
        self.btn_add_dev.setObjectName("btn_add_dev")
        self.verticalLayout_2.addWidget(self.btn_add_dev)
        self.btn_remove_dev = QtWidgets.QPushButton(self.groupBox)
        self.btn_remove_dev.setObjectName("btn_remove_dev")
        self.verticalLayout_2.addWidget(self.btn_remove_dev)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.GB_Commom)
        self.GB_LB = QtWidgets.QGroupBox(self.centralwidget)
        self.GB_LB.setEnabled(False)
        self.GB_LB.setObjectName("GB_LB")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.GB_LB)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_lb_white_brghtness = QtWidgets.QPushButton(self.GB_LB)
        self.btn_lb_white_brghtness.setObjectName("btn_lb_white_brghtness")
        self.gridLayout_5.addWidget(self.btn_lb_white_brghtness, 18, 0, 1, 1)
        self.btn_lb_rgb_brightness = QtWidgets.QPushButton(self.GB_LB)
        self.btn_lb_rgb_brightness.setObjectName("btn_lb_rgb_brightness")
        self.gridLayout_5.addWidget(self.btn_lb_rgb_brightness, 17, 0, 1, 1)
        self.btn_lb_light_on = QtWidgets.QPushButton(self.GB_LB)
        self.btn_lb_light_on.setObjectName("btn_lb_light_on")
        self.gridLayout_5.addWidget(self.btn_lb_light_on, 19, 0, 1, 1)
        self.label_blue = QtWidgets.QLabel(self.GB_LB)
        self.label_blue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_blue.setObjectName("label_blue")
        self.gridLayout_5.addWidget(self.label_blue, 9, 0, 1, 1)
        self.lb_hz_brightness = QtWidgets.QSlider(self.GB_LB)
        self.lb_hz_brightness.setMaximum(255)
        self.lb_hz_brightness.setSingleStep(0)
        self.lb_hz_brightness.setProperty("value", 50)
        self.lb_hz_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.lb_hz_brightness.setObjectName("lb_hz_brightness")
        self.gridLayout_5.addWidget(self.lb_hz_brightness, 1, 0, 1, 1)
        self.lb_hz_red_color = QtWidgets.QSlider(self.GB_LB)
        self.lb_hz_red_color.setMaximum(255)
        self.lb_hz_red_color.setOrientation(QtCore.Qt.Horizontal)
        self.lb_hz_red_color.setObjectName("lb_hz_red_color")
        self.gridLayout_5.addWidget(self.lb_hz_red_color, 6, 0, 1, 1)
        self.btn_lb_rgb_light_setting = QtWidgets.QPushButton(self.GB_LB)
        self.btn_lb_rgb_light_setting.setObjectName("btn_lb_rgb_light_setting")
        self.gridLayout_5.addWidget(self.btn_lb_rgb_light_setting, 16, 0, 1, 1)
        self.label_green = QtWidgets.QLabel(self.GB_LB)
        self.label_green.setObjectName("label_green")
        self.gridLayout_5.addWidget(self.label_green, 7, 0, 1, 1)
        self.lb_hz_green_color = QtWidgets.QSlider(self.GB_LB)
        self.lb_hz_green_color.setMaximum(255)
        self.lb_hz_green_color.setOrientation(QtCore.Qt.Horizontal)
        self.lb_hz_green_color.setObjectName("lb_hz_green_color")
        self.gridLayout_5.addWidget(self.lb_hz_green_color, 8, 0, 1, 1)
        self.btn_lb_light_off = QtWidgets.QPushButton(self.GB_LB)
        self.btn_lb_light_off.setObjectName("btn_lb_light_off")
        self.gridLayout_5.addWidget(self.btn_lb_light_off, 20, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.GB_LB)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)
        self.lb_hz_blue_color = QtWidgets.QSlider(self.GB_LB)
        self.lb_hz_blue_color.setMaximum(255)
        self.lb_hz_blue_color.setOrientation(QtCore.Qt.Horizontal)
        self.lb_hz_blue_color.setObjectName("lb_hz_blue_color")
        self.gridLayout_5.addWidget(self.lb_hz_blue_color, 15, 0, 1, 2)
        self.lb_pb_brightness = QtWidgets.QProgressBar(self.GB_LB)
        self.lb_pb_brightness.setMaximum(255)
        self.lb_pb_brightness.setProperty("value", 50)
        self.lb_pb_brightness.setObjectName("lb_pb_brightness")
        self.gridLayout_5.addWidget(self.lb_pb_brightness, 2, 0, 1, 2)
        self.label_red = QtWidgets.QLabel(self.GB_LB)
        self.label_red.setAlignment(QtCore.Qt.AlignCenter)
        self.label_red.setObjectName("label_red")
        self.gridLayout_5.addWidget(self.label_red, 5, 0, 1, 1)
        self.lb_hz_blue_color.raise_()
        self.label_10.raise_()
        self.btn_lb_light_on.raise_()
        self.btn_lb_rgb_light_setting.raise_()
        self.btn_lb_rgb_brightness.raise_()
        self.btn_lb_light_off.raise_()
        self.label_red.raise_()
        self.lb_hz_red_color.raise_()
        self.label_green.raise_()
        self.lb_hz_green_color.raise_()
        self.label_blue.raise_()
        self.lb_hz_brightness.raise_()
        self.lb_pb_brightness.raise_()
        self.btn_lb_white_brghtness.raise_()
        self.horizontalLayout.addWidget(self.GB_LB)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GB_SP = QtWidgets.QGroupBox(self.centralwidget)
        self.GB_SP.setEnabled(False)
        self.GB_SP.setObjectName("GB_SP")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.GB_SP)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_sp_on = QtWidgets.QPushButton(self.GB_SP)
        self.btn_sp_on.setObjectName("btn_sp_on")
        self.verticalLayout_3.addWidget(self.btn_sp_on)
        self.btn_sp_off = QtWidgets.QPushButton(self.GB_SP)
        self.btn_sp_off.setObjectName("btn_sp_off")
        self.verticalLayout_3.addWidget(self.btn_sp_off)
        self.groupBox_2 = QtWidgets.QGroupBox(self.GB_SP)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rb_sp_enable = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_sp_enable.setObjectName("rb_sp_enable")
        self.verticalLayout_4.addWidget(self.rb_sp_enable)
        self.rb_sp_disable = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_sp_disable.setObjectName("rb_sp_disable")
        self.verticalLayout_4.addWidget(self.rb_sp_disable)
        self.btn_SP_OPC = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_SP_OPC.setObjectName("btn_SP_OPC")
        self.verticalLayout_4.addWidget(self.btn_SP_OPC)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.gridLayout_3.addWidget(self.GB_SP, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)
        self.textEdit_send = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_send.setObjectName("textEdit_send")
        self.gridLayout_2.addWidget(self.textEdit_send, 3, 0, 1, 1)
        self.textEdit_rec = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_rec.setEnabled(True)
        self.textEdit_rec.setObjectName("textEdit_rec")
        self.gridLayout_2.addWidget(self.textEdit_rec, 3, 1, 1, 1)
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
        self.btn_connect.setText(_translate("MainWindow", "Connect"))
        self.lineEdit.setInputMask(_translate("MainWindow", "000.000.000.000"))
        self.label.setText(_translate("MainWindow", "TCP Socket State"))
        self.btn_close.setText(_translate("MainWindow", "Disconnect"))
        self.label_tcp_socket_state.setText(_translate("MainWindow", "Disconnect"))
        self.label_Time.setText(_translate("MainWindow", "Time"))
        self.GB_Commom.setTitle(_translate("MainWindow", "Commom"))
        self.btn_read_mesh_dev.setText(_translate("MainWindow", "Update Dev"))
        self.btn_ac_find.setText(_translate("MainWindow", "Find AC Device"))
        self.btn_ota_available.setText(_translate("MainWindow", "OTA Available"))
        self.btn_ready_for_ota.setText(_translate("MainWindow", "Ready For OTA"))
        self.btn_force_read_all.setText(_translate("MainWindow", "Force Read All"))
        self.btn_start_rssi_scan.setText(_translate("MainWindow", "RSSI(AC)"))
        self.btn_send_json.setText(_translate("MainWindow", "Send Json Format"))
        self.groupBox.setTitle(_translate("MainWindow", "Add Devces"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Generated ID</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Onboard Mac"))
        self.label_5.setText(_translate("MainWindow", "Report Interval"))
        self.btn_add_dev.setText(_translate("MainWindow", "Add Devices"))
        self.btn_remove_dev.setText(_translate("MainWindow", "Remove_devices"))
        self.GB_LB.setTitle(_translate("MainWindow", "LB"))
        self.btn_lb_white_brghtness.setText(_translate("MainWindow", "White Brghtness"))
        self.btn_lb_rgb_brightness.setText(_translate("MainWindow", "RGB Brightness "))
        self.btn_lb_light_on.setText(_translate("MainWindow", "Light ON"))
        self.label_blue.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">Blue</span></p></body></html>"))
        self.btn_lb_rgb_light_setting.setText(_translate("MainWindow", "RGB Setting "))
        self.label_green.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Green</span></p></body></html>"))
        self.btn_lb_light_off.setText(_translate("MainWindow", "Light OFF"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Brightness</span></p></body></html>"))
        self.label_red.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Red</span></p></body></html>"))
        self.GB_SP.setTitle(_translate("MainWindow", "SP / Boiler"))
        self.btn_sp_on.setText(_translate("MainWindow", "General_ON"))
        self.btn_sp_off.setText(_translate("MainWindow", "General OFF"))
        self.groupBox_2.setTitle(_translate("MainWindow", "SP OPC Control"))
        self.rb_sp_enable.setText(_translate("MainWindow", "SP OPC Enable"))
        self.rb_sp_disable.setText(_translate("MainWindow", "SP OPC disable"))
        self.btn_SP_OPC.setText(_translate("MainWindow", "SP OPC"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Send Json Format :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Receive Json Format:</span></p></body></html>"))
        self.actionAbout.setText(_translate("MainWindow", "About"))