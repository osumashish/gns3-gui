# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/traceng/ui/traceng_node_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TraceNGNodeWizard(object):
    def setupUi(self, TraceNGNodeWizard):
        TraceNGNodeWizard.setObjectName("TraceNGNodeWizard")
        TraceNGNodeWizard.resize(706, 452)
        TraceNGNodeWizard.setModal(True)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiServerWizardPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiServerTypeGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiRemoteRadioButton.setEnabled(False)
        self.uiRemoteRadioButton.setChecked(False)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.verticalLayout.addWidget(self.uiRemoteRadioButton)
        self.uiVMRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiVMRadioButton.setEnabled(False)
        self.uiVMRadioButton.setObjectName("uiVMRadioButton")
        self.verticalLayout.addWidget(self.uiVMRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiLocalRadioButton.setChecked(True)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.verticalLayout.addWidget(self.uiLocalRadioButton)
        self.gridLayout_2.addWidget(self.uiServerTypeGroupBox, 0, 0, 1, 1)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout_7.addWidget(self.uiRemoteServersLabel, 0, 0, 1, 1)
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout_7.addWidget(self.uiRemoteServersComboBox, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.uiRemoteServersGroupBox, 1, 0, 1, 1)
        TraceNGNodeWizard.addPage(self.uiServerWizardPage)
        self.uiNameWizardPage = QtWidgets.QWizardPage()
        self.uiNameWizardPage.setObjectName("uiNameWizardPage")
        self.gridLayout = QtWidgets.QGridLayout(self.uiNameWizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.uiNameWizardPage)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.uiNameWizardPage)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiIPAddressLabel = QtWidgets.QLabel(self.uiNameWizardPage)
        self.uiIPAddressLabel.setObjectName("uiIPAddressLabel")
        self.gridLayout.addWidget(self.uiIPAddressLabel, 1, 0, 1, 1)
        self.uiIPAddressLineEdit = QtWidgets.QLineEdit(self.uiNameWizardPage)
        self.uiIPAddressLineEdit.setText("")
        self.uiIPAddressLineEdit.setObjectName("uiIPAddressLineEdit")
        self.gridLayout.addWidget(self.uiIPAddressLineEdit, 1, 1, 1, 1)
        TraceNGNodeWizard.addPage(self.uiNameWizardPage)

        self.retranslateUi(TraceNGNodeWizard)
        QtCore.QMetaObject.connectSlotsByName(TraceNGNodeWizard)

    def retranslateUi(self, TraceNGNodeWizard):
        _translate = QtCore.QCoreApplication.translate
        TraceNGNodeWizard.setWindowTitle(_translate("TraceNGNodeWizard", "New TraceNG node template"))
        self.uiServerWizardPage.setTitle(_translate("TraceNGNodeWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("TraceNGNodeWizard", "Please choose a server type to run the TraceNG node."))
        self.uiServerTypeGroupBox.setTitle(_translate("TraceNGNodeWizard", "Server type"))
        self.uiRemoteRadioButton.setText(_translate("TraceNGNodeWizard", "Run the TraceNG node on a remote computer"))
        self.uiVMRadioButton.setText(_translate("TraceNGNodeWizard", "Run the TraceNG node on the GNS3 VM"))
        self.uiLocalRadioButton.setText(_translate("TraceNGNodeWizard", "Run the TraceNG node on your local computer"))
        self.uiRemoteServersGroupBox.setTitle(_translate("TraceNGNodeWizard", "Remote server"))
        self.uiRemoteServersLabel.setText(_translate("TraceNGNodeWizard", "Run on:"))
        self.uiNameWizardPage.setTitle(_translate("TraceNGNodeWizard", "Name and IP address"))
        self.uiNameWizardPage.setSubTitle(_translate("TraceNGNodeWizard", "Please choose a descriptive name and IP address for the new TraceNG node."))
        self.uiNameLabel.setText(_translate("TraceNGNodeWizard", "Name:"))
        self.uiIPAddressLabel.setText(_translate("TraceNGNodeWizard", "IP address:"))

