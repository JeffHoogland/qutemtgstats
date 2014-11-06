#! /usr/bin/env python
# -*- coding: utf-8 -*-
#  Tested under Python 2.7.1 & PyQt 4.8.3
#
#  QTreeView implementation of a Pivot Table (trying to mimic the spreadsheet concept, as in OpenOffice / Excel)
#
#  This example represents tabular data as a tree. 
#  It was based on Mark Summerfeld's "Rapid GUI programming with Python and Qt", chapter 16, section
#  "Representing Tabular Data in Trees".
#
#  The Tree is composed of branches which hold either sub-branches or leaves, and leaves which hold the data itself.
#  It is built from the table by using the last <n_values> columns as values and the rest of the columns 
#  (ie the first columns up to the n_valueth column counting from the end) as keys.
#  The keys define the position of each item in the tree, for example a row:
#
#  ['Key 1 Value A', 'Key 2 Value AA', Key 3 Value AAA', 15] 
#
#  becomes:
#
#  'Key 1 Value A'                                                 15 *(this is a subtotal as shown below)
#                |-->'Key 2 Value AA'                              15 *(this is a subtotal as shown below)
#                                   |--> 'Key 3 Value AAA'         15 *(this is the item value)
#
#  The last n_values columns hold the values which are to be shown at the leaves or added at the branches:
#    thus each branch line hols the subtotal of its children's values. For example, the rows:
#
#  ['Key 1 Value A', 'Key 2 Value AA', Key 3 Value AAA', 15] 
#  ['Key 1 Value A', 'Key 2 Value AA', Key 3 Value BBB', 30] 
#  ['Key 1 Value A', 'Key 2 Value BB', Key 3 Value CCC', 74] 
#
#  Are represented:
#
#  'Key 1 Value A'                                                119 (subtotal for Key1 = A)
#                |-->'Key 2 Value AA'                              45 (subtotal for Key1 = A, Key2 = AA)
#                                   |--> 'Key 3 Value AAA'         15 (item value)
#                                   |--> 'Key 3 Value BBB'         30 (item value)
#                |-->'Key 2 Value BB'                              74 (subtotal for Key1 = A, Key2 = BB)
#                                   |--> 'Key 3 Value CCC'         74 (item value)
#  
# -------------------------------------------------------------------------------------------------------- #
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *
# -------------------------------------------------------------------------------------------------------- #
# PyQt: select API 2 for Qt components
import sip
for component in ['QDate', 'QDate','QDateTime', 'QString', 'QTextStream', 'QTime', 'QUrl', 'QVariant']:
    sip.setapi(component, 2)
# -------------------------------------------------------------------------------------------------------- #
import sys
from PySide import QtCore, QtGui
import bisect

KEY, NODE = range(2)
DATASET = [
    ['Entity 1','Class 1', 'Line 3', -5700],
    ['Entity 1','Class 1', 'Line 1', 15000],
    ['Entity 2','Class 1', 'Line 2', -1300],
    ['Entity 1','Class 1', 'Line 2', -1200],
    ['Entity 1','Class 2', 'Line 2', -500],
    ['Entity 2','Class 1', 'Line 1', 4500],
    ['Entity 1','Class 2', 'Line 1', 3500],
]

class BranchNode(object):
    def __init__(self, name, parent=None):
        super(BranchNode, self).__init__()
        self.parent = parent
        self.name = name
        self.values = []
        self.children = []

    def __len__(self):
        """The length of a BranchNode = number of child nodes inside it."""
        return len(self.children)

    def childAtRow(self, row):
        return self.children[row][NODE]

    def rowOfChild(self, child):
        for i, item in enumerate(self.children):
            if item[NODE] == child:
                return i
        return -1

    def childWithKey(self, key):
        if not self.children:
            return None
        i = bisect.bisect_left(self.children, (key, None))
        if i < 0 or i >= len(self.children):
            return None
        if self.children[i][KEY] == key:
            return self.children[i][NODE]
        return None

    def insertChild(self, child):
        child.parent = self
        bisect.insort(self.children, (child.name.lower(), child))

    def hasLeaves(self):
        if not self.children:
            return False
        return isinstance(self.children[0], LeafNode)
    
    def sumValues(self, values):
        """ Add to self.values, and ensure that self.values has the proper length. Used when adding rows, see TreeOfTableModel.addRecord. """
        while len(self.values) < len(values):
            self.values.append(0)
        for value in values:
            self.values = [sum(x) for x in zip(self.values, values)]

class LeafNode(object):
    def __init__(self, name, values, parent=None):
        super(LeafNode, self).__init__()
        self.parent = parent
        self.name = name
        self.values = values

    def __len__(self):
        """The length of a LeafNode = number of fields it contains = name field + value fields."""
        return len(1 + self.values)

class TreeOfTableModel(QtCore.QAbstractItemModel):
    def __init__(self, parent=None):
        super(TreeOfTableModel, self).__init__(parent)
        self.root = BranchNode("")
        self.columns = 0
            
    def load(self, table, n_values=1):
        """Loads a data table into the model."""
        self.n_values = n_values
        self.columns = n_values + 1       # Fixed width assumed, ie all rows in the table should have the same number of columns
        self.headers = [u'Keys', u'Values']
        for row in table:
            self.addRecord(row)
        self.reset()
                
    def addRecord(self, row):
        keys = row[:-self.n_values]       # Keys are the columns up to the first value column
        values = row[-self.n_values:]     # Values are the rest of the columns
        root = self.root
        branch = None
        for key in keys[:-1]:            
            branch = root.childWithKey(key.lower())
            if branch is None:
                branch = BranchNode(key)
                root.insertChild(branch)
            branch.sumValues(values)      # Add the values to the branch's subtotal
            root = branch
        name = keys[-1]        
        branch.insertChild(LeafNode(name, values, branch))

    def rowCount(self, parent):
        node = self.nodeFromIndex(parent)
        if node is None or isinstance(node, LeafNode):
            return 0
        return len(node)

    def columnCount(self, parent):
        return self.columns

    def data(self, index, role):
        if role == QtCore.Qt.TextAlignmentRole:
            return (int(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft) if index.column() < self.columns - 1 else int(QtCore.Qt.AlignTop|QtCore.Qt.AlignRight))
        if role != QtCore.Qt.DisplayRole:
            return None
        node = self.nodeFromIndex(index)
        return (node.name if index.column() == 0 else node.values[index.column() -1])

    def headerData(self, section, orientation, role):
        if (orientation == QtCore.Qt.Horizontal and
            role == QtCore.Qt.DisplayRole):
            return self.headers[section]
        return None

    def index(self, row, column, parent):
        branch = self.nodeFromIndex(parent)
        return self.createIndex(row, column, branch.childAtRow(row))

    def parent(self, child):
        node = self.nodeFromIndex(child)
        if node is None:
            return QtCore.QModelIndex()
        parent = node.parent
        if parent is None:
            return QtCore.QModelIndex()
        grandparent = parent.parent
        if grandparent is None:
            return QtCore.QModelIndex()
        row = grandparent.rowOfChild(parent)
        return self.createIndex(row, 0, parent)

    def nodeFromIndex(self, index):
        return (index.internalPointer() if index.isValid() else self.root)

       
    
class MainWindow(QtGui.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.model = TreeOfTableModel()
        self.tree = QtGui.QTreeView()        
        self.tree.setModel(self.model)
        self.model.load(DATASET)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.tree)
        self.setLayout(layout)
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
