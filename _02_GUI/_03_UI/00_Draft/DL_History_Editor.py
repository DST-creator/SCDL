# Form implementation generated from reading ui file 'DL_History_Editor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DL_History_Editor(object):
    def setupUi(self, DL_History_Editor):
        DL_History_Editor.setObjectName("DL_History_Editor")
        DL_History_Editor.resize(400, 520)
        DL_History_Editor.setMinimumSize(QtCore.QSize(400, 520))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DL_History_Editor)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalWidget = QtWidgets.QWidget(parent=DL_History_Editor)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tblView = QtWidgets.QTableView(parent=self.verticalWidget)
        self.tblView.setObjectName("tblView")
        self.verticalLayout.addWidget(self.tblView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cb_update_pl_df = QtWidgets.QCheckBox(parent=self.verticalWidget)
        self.cb_update_pl_df.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.cb_update_pl_df.setChecked(True)
        self.cb_update_pl_df.setObjectName("cb_update_pl_df")
        self.horizontalLayout.addWidget(self.cb_update_pl_df)
        self.horizontalLayout.setStretch(0, 30)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.verticalWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout_2.addWidget(self.verticalWidget)

        self.retranslateUi(DL_History_Editor)
        QtCore.QMetaObject.connectSlotsByName(DL_History_Editor)

    def retranslateUi(self, DL_History_Editor):
        _translate = QtCore.QCoreApplication.translate
        DL_History_Editor.setWindowTitle(_translate("DL_History_Editor", "Dialog"))
        self.cb_update_pl_df.setText(_translate("DL_History_Editor", "Update playlist table"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DL_History_Editor = QtWidgets.QDialog()
    ui = Ui_DL_History_Editor()
    ui.setupUi(DL_History_Editor)
    DL_History_Editor.show()
    sys.exit(app.exec())
