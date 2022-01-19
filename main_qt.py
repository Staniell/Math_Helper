import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import first_topics

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("app_interface.ui", self)

        self.Class_Combobox.addItem("Variation Measure")
        self.Class_Combobox.addItem("Grouped Data")
        self.Class_Combobox.addItem("Central Tendency")

        #For variation measure
        self.Grouped_Combobox.addItem("Population Variance")
        self.Grouped_Combobox.addItem("Sample Variance")

        self.pushButton.clicked.connect(self.variation_Measure)
        self.Class_Combobox.currentIndexChanged.connect(self.changeList)
        self.resultText.setReadOnly(True)


    def changeList(self):
        self.Grouped_Combobox.clear()
        if self.Class_Combobox.currentText() == "Grouped Data":
            self.Grouped_Combobox.addItem("Percentile")
            self.Grouped_Combobox.addItem("Sample Variance")
        
        elif self.Class_Combobox.currentText() == "Variation Measure":
            self.Grouped_Combobox.addItem("Population Variance")
            self.Grouped_Combobox.addItem("Sample Variance")
        else:
            self.Grouped_Combobox.addItem("Mean")
            self.Grouped_Combobox.addItem("Median")
            self.Grouped_Combobox.addItem("Mode")
        print("Hello world")

    def variation_Measure(self):
        text_value = self.lineEdit.text().strip()
        data = list(map(int, text_value.split(" ")))
        
        if self.Class_Combobox.currentText() == "Variation Measure":
            x = first_topics.Variation_Measure()
            if self.Grouped_Combobox.currentText() == "Sample Variance":
                result = x.sample_variance(data, True)
            elif self.Grouped_Combobox.currentText() == "Population Variance":
                result = x.pop_variance(data)
        
        elif self.Class_Combobox.currentText() == "Grouped Data":
#             x = first_topics.Grouped_Data()
#             if self.Grouped_Combobox.currentText() == "Percentile":
#                 x.percentile(70,{range(40,50):[3], range(50,60):[5], range(60,70):[6], range(70,80):[9],
# range(80,90):[8],range(90,100):[7]})
            pass
        elif self.Class_Combobox.currentText() == "Central Tendency":
            x = first_topics.Central_Tendency()
            if self.Grouped_Combobox.currentText() == "Mean":
                result = x.mean(data)
            elif self.Grouped_Combobox.currentText() == "Mode":
                result = x.mode(data)
            elif self.Grouped_Combobox.currentText() == "Median":
                result = x.median(data)
        

        print(result)
        self.resultText.setPlainText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Window..")