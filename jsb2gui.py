#!/usr/bin/env python
# -*- coding: utf-8 *-*

import sys
import json
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import (QApplication, QMainWindow, QWidget, QTreeWidgetItem,
    QFileDialog, QTableWidgetItem)
from PyQt4.QtCore import Qt, QStringList, QString
from jsb2mainwindow import Ui_MainWindow


class JSB2_GUI(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.treeJSB.itemSelectionChanged.connect(self.selected)
        self.ui.buttonBox.accepted.connect(self.commit_data)
        self.ui.buttonBox.rejected.connect(self.rollback_data)

    def commit_data(self):
        for i in range(self.ui.twEditors.rowCount()):
            value = self.ui.twEditors.item(0, 0).text()
            self.ui.treeJSB.selectedItems()[0].setData(1, Qt.DisplayRole, value)
#            print self.ui.twEditors.item(i, 0).text()

    def rollback_data(self):
        print 'rollback'

    def selected(self):
        selected = self.ui.treeJSB.selectedItems()[0]
        role = unicode(selected.data(0, Qt.UserRole).toString())
        if role:
            editors = {
                'projectName': lambda: self.edit_simpletextfield('projectName'),
                'licenseText': lambda: self.edit_simpletextfield('licenseText'),
                'deployDir': lambda: self.edit_simpletextfield('deployDir'),
                'packageDescriptor': lambda: self.edit_childtextfield(),
                'fileDescriptor': lambda: self.edit_childtextfield(),
                'simpletext': lambda: self.edit_simpletextfield(),
                'checkbox': lambda: self.edit_checkbox()
            }
            editors.get(role, self.clear_table)()
        else:
            self.clear_table()

    def clear_table(self):
        self.ui.twEditors.setRowCount(0)
        self.ui.twEditors.setColumnCount(0)
        self.ui.twEditors.clearContents()

    def edit_checkbox(self, label=None):
        selected = self.ui.treeJSB.selectedItems()[0]
        if not label:
            label = selected.data(0, Qt.DisplayRole).toString()
        self.clear_table()
        self.ui.twEditors.setRowCount(1)
        self.ui.twEditors.setColumnCount(1)
        self.ui.twEditors.setVerticalHeaderLabels(QStringList(label))

        checkbox = QTableWidgetItem()
        if selected.data(1, Qt.DisplayRole).toString() == 'True':
            checkbox.setCheckState(Qt.Checked)
        else:
            checkbox.setCheckState(Qt.Unchecked)
        self.ui.twEditors.setItem(0, 0, checkbox)

    def edit_childtextfield(self, label=None):
        selected = self.ui.treeJSB.selectedItems()[0]
        self.clear_table()
        self.ui.twEditors.setRowCount(0)
        self.ui.twEditors.setColumnCount(1)

        row_labels = []
        tw = self.ui.twEditors
        for ch in [selected.child(i) for i in range(selected.childCount())]:
            if ch.childCount() == 0:
                label = ch.data(0, Qt.DisplayRole).toString()
                value = ch.data(1, Qt.DisplayRole).toString()
                row_labels.append(label)
                tw.insertRow(tw.rowCount())
                tw.setItem(tw.rowCount() - 1, 0, QTableWidgetItem(value))
        tw.setVerticalHeaderLabels(QStringList(row_labels))

    def edit_simpletextfield(self, label=None):
#        self.ui.twEditors.clearContents()

        if not label:
            label = self.ui.treeJSB.selectedItems()[0].data(0, Qt.DisplayRole).toString()
        self.clear_table()
        self.ui.twEditors.setRowCount(1)
        self.ui.twEditors.setColumnCount(1)
        self.ui.twEditors.setHorizontalHeaderLabels(QStringList(['Value']))
        self.ui.twEditors.setVerticalHeaderLabels(QStringList([label]))
        self.ui.twEditors.setItem(0, 0, QTableWidgetItem(
            self.ui.treeJSB.selectedItems()[0].data(1,
                Qt.DisplayRole).toString()
            ))

    def set_text(self, edit=None, item=None):
        item.setData(1, Qt.DisplayRole, edit.text())

    def new_tree_item(self, key, value=None, user_data=None):
        item = QTreeWidgetItem([key, value])
        if user_data:
            item.setData(0, Qt.UserRole, user_data)
        return item

    #TODO: remove file_name argument
    @pyqtSlot('bool')
    def on_action_Open_triggered(self, file_name=None):
        if not file_name:
            file_name = QFileDialog.getOpenFileName(self, u'Open file',
                filter="*.jsb2")
        if file_name:
            f = open(file_name, 'r')
            json_file = f.read()
            jsb2 = json.loads(json_file)
            self.ui.treeJSB.clear()

            # Top leves keys
            items = [
                self.new_tree_item(u'projectName', jsb2['projectName'],
                    u'projectName'),
                self.new_tree_item(u'deployDir', jsb2['deployDir'],
                    u'deployDir'),
                self.new_tree_item(u'licenseText', jsb2['licenseText'],
                    u'licenseText')
            ]
            # Packages
            pkgs = QTreeWidgetItem(
                [u'pkgs', u'[%i packages]' % len(jsb2['pkgs'])])
            for pkg in jsb2['pkgs']:
                child_pkg = self.new_tree_item(pkg['name'], pkg['name'],
                    'packageDescriptor')
                child_pkg.addChild(self.new_tree_item(u'name', pkg['name'],
                    'simpletext'))
                child_pkg.addChild(self.new_tree_item(u'file', pkg['file'],
                    'simpletext'))
                if 'isDebug' in pkg:
                    isdebug = unicode(pkg['isDebug'])
                    child_pkg.addChild(self.new_tree_item(u'isDebug', isdebug,
                        'checkbox'))
#                    child_pkg.addChild(QTreeWidgetItem([u'isDebug', idebug]))
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
#                fileIncludes = QTreeWidgetItem([u'fileIncludes', num_files])
                fileIncludes = self.new_tree_item(u'fileIncludes', num_files,
                    'fileDescriptor')
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

            self.ui.textConsole.appendPlainText(u'Loaded project "%s" from %s'
                 % (jsb2['projectName'], file_name))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = JSB2_GUI()
    main_window.show()
    #TODO: Test only
    main_window.on_action_Open_triggered('/home/churi/python/JSB2-GUI/ext.jsb2')
    sys.exit(app.exec_())
