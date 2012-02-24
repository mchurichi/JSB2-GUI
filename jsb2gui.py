#!/usr/bin/env python
# -*- coding: utf-8 *-*

import sys
import json
from PyQt4.QtCore import QObject, SIGNAL, pyqtSlot
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QTreeWidgetItem, \
    QFileDialog
from jsb2mainwindow import Ui_MainWindow


class JSB2_GUI(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QObject.connect(self.ui.treeJSB, \
            SIGNAL('itemSelectionChanged()'), self.selected)

    def selected(self):
        pass
#        print self.ui.treeJSB.selectedItems()[0].setText(1, 'lalalal')

    @pyqtSlot('bool')
    def on_action_Open_triggered(self, checked=None):
        file_name = QFileDialog.getOpenFileName(self, u'Open file')
        if file_name:
            f = open(file_name, 'r')
            json_file = f.read()
            jsb2 = json.loads(json_file)
            self.ui.treeJSB.clear()

            # Top leves keys
            items = [
                QTreeWidgetItem([u'projectName', jsb2['projectName']]),
                QTreeWidgetItem([u'deployDir', jsb2['deployDir']]),
                QTreeWidgetItem([u'licenseText', jsb2['licenseText']])
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = JSB2_GUI()
    main_window.show()
    sys.exit(app.exec_())
