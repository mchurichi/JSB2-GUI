# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jsb2mainwindow.ui'
#
# Created: Fri Feb 24 13:03:57 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(919, 615)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeJSB = QtGui.QTreeWidget(self.widget)
        self.treeJSB.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.SelectedClicked)
        self.treeJSB.setUniformRowHeights(True)
        self.treeJSB.setAnimated(True)
        self.treeJSB.setColumnCount(2)
        self.treeJSB.setObjectName(_fromUtf8("treeJSB"))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeJSB.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeJSB.headerItem().setFont(1, font)
        item_0 = QtGui.QTreeWidgetItem(self.treeJSB)
        item_0 = QtGui.QTreeWidgetItem(self.treeJSB)
        item_0 = QtGui.QTreeWidgetItem(self.treeJSB)
        item_0 = QtGui.QTreeWidgetItem(self.treeJSB)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_3 = QtGui.QTreeWidgetItem(item_2)
        item_4 = QtGui.QTreeWidgetItem(item_3)
        item_4 = QtGui.QTreeWidgetItem(item_3)
        item_3 = QtGui.QTreeWidgetItem(item_2)
        item_4 = QtGui.QTreeWidgetItem(item_3)
        item_4 = QtGui.QTreeWidgetItem(item_3)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_3 = QtGui.QTreeWidgetItem(item_2)
        item_4 = QtGui.QTreeWidgetItem(item_3)
        item_4 = QtGui.QTreeWidgetItem(item_3)
        item_0 = QtGui.QTreeWidgetItem(self.treeJSB)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        self.treeJSB.header().setVisible(True)
        self.treeJSB.header().setDefaultSectionSize(200)
        self.treeJSB.header().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.treeJSB)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnAdd = QtGui.QPushButton(self.widget)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.horizontalLayout_2.addWidget(self.btnAdd)
        self.btnRemove = QtGui.QPushButton(self.widget)
        self.btnRemove.setObjectName(_fromUtf8("btnRemove"))
        self.horizontalLayout_2.addWidget(self.btnRemove)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.formLayout = QtGui.QFormLayout(self.widget1)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget1)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.splitter_2)
        self.plainTextEdit.setBaseSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(9)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_2.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 919, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuBuilder = QtGui.QMenu(self.menubar)
        self.menuBuilder.setObjectName(_fromUtf8("menuBuilder"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_New = QtGui.QAction(MainWindow)
        self.action_New.setObjectName(_fromUtf8("action_New"))
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName(_fromUtf8("action_Save"))
        self.action_Save_as = QtGui.QAction(MainWindow)
        self.action_Save_as.setObjectName(_fromUtf8("action_Save_as"))
        self.action_Close = QtGui.QAction(MainWindow)
        self.action_Close.setObjectName(_fromUtf8("action_Close"))
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_Preview = QtGui.QAction(MainWindow)
        self.action_Preview.setObjectName(_fromUtf8("action_Preview"))
        self.action_Optiones = QtGui.QAction(MainWindow)
        self.action_Optiones.setObjectName(_fromUtf8("action_Optiones"))
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_Save_as)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Close)
        self.menu_File.addAction(self.action_Quit)
        self.menuBuilder.addAction(self.action_Preview)
        self.menuBuilder.addSeparator()
        self.menuBuilder.addAction(self.action_Optiones)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuBuilder.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "JSB2 GUI", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Value", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeJSB.isSortingEnabled()
        self.treeJSB.setSortingEnabled(False)
        self.treeJSB.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "projectName", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(0).setText(1, QtGui.QApplication.translate("MainWindow", "SmartGestion", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "deployDir", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(1).setText(1, QtGui.QApplication.translate("MainWindow", "/var/www/public", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(2).setText(0, QtGui.QApplication.translate("MainWindow", "licenseText", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(2).setText(1, QtGui.QApplication.translate("MainWindow", "Copyright SmartSoftware Argentina 2012", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).setText(0, QtGui.QApplication.translate("MainWindow", "pkgs", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).setText(1, QtGui.QApplication.translate("MainWindow", "[2 packages]", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "all (name)", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "[2 files]", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "name", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "file", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(1).setText(1, QtGui.QApplication.translate("MainWindow", "all.js", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "isDebug", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(2).setText(1, QtGui.QApplication.translate("MainWindow", "yes", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).setText(0, QtGui.QApplication.translate("MainWindow", "fileIncludes", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).setText(1, QtGui.QApplication.translate("MainWindow", "[2 files]", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "ext-core.js (text)", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).child(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "text", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).child(0).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "ext-core.js", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).child(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "path", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).child(0).child(1).setText(1, QtGui.QApplication.translate("MainWindow", "public/js/ext/", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "ext-all-debug.js (text)", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).child(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "text", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).child(1).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "ext-all-debug.js", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).child(1).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "path", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(0).child(3).child(1).child(1).setText(1, QtGui.QApplication.translate("MainWindow", "public/js/ext/", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "grid (name)", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).setText(1, QtGui.QApplication.translate("MainWindow", "[1 file]", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "name", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "grid", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "file", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(1).setText(1, QtGui.QApplication.translate("MainWindow", "grid.js", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "isDebug", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(2).setText(1, QtGui.QApplication.translate("MainWindow", "yes", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(3).setText(0, QtGui.QApplication.translate("MainWindow", "fileIncludes", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(3).setText(1, QtGui.QApplication.translate("MainWindow", "[1 file]", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(3).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "grid.js (text)", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(3).child(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "text", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(3).child(0).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "grid.js", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(3).child(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "path", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(3).child(1).child(3).child(0).child(1).setText(1, QtGui.QApplication.translate("MainWindow", "public/js/", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(4).setText(0, QtGui.QApplication.translate("MainWindow", "resources", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(4).setText(1, QtGui.QApplication.translate("MainWindow", "[1 resource]", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(4).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "src (name)", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(4).child(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "src", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(4).child(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "dest", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.topLevelItem(4).child(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "filters", None, QtGui.QApplication.UnicodeUTF8))
        self.treeJSB.setSortingEnabled(__sortingEnabled)
        self.btnAdd.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemove.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemove.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBuilder.setTitle(QtGui.QApplication.translate("MainWindow", "&Builder", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New.setText(QtGui.QApplication.translate("MainWindow", "&New...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save_as.setText(QtGui.QApplication.translate("MainWindow", "Save &as...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Close.setText(QtGui.QApplication.translate("MainWindow", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Close.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Preview.setText(QtGui.QApplication.translate("MainWindow", "&Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Optiones.setText(QtGui.QApplication.translate("MainWindow", "&Options", None, QtGui.QApplication.UnicodeUTF8))

