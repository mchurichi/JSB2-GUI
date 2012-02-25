#!/usr/bin/env python
# -*- coding: utf-8 *-*

import sys
import json
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QTreeWidgetItem, \
    QFileDialog, QFormLayout, QLineEdit, QLabel
from PyQt4.QtCore import Qt
from jsb2mainwindow import Ui_MainWindow


class JSB2_GUI(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.treeJSB.itemSelectionChanged.connect(self.selected)

    def selected(self):
        selected = self.ui.treeJSB.selectedItems()[0]
        role = str(selected.data(0, Qt.UserRole).toString())
        if role:
            editors = {
                'projectName': lambda: self._edit_textfield('projectName'),
                'licenseText': lambda: self._edit_textfield('licenseText'),
                'deployDir': lambda: self._edit_textfield('deployDir'),
            }
            editor = editors.get(role, self._clear_form)
            if editor:
                editor()
        else:
            self._clear_form()

    def _clear_form(self):
        form = self.ui.formLayout
        while form.count() > 0:
            item = form.takeAt(0)
            if not item:
                continue
            w = item.widget()
            if w:
                w.deleteLater()

    def _edit_textfield(self, label=None):
        self._clear_form()

        self.ui.label22 = QLabel(self.ui.layoutWidget1)
        self.ui.label22.setText(QApplication.translate("MainWindow", \
            label or 'Value', None, QApplication.UnicodeUTF8))
        self.ui.label22.setObjectName("label")

        self.ui.formLayout.setWidget(2, QFormLayout.LabelRole, self.ui.label22)

        self.ui.lineEdit22 = QLineEdit(self.ui.layoutWidget1)
        self.ui.lineEdit22.setObjectName("lineEdit")
        self.ui.lineEdit22.returnPressed.connect(self.ui.buttonBox.accepted)

        self.ui.buttonBox.accepted.connect(
            lambda edit=self.ui.lineEdit22,
                   item=self.ui.treeJSB.selectedItems()[0]:
                       self._set_text(edit, item)
        )

        self.ui.formLayout.setWidget(2, QFormLayout.FieldRole, \
            self.ui.lineEdit22)

    def _set_text(self, edit=None, item=None):
        item.setData(1, Qt.DisplayRole, edit.text())

    def _new_tree_item(self, key, value=None, user_data=None):
        item = QTreeWidgetItem([key, value])
        if user_data:
            item.setData(0, Qt.UserRole, user_data)
        return item

    #TODO: remove file_name argument
    @pyqtSlot('bool')
    def on_action_Open_triggered(self, file_name=None):
        if not file_name:
            file_name = QFileDialog.getOpenFileName(self, u'Open file')
        if file_name:
            f = open(file_name, 'r')
            json_file = f.read()
            jsb2 = json.loads(json_file)
            self.ui.treeJSB.clear()

            # Top leves keys
            items = [
#                QTreeWidgetItem([u'projectName', jsb2['projectName']]),
#                QTreeWidgetItem([u'deployDir', jsb2['deployDir']]),
#                QTreeWidgetItem([u'licenseText', jsb2['licenseText']])
                self._new_tree_item(u'projectName', jsb2['projectName'], \
                    u'projectName'),
                self._new_tree_item(u'deployDir', jsb2['deployDir'], \
                    u'deployDir'),
                self._new_tree_item(u'licenseText', jsb2['licenseText'], \
                    u'licenseText')
            ]
            # Packages
            pkgs = QTreeWidgetItem(\
                [u'pkgs', u'[%i packages]' % len(jsb2['pkgs'])])
            for pkg in jsb2['pkgs']:
                child_pkg = QTreeWidgetItem([pkg['name']])
                child_pkg.addChild(QTreeWidgetItem([u'name', pkg['name']]))
                child_pkg.addChild(QTreeWidgetItem([u'file', pkg['file']]))
                if 'isDebug' in pkg:
                    idebug = unicode(pkg['isDebug'])
                    child_pkg.addChild(QTreeWidgetItem([u'isDebug', idebug]))
                if 'includeDeps' in pkg:
                    ideps = unicode(pkg['includeDeps'])
                    child_pkg.addChild(QTreeWidgetItem([u'includeDeps', ideps]))
                # Dependencies
                if 'pkgDeps' in pkg:
                    num_deps = u'[%i dependencies]' % len(pkg['pkgDeps'])
                    pkg_deps = QTreeWidgetItem([u'pkgDeps', num_deps])
                    for dep in pkg['pkgDeps']:
                        pkg_deps.addChild(QTreeWidgetItem([dep]))
                    child_pkg.addChild(pkg_deps)
                # Files included
                num_files = u'[%i files]' % len(pkg['fileIncludes'])
                fileIncludes = QTreeWidgetItem([u'fileIncludes', num_files])
                for file in pkg['fileIncludes']:
                    child_f = QTreeWidgetItem([file['text']])
                    child_f.addChild(QTreeWidgetItem([u'text', file['text']]))
                    child_f.addChild(QTreeWidgetItem([u'path', file['path']]))
                    fileIncludes.addChild(child_f)
                child_pkg.addChild(fileIncludes)
                # Add package
                pkgs.addChild(child_pkg)
            # Add all packages
            items.append(pkgs)

            # Top level key Resources
            num_res = u'[%i resources]' % len(jsb2['resources'])
            resources = QTreeWidgetItem([u'resources', num_res])
            for res in jsb2['resources']:
                child_r = QTreeWidgetItem([res['src']])
                child_r.addChild(QTreeWidgetItem([u'src', res['src']]))
                child_r.addChild(QTreeWidgetItem([u'dest', res['dest']]))
                child_r.addChild(QTreeWidgetItem([u'filters', res['filters']]))
                resources.addChild(child_r)
            # Add resource
            items.append(resources)

            # Add all top level keys
            self.ui.treeJSB.addTopLevelItems(items)

            self.ui.textConsole.appendPlainText(u'Loaded project "%s" from %s'\
                 % (jsb2['projectName'], file_name))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = JSB2_GUI()
    main_window.show()
    #TODO: Test only
    main_window.on_action_Open_triggered('/home/churi/python/jsb2-gui/ext.jsb2')
    sys.exit(app.exec_())
