from fpdf import FPDF
import textwrap

pdf = FPDF()
pdf.add_page()
pdf.set_font('Helvetica', '', 11)
long_text = 'A' * 300 + ' ' + 'B' * 300 + ' ' + 'https://example.com/' + 'C' * 300
wrapped = textwrap.wrap(
    long_text,
    width=95,
    break_long_words=True,
    break_on_hyphens=False,
    replace_whitespace=False,
)
for chunk in wrapped:
    pdf.multi_cell(0, 7, chunk)

output = pdf.output(dest='S')
print('OK', len(output))
