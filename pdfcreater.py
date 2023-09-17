# from wkhtmltopdf import wkhtmltopdf

# wkhtmltopdf(url='demo.html', output_file='demo.pdf')

# wkhtmltopdf(url='www.google.com', output_file='example.pdf')

# import wkhtmltopdf
# from wkhtmltopdf.main import WKhtmlToPdf

# var = WKhtmlToPdf(
#     url='http://google.com',
#     output_file='demo.pdf',
# )
# var.render()


# from ironpdf import ChromePdfRendere
# # Instantiate Renderer
# renderer = ChromePdfRenderer()

# # Create a PDF from a URL or local file path
# # pdf = renderer.RenderUrlAsPdf("https://en.wikipedia.org/wiki/PDF")

# # # Export to a file or Stream
# # pdf.SaveAs("url.pdf")

# # Instantiate Renderer
# renderer = ChromePdfRenderer()

# # Create a PDF from an existing HTML file using Python
# pdf = renderer.RenderHtmlFileAsPdf("demo.html")

# # Export to a file or Stream
# pdf.SaveAs("htmlfile_to_pdf.pdf")
# import os
# from pyhtml2pdf import converter

# path = os.path.abspath('demo.html')
# print(path)
# converter.convert(f'file:///{path}', 'sample.pdf',compress=True, power=0)

import pdfkit

pdfkit.from_string("Hello ! My Name is Guru. i'm creat a pdf threw cmd","string.pdf")