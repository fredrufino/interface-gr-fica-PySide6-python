# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesErigwH.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

#IMPORT QT CORE
from qt_core import *

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(769, 484)
        self.Page_1 = QWidget()
        self.Page_1.setObjectName(u"Page_1")
        self.verticalLayout = QVBoxLayout(self.Page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.Page_1)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        application_pages.addWidget(self.Page_1)
        self.Page_2 = QWidget()
        self.Page_2.setObjectName(u"Page_2")
        self.verticalLayout_2 = QVBoxLayout(self.Page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.Page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application_pages.addWidget(self.Page_2)
        self.Page_3 = QWidget()
        self.Page_3.setObjectName(u"Page_3")
        self.verticalLayout_3 = QVBoxLayout(self.Page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.Page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        application_pages.addWidget(self.Page_3)

        self.retranslateUi(application_pages)

        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("application_pages", u"P\u00e1gina Inicial", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"P\u00e1gina 2", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"P\u00e1gina 3", None))
    # retranslateUi

