from fpdf import FPDF


class Shirtificate:
    def __init__(self):
        self._pdf= FPDF()
        self._pdf.add_page()

    def set_header(self):
        self._pdf.set_font("helvetica", "B", 52)
        self._pdf.cell(0, 60, "CS50 Shirtificate!!",  new_x="LMARGIN", new_y="NEXT", align='C')

    def set_shirt(self,name):
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(25)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=65, y=135, txt=f"{name} took CS50!")

    def set_star(self):
        self._pdf.set_fill_color(r=255, g=255, b=255)
        self._pdf.star(x=55, y=130, r_in=5, r_out=13, rotate_degrees=0, corners=3, style="FD")

    def save_pdf(self):
        self._pdf.output('shirtificate.pdf')

    def run(self, name):
        self.set_header()
        self.set_shirt(name)
        self.set_star()
        self.save_pdf()

def main():
    name= input("What name do you want to print? ")
    pdf=Shirtificate()
    pdf.run(name)

if __name__=="__main__":
    main()