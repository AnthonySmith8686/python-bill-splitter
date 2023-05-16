import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates flatmate object who lives in the flat and shares the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PDFReport:
    """
    Creates PDF file about flatmates bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image('house.png', w=30, h=30)

        # Add Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period Label and Value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert Name and Due Amount of First Flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=0, ln=1)

        # Insert Name and Due Amount of First Flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


the_bill = Bill(amount=120, period="March 2022")
john = Flatmate(name="John", days_in_house=20)
mary = Flatmate(name="Mary", days_in_house=25)

print(john.pays(bill=the_bill, flatmate2=mary))

pdf_report = PDFReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)


