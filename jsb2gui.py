#!/usr/bin/env python
# -*- coding: utf-8 *-*

#    Copyright © 2012 Maximiliano Gabriel Churichi <mchurichi AT gmail DOT com>

#    This file is part of JSB2 GUI.
#
#    JSB2 GUI is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    JSB2 GUI is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with SB2 GUI.  If not, see <http://www.gnu.org/licenses/>.

import sys
import json
from PyQt4 import uic
from PyQt4.QtCore import Qt, pyqtSlot, QStringList
from PyQt4.QtGui import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from jsb2parser import JSB2Parser


class JSB2_GUI(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = uic.loadUi('jsb2mainwindow.ui', self)

        self.ui.treeJSB.itemSelectionChanged.connect(self.selected)
        self.ui.buttonBox.accepted.connect(self.commit_data)
        self.ui.buttonBox.rejected.connect(self.rollback_data)

    def commit_data(self):
        selected = self.get_selected()
        if not selected:
            return
        tw = self.ui.twEditors
        # Si es una una fila, seteo y salgo
        if tw.rowCount() == 1:
            value = self.get_edit_value(tw.item(0, 0))
            self.ui.treeJSB.selectedItems()[0].setData(1, Qt.DisplayRole, value)
            return

        # Obtengo los campos del editor
        data = {}
        for i in range(self.ui.twEditors.rowCount()):
            item = tw.item(i, 0)
            key = unicode(tw.verticalHeaderItem(i).text())
            # its checkable?
            data[key] = self.get_edit_value(item)
            # TODO: mapear data a los hijos del item del arbol

        # Obtengo los hijos en el arbol y seteo sus nuevos valores
        childrens = [selected.child(i) for i in range(selected.childCount())]
        for ch in childrens:
            # TODO: ver como setear la descripcion para los nodos con hijos
            if ch.childCount() == 0:
                key = unicode(ch.data(0, Qt.DisplayRole).toString())
                ch.setData(1, Qt.DisplayRole, data[key])

    def rollback_data(self):
        print 'rollback'

    def selected(self):
        selected = self.get_selected()
        if not selected:
            return
        role = unicode(selected.data(0, Qt.UserRole).toString())
        if role:
            editors = {
                'projectName': self.edit_simpletextfield,
                'licenseText': self.edit_simpletextfield,
                'deployDir': self.edit_simpletextfield,
                'packageDescriptor': self.edit_childtextfield,
                'fileDescriptor': self.edit_childtextfield,
                'resourceDescriptor': self.edit_childtextfield,
                'pkgDeps': self.edit_childtextfield,

                'simpletext': self.edit_simpletextfield,
                'checkbox': self.edit_checkbox
            }
            editors.get(role, self.clear_table)()
        else:
            self.clear_table()

    def get_selected(self):
        selected = self.ui.treeJSB.selectedItems()
        if selected:
            return selected[0]
        else:
            return None

    def get_edit_value(self, widget):
        if not widget.data(Qt.EditRole).toBool():
            return 'True' if widget.checkState() == Qt.Checked else 'False'
        else:
            return unicode(widget.text())

    def clear_table(self):
        self.ui.twEditors.setRowCount(0)
        self.ui.twEditors.setColumnCount(0)
        self.ui.twEditors.clearContents()

    def edit_checkbox(self, label=None):
        selected = self.get_selected()
        if not selected:
            return
        if not label:
            label = selected.data(0, Qt.DisplayRole).toString()
        self.clear_table()
        self.ui.twEditors.setRowCount(1)
        self.ui.twEditors.setColumnCount(1)
        self.ui.twEditors.setVerticalHeaderLabels(QStringList(label))

        checkbox = QTableWidgetItem()
        checkbox.setFlags(checkbox.flags() | Qt.ItemIsUserCheckable)
        checked = selected.data(1, Qt.DisplayRole).toString() == 'True'
        checkbox.setCheckState(Qt.Checked if checked else Qt.Unchecked)
        self.ui.twEditors.setItem(0, 0, checkbox)

    def edit_childtextfield(self, label=None):
        selected = self.get_selected()
        if not selected:
            return
        self.clear_table()
        self.ui.twEditors.setRowCount(0)
        self.ui.twEditors.setColumnCount(1)

        row_labels = []
        tw = self.ui.twEditors
        for ch in [selected.child(i) for i in range(selected.childCount())]:
            label = ch.data(0, Qt.DisplayRole).toString()
            value = ch.data(1, Qt.DisplayRole).toString()
            row_labels.append(label)
            tw.insertRow(tw.rowCount())
            if ch.childCount() == 0:
                if ch.data(0, Qt.UserRole).toString() == 'checkbox':
                    item = QTableWidgetItem()
                    checked = ch.data(1, Qt.DisplayRole).toString() == 'True'
                    item.setCheckState(Qt.Checked if checked else Qt.Unchecked)
                else:
                    item = QTableWidgetItem(value)
            else:
                # TODO: link to the tree item, or something like that
                item = QTableWidgetItem('link')

            tw.setItem(tw.rowCount() - 1, 0, item)
        tw.setVerticalHeaderLabels(QStringList(row_labels))

    def edit_simpletextfield(self, label=None):
        selected = self.get_selected()
        if not selected:
            return
        if not label:
            label = selected.data(0, Qt.DisplayRole).toString()
        self.clear_table()
        self.ui.twEditors.setRowCount(1)
        self.ui.twEditors.setColumnCount(1)
        self.ui.twEditors.setHorizontalHeaderLabels(QStringList(['Value']))
        self.ui.twEditors.setVerticalHeaderLabels(QStringList([label]))
        self.ui.twEditors.setItem(0, 0, QTableWidgetItem(
            self.ui.treeJSB.selectedItems()[0].data(1,
                Qt.DisplayRole).toString()
            ))

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
            jsb2parser = JSB2Parser(jsb2)
            self.ui.treeJSB.addTopLevelItems(jsb2parser.json)
            self.ui.textConsole.appendPlainText(u'Loaded project "%s" from %s'
                 % (jsb2['projectName'], file_name))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = JSB2_GUI()
    main_window.show()
    #TODO: Test only
    main_window.on_action_Open_triggered('ext.jsb2')
    sys.exit(app.exec_())
