import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

class GpaCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GPA Calculator")

        layout = QVBoxLayout()
        self.grades = []
        self.credits = []

        for i in range(8):
            grade_label = QLabel(f"Course {i+1} Grade:")
            grade_input = QLineEdit()
            credit_label = QLabel(f"Course {i+1} Credits:")
            credit_input = QSpinBox()
            credit_input.setRange(1, 5)

            layout.addWidget(grade_label)
            layout.addWidget(grade_input)
            layout.addWidget(credit_label)
            layout.addWidget(credit_input)

            self.grades.append(grade_input)
            self.credits.append(credit_input)


        self.calculate_button = QPushButton("Calculate GPA")
        self.calculate_button.clicked.connect(self.calculate_gpa)
        layout.addWidget(self.calculate_button)


        self.gpa_label = QLabel("GPA:")
        layout.addWidget(self.gpa_label)


        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


        self.setFixedSize(700, 800)


    def calculate_gpa(self):
        quality_points = 0
        total_credits = 0


        for grade, credit in zip(self.grades, self.credits):
            if grade.text():
                quality_points += self.grade_to_quality_points(grade.text()) * credit.value()
                total_credits += credit.value()


        if total_credits == 0:
            self.gpa_label.setText("GPA: 0.0")
        else:
            gpa = quality_points / total_credits
            self.gpa_label.setText(f"GPA: {round(gpa, 2)}")


    def grade_to_quality_points(self, grade):
        grade_dict = {"A": 4, "A-": 3.7, "B+": 3.3, "B": 3, "B-": 2.7, "C+": 2.3, "C": 2, "C-": 1.7, "D": 1, "F": 0}
        return grade_dict.get(grade.upper(), 0)

       

app = QApplication(sys.argv)
window = GpaCalculator()
window.show()

app.exec()