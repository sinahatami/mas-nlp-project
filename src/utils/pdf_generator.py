from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit


def create_debate_pdf(filename, debate_content):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y_position = height - 40
    x_position = 40
    max_width = width - 2 * x_position

    c.setFont("Helvetica", 10)

    for line in debate_content:
        wrapped_lines = simpleSplit(line, "Helvetica", 10, max_width)

        for wrapped_line in wrapped_lines:
            c.drawString(x_position, y_position, wrapped_line)
            y_position -= 20

            if y_position < 40:
                c.showPage()
                y_position = height - 40
                c.setFont("Helvetica", 10)

    c.save()