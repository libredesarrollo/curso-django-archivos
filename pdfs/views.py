import io
from turtle import width

from django.shortcuts import render
from django.conf import settings

from django.http import FileResponse

from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4


# Create your views here.

from weasyprint import HTML
from reportlab.pdfgen import canvas

def generate_pdf(request):
    filename="documents/archivo.pdf"
    HTML("https://www.google.com.ve/").write_pdf(filename)
    return render(request, 'csv.html')

def generate_pdf2(request):
    filename="archivo2.pdf"
    image="documents/logo2.png"

    c = canvas.Canvas(settings.PDF_ROOT+filename, pagesize=A4)

    c.drawString(100,50, "Hola Mundo")

    c.setFont("Times-Roman",20)
    c.drawString(50,10, "Nuevo texto")

    c.setStrokeColorRGB(0,255,66)
    c.circle(70,80,50)
    c.setFillColorRGB(255,0,0)
    c.rect(2*inch,7*inch,8*inch,10*inch, stroke=1, fill=1)
    c.setStrokeColorRGB(0,0,0)
    c.line(2*inch,2*inch,4*inch,8*inch)

    c.drawImage(image,10,15,width=150,preserveAspectRatio=True)

    c.showPage()
    c.save()    
    return render(request, 'csv.html')
    
def generate_pdf_download(request):
    filename="archivo2.pdf"

    buffer = io.BytesIO()

    c = canvas.Canvas(buffer)

    c.drawString(100,50, "Hola Mundo")

    c.showPage()
    c.save()    
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=filename)


def download_file(request):
    # filename="documents/pdf/archivo2.pdf"
    filename="documents/LibroExcel2.xlsx"
    return FileResponse(open(filename,'rb'), filename=filename)