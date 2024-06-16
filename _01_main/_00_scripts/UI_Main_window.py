# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import PyQt6.QtWidgets as QTW
import pandas as pd
from CustomTableModel import CustomTableModel, CustomTableView, CheckBoxDelegate


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 787)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 0, 1161, 741))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.grid_left = QtWidgets.QGridLayout()
        self.grid_left.setObjectName("grid_left")
        self.btn_save_left = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        self.btn_save_left.setObjectName("btn_save_left")
        self.grid_left.addWidget(self.btn_save_left, 3, 0, 1, 1)
        self.btn_delrow_left = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        self.btn_delrow_left.setObjectName("btn_delrow_left")
        self.grid_left.addWidget(self.btn_delrow_left, 1, 1, 1, 1)
        self.btn_cancel_left = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        self.btn_cancel_left.setObjectName("btn_cancel_left")
        self.grid_left.addWidget(self.btn_cancel_left, 3, 1, 1, 1)
        
        
        #Insert left table
        self.tbl_view_left = QTW.QTableView()
        self.tbl_left = CustomTableModel(pd.DataFrame())
        self.tbl_view_left.setModel(self.tbl_left)
        self.delegate_left = CheckBoxDelegate(self.tbl_view_left)
        self.tbl_view_left.setItemDelegate(self.delegate_left)
        self.grid_left.addWidget(self.tbl_view_left, 0, 0, 1, 2)
        
        # self.tbl_left = QtWidgets.QTableWidget(parent=self.gridLayoutWidget_5)
        # self.tbl_left.setObjectName("tbl_left")
        # self.tbl_left.setColumnCount(0)
        # self.tbl_left.setRowCount(0)
        # self.grid_left.addWidget(self.tbl_left, 0, 0, 1, 2)
        
        
        
        self.btn_addrow_left = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        self.btn_addrow_left.setObjectName("btn_addrow_left")
        self.grid_left.addWidget(self.btn_addrow_left, 1, 0, 1, 1)
        self.line_tbl_left = QtWidgets.QFrame(parent=self.gridLayoutWidget_5)
        self.line_tbl_left.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_tbl_left.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_tbl_left.setObjectName("line_tbl_left")
        self.grid_left.addWidget(self.line_tbl_left, 2, 0, 1, 2)
        self.gridLayout.addLayout(self.grid_left, 0, 0, 1, 1)
        self.grid_right = QtWidgets.QGridLayout()
        self.grid_right.setObjectName("grid_right")
        self.btn_addrow_right = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        self.btn_addrow_right.setObjectName("btn_addrow_right")
        self.grid_right.addWidget(self.btn_addrow_right, 1, 0, 1, 1)
        self.btn_delrow_right = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        self.btn_delrow_right.setObjectName("btn_delrow_right")
        self.grid_right.addWidget(self.btn_delrow_right, 1, 1, 1, 1)
        self.btn_save_right = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        self.btn_save_right.setObjectName("btn_save_right")
        self.grid_right.addWidget(self.btn_save_right, 3, 0, 1, 1)
        
        #Insert table right
        self.tbl_view_right = QTW.QTableView()
        self.tbl_right = CustomTableModel(pd.DataFrame())
        self.tbl_view_right.setModel(self.tbl_right)
        self.delegate_right = CheckBoxDelegate(self.tbl_view_right)
        self.tbl_view_right.setItemDelegate(self.delegate_right)
        self.grid_right.addWidget(self.tbl_view_right, 0, 0, 1, 2)
        
        # self.tbl_right = QtWidgets.QTableWidget(parent=self.gridLayoutWidget_5)
        # self.tbl_right.setObjectName("tbl_right")
        # self.tbl_right.setColumnCount(0)
        # self.tbl_right.setRowCount(0)
        # self.grid_right.addWidget(self.tbl_right, 0, 0, 1, 2)
        
        
        self.btn_cancel_right = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        self.btn_cancel_right.setObjectName("btn_cancel_right")
        self.grid_right.addWidget(self.btn_cancel_right, 3, 1, 1, 1)
        self.line_tbl_right = QtWidgets.QFrame(parent=self.gridLayoutWidget_5)
        self.line_tbl_right.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_tbl_right.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_tbl_right.setObjectName("line_tbl_right")
        self.grid_right.addWidget(self.line_tbl_right, 2, 0, 1, 2)
        self.gridLayout.addLayout(self.grid_right, 0, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.gridLayoutWidget_5)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_scdl = QtWidgets.QWidget()
        self.tab_scdl.setObjectName("tab_scdl")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.tab_scdl)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 261, 461))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.glayout_SCDL = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.glayout_SCDL.setContentsMargins(0, 0, 0, 0)
        self.glayout_SCDL.setObjectName("glayout_SCDL")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayout_SCDL.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayout_SCDL.addItem(spacerItem1, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=self.gridLayoutWidget_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.glayout_SCDL.addWidget(self.line_2, 7, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.gridLayoutWidget_4)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.glayout_SCDL.addWidget(self.line, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayout_SCDL.addItem(spacerItem2, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayout_SCDL.addItem(spacerItem3, 8, 0, 1, 1)
        self.glayout_pl_search = QtWidgets.QGridLayout()
        self.glayout_pl_search.setObjectName("glayout_pl_search")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.glayout_pl_search.addItem(spacerItem4, 1, 2, 4, 1)
        self.TxtEdit_pl_search = QtWidgets.QPlainTextEdit(parent=self.gridLayoutWidget_4)
        self.TxtEdit_pl_search.setObjectName("TxtEdit_pl_search")
        self.glayout_pl_search.addWidget(self.TxtEdit_pl_search, 5, 1, 1, 1)
        self.btn_pl_search = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.btn_pl_search.setObjectName("btn_pl_search")
        self.glayout_pl_search.addWidget(self.btn_pl_search, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayout_pl_search.addItem(spacerItem5, 6, 1, 1, 1)
        self.rbtn_pl_search_name = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_4)
        self.rbtn_pl_search_name.setObjectName("rbtn_pl_search_name")
        self.glayout_pl_search.addWidget(self.rbtn_pl_search_name, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.glayout_pl_search.addItem(spacerItem6, 1, 0, 4, 1)
        self.lbl_pl_search = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_pl_search.sizePolicy().hasHeightForWidth())
        self.lbl_pl_search.setSizePolicy(sizePolicy)
        self.lbl_pl_search.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_pl_search.setObjectName("lbl_pl_search")
        self.glayout_pl_search.addWidget(self.lbl_pl_search, 0, 0, 1, 3)
        self.rbtn_pl_search_key = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_4)
        self.rbtn_pl_search_key.setAutoExclusive(True)
        self.rbtn_pl_search_key.setObjectName("rbtn_pl_search_key")
        self.glayout_pl_search.addWidget(self.rbtn_pl_search_key, 4, 1, 1, 1)
        self.rbtn_pl_all = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_4)
        self.rbtn_pl_all.setChecked(True)
        self.rbtn_pl_all.setObjectName("rbtn_pl_all")
        self.glayout_pl_search.addWidget(self.rbtn_pl_all, 2, 1, 1, 1)
        self.glayout_pl_search.setColumnStretch(0, 1)
        self.glayout_pl_search.setColumnStretch(1, 30)
        self.glayout_pl_search.setColumnStretch(2, 1)
        self.glayout_pl_search.setRowStretch(0, 1)
        self.glayout_pl_search.setRowStretch(1, 1)
        self.glayout_pl_search.setRowStretch(2, 1)
        self.glayout_pl_search.setRowStretch(3, 1)
        self.glayout_pl_search.setRowStretch(4, 2)
        self.glayout_pl_search.setRowStretch(5, 1)
        self.glayout_SCDL.addLayout(self.glayout_pl_search, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayout_SCDL.addItem(spacerItem7, 2, 0, 1, 1)
        self.glayout_track_dl = QtWidgets.QGridLayout()
        self.glayout_track_dl.setObjectName("glayout_track_dl")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.glayout_track_dl.addItem(spacerItem8, 2, 2, 1, 1)
        self.btn_track_dl = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.btn_track_dl.setObjectName("btn_track_dl")
        self.glayout_track_dl.addWidget(self.btn_track_dl, 2, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.glayout_track_dl.addItem(spacerItem9, 2, 0, 1, 1)
        self.lbl_track_dl = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_track_dl.sizePolicy().hasHeightForWidth())
        self.lbl_track_dl.setSizePolicy(sizePolicy)
        self.lbl_track_dl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_track_dl.setObjectName("lbl_track_dl")
        self.glayout_track_dl.addWidget(self.lbl_track_dl, 1, 1, 1, 1)
        self.glayout_track_dl.setColumnStretch(0, 1)
        self.glayout_track_dl.setColumnStretch(1, 30)
        self.glayout_track_dl.setColumnStretch(2, 1)
        self.glayout_SCDL.addLayout(self.glayout_track_dl, 9, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.glayout_SCDL.addItem(spacerItem10, 10, 0, 1, 1)
        self.glayout_track_ext = QtWidgets.QGridLayout()
        self.glayout_track_ext.setObjectName("glayout_track_ext")
        self.btn_track_ext = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.btn_track_ext.setObjectName("btn_track_ext")
        self.glayout_track_ext.addWidget(self.btn_track_ext, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.glayout_track_ext.addItem(spacerItem11, 1, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.glayout_track_ext.addItem(spacerItem12, 1, 2, 1, 1)
        self.lbl_track_ext = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_track_ext.sizePolicy().hasHeightForWidth())
        self.lbl_track_ext.setSizePolicy(sizePolicy)
        self.lbl_track_ext.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_track_ext.setObjectName("lbl_track_ext")
        self.glayout_track_ext.addWidget(self.lbl_track_ext, 0, 1, 1, 1)
        self.glayout_track_ext.setColumnStretch(0, 1)
        self.glayout_track_ext.setColumnStretch(1, 30)
        self.glayout_track_ext.setColumnStretch(2, 1)
        self.glayout_track_ext.setRowStretch(0, 10)
        self.glayout_SCDL.addLayout(self.glayout_track_ext, 5, 0, 1, 1)
        self.glayout_SCDL.setRowStretch(0, 1)
        self.glayout_SCDL.setRowStretch(1, 20)
        self.glayout_SCDL.setRowStretch(2, 1)
        self.glayout_SCDL.setRowStretch(3, 1)
        self.glayout_SCDL.setRowStretch(4, 1)
        self.glayout_SCDL.setRowStretch(5, 6)
        self.glayout_SCDL.setRowStretch(6, 1)
        self.glayout_SCDL.setRowStretch(7, 1)
        self.glayout_SCDL.setRowStretch(8, 1)
        self.glayout_SCDL.setRowStretch(9, 6)
        self.glayout_SCDL.setRowStretch(10, 1)
        self.tabWidget.addTab(self.tab_scdl, "")
        self.tab_lib = QtWidgets.QWidget()
        self.tab_lib.setObjectName("tab_lib")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab_lib)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 241, 531))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gLayout_Lib = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gLayout_Lib.setContentsMargins(0, 0, 0, 0)
        self.gLayout_Lib.setObjectName("gLayout_Lib")
        self.btn_move_files = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.btn_move_files.setObjectName("btn_move_files")
        self.gLayout_Lib.addWidget(self.btn_move_files, 24, 0, 1, 1)
        self.lbl_read_dirs = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.lbl_read_dirs.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_read_dirs.setObjectName("lbl_read_dirs")
        self.gLayout_Lib.addWidget(self.lbl_read_dirs, 1, 0, 1, 1)
        self.line_lib1 = QtWidgets.QFrame(parent=self.gridLayoutWidget_3)
        self.line_lib1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_lib1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_lib1.setObjectName("line_lib1")
        self.gLayout_Lib.addWidget(self.line_lib1, 6, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gLayout_Lib.addItem(spacerItem13, 7, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gLayout_Lib.addItem(spacerItem14, 13, 0, 1, 1)
        self.line_lib3 = QtWidgets.QFrame(parent=self.gridLayoutWidget_3)
        self.line_lib3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_lib3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_lib3.setObjectName("line_lib3")
        self.gLayout_Lib.addWidget(self.line_lib3, 17, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gLayout_Lib.addItem(spacerItem15, 18, 0, 1, 1)
        self.btn_sync_music = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.btn_sync_music.setObjectName("btn_sync_music")
        self.gLayout_Lib.addWidget(self.btn_sync_music, 15, 0, 1, 1)
        self.btn_goalfld_search = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.btn_goalfld_search.setObjectName("btn_goalfld_search")
        self.gLayout_Lib.addWidget(self.btn_goalfld_search, 20, 0, 1, 1)
        self.lineEdit_nf_dir = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_3)
        self.lineEdit_nf_dir.setObjectName("lineEdit_nf_dir")
        self.gLayout_Lib.addWidget(self.lineEdit_nf_dir, 4, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.gLayout_Lib.addItem(spacerItem16, 25, 0, 1, 1)
        self.line_lib4 = QtWidgets.QFrame(parent=self.gridLayoutWidget_3)
        self.line_lib4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_lib4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_lib4.setObjectName("line_lib4")
        self.gLayout_Lib.addWidget(self.line_lib4, 23, 0, 1, 1)
        self.lbl_file_uni = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.lbl_file_uni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_file_uni.setObjectName("lbl_file_uni")
        self.gLayout_Lib.addWidget(self.lbl_file_uni, 8, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gLayout_Lib.addItem(spacerItem17, 5, 0, 1, 1)
        self.btn_read_lib = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.btn_read_lib.setObjectName("btn_read_lib")
        self.gLayout_Lib.addWidget(self.btn_read_lib, 2, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gLayout_Lib.addItem(spacerItem18, 11, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gLayout_Lib.addItem(spacerItem19, 16, 0, 1, 1)
        self.btn_file_uni = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.btn_file_uni.setObjectName("btn_file_uni")
        self.gLayout_Lib.addWidget(self.btn_file_uni, 9, 0, 1, 1)
        self.lbl_music_sync = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.lbl_music_sync.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_music_sync.setObjectName("lbl_music_sync")
        self.gLayout_Lib.addWidget(self.lbl_music_sync, 14, 0, 1, 1)
        self.gLayout_uni = QtWidgets.QGridLayout()
        self.gLayout_uni.setObjectName("gLayout_uni")
        self.rbtn_nf = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_3)
        self.rbtn_nf.setChecked(True)
        self.rbtn_nf.setObjectName("rbtn_nf")
        self.gLayout_uni.addWidget(self.rbtn_nf, 1, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gLayout_uni.addItem(spacerItem20, 0, 2, 2, 1)
        self.rbtn_lib = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_3)
        self.rbtn_lib.setChecked(False)
        self.rbtn_lib.setObjectName("rbtn_lib")
        self.gLayout_uni.addWidget(self.rbtn_lib, 0, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gLayout_uni.addItem(spacerItem21, 0, 0, 2, 1)
        self.gLayout_uni.setColumnStretch(0, 1)
        self.gLayout_uni.setColumnStretch(1, 5)
        self.gLayout_uni.setColumnStretch(2, 1)
        self.gLayout_Lib.addLayout(self.gLayout_uni, 10, 0, 1, 1)
        self.lbl_lib_update = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.lbl_lib_update.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_lib_update.setObjectName("lbl_lib_update")
        self.gLayout_Lib.addWidget(self.lbl_lib_update, 19, 0, 1, 1)
        self.btn_reset_goalfld = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.btn_reset_goalfld.setObjectName("btn_reset_goalfld")
        self.gLayout_Lib.addWidget(self.btn_reset_goalfld, 22, 0, 1, 1)
        self.line_lib2 = QtWidgets.QFrame(parent=self.gridLayoutWidget_3)
        self.line_lib2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_lib2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_lib2.setObjectName("line_lib2")
        self.gLayout_Lib.addWidget(self.line_lib2, 12, 0, 1, 1)
        self.gLayout_move = QtWidgets.QGridLayout()
        self.gLayout_move.setObjectName("gLayout_move")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gLayout_move.addItem(spacerItem22, 0, 0, 2, 1)
        self.rbtn_search = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_3)
        self.rbtn_search.setChecked(True)
        self.rbtn_search.setObjectName("rbtn_search")
        self.gLayout_move.addWidget(self.rbtn_search, 1, 1, 1, 1)
        self.rbtn_meta = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_3)
        self.rbtn_meta.setChecked(False)
        self.rbtn_meta.setObjectName("rbtn_meta")
        self.gLayout_move.addWidget(self.rbtn_meta, 0, 1, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gLayout_move.addItem(spacerItem23, 0, 2, 2, 1)
        self.gLayout_move.setColumnStretch(0, 1)
        self.gLayout_move.setColumnStretch(1, 30)
        self.gLayout_move.setColumnStretch(2, 1)
        self.gLayout_Lib.addLayout(self.gLayout_move, 21, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.gLayout_Lib.addItem(spacerItem24, 0, 0, 1, 1)
        self.btn_read_new = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.btn_read_new.setObjectName("btn_read_new")
        self.gLayout_Lib.addWidget(self.btn_read_new, 3, 0, 1, 1)
        self.gLayout_Lib.setRowStretch(0, 1)
        self.tabWidget.addTab(self.tab_lib, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.glayout_msg = QtWidgets.QGridLayout()
        self.glayout_msg.setObjectName("glayout_msg")
        self.lbl_msg = QtWidgets.QLabel(parent=self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_msg.setFont(font)
        self.lbl_msg.setObjectName("lbl_msg")
        self.glayout_msg.addWidget(self.lbl_msg, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(parent=self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.glayout_msg.addWidget(self.progressBar, 2, 0, 1, 1)
        self.txtedit_messages = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_5)
        self.txtedit_messages.setEnabled(True)
        self.txtedit_messages.setReadOnly(True)
        self.txtedit_messages.setObjectName("txtedit_messages")
        self.glayout_msg.addWidget(self.txtedit_messages, 1, 0, 1, 1)
        self.glayout_msg.setColumnStretch(0, 1)
        self.glayout_msg.setRowStretch(0, 1)
        self.glayout_msg.setRowStretch(1, 100)
        self.glayout_msg.setRowStretch(2, 1)
        self.gridLayout.addLayout(self.glayout_msg, 1, 0, 1, 3)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 5)
        self.gridLayout.setRowStretch(0, 6)
        self.gridLayout.setRowStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1180, 22))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionrfsey = QtGui.QAction(parent=MainWindow)
        self.actionrfsey.setObjectName("actionrfsey")
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_save_left.setText(_translate("MainWindow", "Save"))
        self.btn_delrow_left.setText(_translate("MainWindow", "Delete current row"))
        self.btn_cancel_left.setText(_translate("MainWindow", "Cancel"))
        self.btn_addrow_left.setText(_translate("MainWindow", "Add row"))
        self.btn_addrow_right.setText(_translate("MainWindow", "Add row"))
        self.btn_delrow_right.setText(_translate("MainWindow", "Delete current row"))
        self.btn_save_right.setText(_translate("MainWindow", "Save"))
        self.btn_cancel_right.setText(_translate("MainWindow", "Cancel"))
        self.TxtEdit_pl_search.setPlaceholderText(_translate("MainWindow", "Enter playlist names / search keywords"))
        self.btn_pl_search.setText(_translate("MainWindow", "Find Playlists"))
        self.rbtn_pl_search_name.setText(_translate("MainWindow", "Specify Playlists via Name"))
        self.lbl_pl_search.setText(_translate("MainWindow", "Playlist Search Engine"))
        self.rbtn_pl_search_key.setText(_translate("MainWindow", "Specify Name Keywords"))
        self.rbtn_pl_all.setText(_translate("MainWindow", "Find all Playlists"))
        self.btn_track_dl.setText(_translate("MainWindow", "Download Tracks"))
        self.lbl_track_dl.setText(_translate("MainWindow", "Track Downloader"))
        self.btn_track_ext.setText(_translate("MainWindow", "Extract Tracks"))
        self.lbl_track_ext.setText(_translate("MainWindow", "Track Extractor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scdl), _translate("MainWindow", "SCDL"))
        self.btn_move_files.setText(_translate("MainWindow", "Move files"))
        self.lbl_read_dirs.setText(_translate("MainWindow", "Inputs"))
        self.btn_sync_music.setText(_translate("MainWindow", "Sync .mp3 files"))
        self.btn_goalfld_search.setText(_translate("MainWindow", "Search new tracks in Library"))
        self.lineEdit_nf_dir.setPlaceholderText(_translate("MainWindow", "C:/Users/davis/Downloads/SC DL"))
        self.lbl_file_uni.setText(_translate("MainWindow", "File Unifyer"))
        self.btn_read_lib.setText(_translate("MainWindow", "Read library"))
        self.btn_file_uni.setText(_translate("MainWindow", "Unify files"))
        self.lbl_music_sync.setText(_translate("MainWindow", "Music Sync"))
        self.rbtn_nf.setText(_translate("MainWindow", "New files"))
        self.rbtn_lib.setText(_translate("MainWindow", "Library"))
        self.lbl_lib_update.setText(_translate("MainWindow", "Library Updater"))
        self.btn_reset_goalfld.setText(_translate("MainWindow", "Reset goal folder"))
        self.rbtn_search.setText(_translate("MainWindow", "Search filename in Library"))
        self.rbtn_meta.setText(_translate("MainWindow", "Use genre metadata"))
        self.btn_read_new.setText(_translate("MainWindow", "Read new files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_lib), _translate("MainWindow", "Lib Updater"))
        self.lbl_msg.setText(_translate("MainWindow", "Messages"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionrfsey.setText(_translate("MainWindow", "rfsey"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
