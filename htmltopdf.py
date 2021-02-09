import pdfkit as pdf

fn = raw_input('Please Enter the FileName(Include:.pdf):  ')
url = raw_input('Please Enter the URL:  ')

pdf.from_url(url, fn)
