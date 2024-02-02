from PyQt6 import QtCore,QtWidgets

class ItemDelegate(QtWidgets.QItemDelegate):
    def setEditorData(self, editor):
        if isinstance(editor, QtWidgets.QDateEdit):
            #text = index.data()
            #date = QtCore.QDate.fromString(text, "d-MMM-yyyy")
            #editor.setDate(date)
            return
        super().setEditorData(editor)

    def setModelData(self, editor):
        if isinstance(editor, QtWidgets.QDateEdit):
            text = editor.date().toString("d-MMM-yyyy")
            #model.setData(index, text)
            return
        super().setModelData(editor)