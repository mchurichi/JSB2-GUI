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

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTreeWidgetItem


class JSB2Parser:

    def __init__(self, jsb2string=None):
        if jsb2string:
            self.parse(jsb2string)

    def new_tree_item(self, key, value=None, user_data=None):
        data = [key]
        if value:
            data.append(value)
        item = QTreeWidgetItem(data)
        if user_data:
            item.setData(0, Qt.UserRole, user_data)
        return item

    def parse(self, js):
        # Top leves keys
        items = [
            self.new_tree_item(u'projectName', js['projectName'],
                u'projectName'),
            self.new_tree_item(u'deployDir', js['deployDir'],
                u'deployDir'),
            self.new_tree_item(u'licenseText', js['licenseText'],
                u'licenseText')
        ]
        # Packages
        pkgs = self.new_tree_item(u'pkgs', u'[%i packages]' % len(js['pkgs']))
        for pkg in js['pkgs']:
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
            if 'includeDeps' in pkg:
                ideps = unicode(pkg['includeDeps'])
                child_pkg.addChild(self.new_tree_item(u'includeDeps', ideps,
                    'checkbox'))
            # Dependencies
            if 'pkgDeps' in pkg:
                num_deps = u'[%i dependencies]' % len(pkg['pkgDeps'])
                pkg_deps = self.new_tree_item(u'pkgDeps', num_deps)
                for dep in pkg['pkgDeps']:
                    pkg_deps.addChild(self.new_tree_item(dep,
                        user_data='pkgDeps'))
                child_pkg.addChild(pkg_deps)
            # Files included
            num_files = u'[%i files]' % len(pkg['fileIncludes'])
            fileIncludes = self.new_tree_item(u'fileIncludes', num_files)
            for file in pkg['fileIncludes']:
                child_f = self.new_tree_item(file['text'],
                    user_data='fileDescriptor')
                child_f.addChild(self.new_tree_item(u'text', file['text'],
                    'simpletext'))
                child_f.addChild(self.new_tree_item(u'path', file['path'],
                    'simpletext'))
                fileIncludes.addChild(child_f)
            child_pkg.addChild(fileIncludes)
            # Add package
            pkgs.addChild(child_pkg)
        # Add all packages
        items.append(pkgs)

        # Top level key Resources
        num_res = u'[%i resources]' % len(js['resources'])
        resources = self.new_tree_item(u'resources', num_res)
        for res in js['resources']:
            child_r = (self.new_tree_item(res['src'],
                user_data='resourceDescriptor'))
            child_r.addChild(self.new_tree_item(u'src', res['src'],
                'simpletext'))
            child_r.addChild(self.new_tree_item(u'dest', res['dest'],
                'simpletext'))
            child_r.addChild(self.new_tree_item(u'filters', res['filters'],
                'simpletext'))
            resources.addChild(child_r)
        # Add resource
        items.append(resources)

        # Add all top level keys
        self.json = items
