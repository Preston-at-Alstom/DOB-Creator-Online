from pypdf import PdfWriter
from pypdf import PdfReader
from io import BytesIO
import datetime as dt
  

def get_date():
    #get date
    hour = int(dt.datetime.now().strftime("%H"))
    if hour >=19 and hour <24:
            date = dt.date.today() + dt.timedelta(days=1)
    else:
            date = dt.date.today()

    # from date, get month
    month = date.strftime("%B")
    if date.day >0 and date.day <10:
            day = f'0{date.day}'
    else:
        day = date.day

    # from date, get year
    year = date.year

    return month, day, year

# Create File names for DOB packages
def create_file_names():
    month, day, year = get_date()

    dob_print_output_file = f'Complete DOB Package (print version) {month} {day}, {year}.pdf'
    dob_email_output_file = f'Complete DOB Package {month} {day}, {year}.pdf'
    don_output_file       = f'DON Package {month} {day}, {year}.pdf'
    cp_output_file        = f'CP DOB {month} {day}, {year}.pdf'
    metro_output_file     = f'Metrolinx DOB {month} {day}, {year}.pdf'

    return dob_print_output_file, dob_email_output_file, don_output_file, cp_output_file, metro_output_file



def combine(list_of_pdfs):
    # Create a PdfMerger object
    merger = PdfWriter()
    
    # Iterate through the uploaded files and append them to the merger
                # The uploaded file is a file-like object, which pypdf can read directly
    
    for file in list_of_pdfs:
        number_of_pages = len(PdfReader(file).pages)
        if  number_of_pages % 2 != 0:
            merger.append(file)
            merger.append('./PDFs/blank.pdf')
        else:
            merger.append(file)

    byte_stream = BytesIO()
    merger.write(byte_stream)
    byte_stream.seek(0)
    return byte_stream

