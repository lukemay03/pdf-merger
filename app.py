from flask import Flask, request, send_file
from PyPDF2 import PdfMerger
import io

app = Flask(__name__)

@app.route("/merge", methods=["POST"])
def merge_pdfs():
    files = request.files.getlist("files")
    merger = PdfMerger()
    for f in files:
        merger.append(f.stream)
    output = io.BytesIO()
    merger.write(output)
    merger.close()
    output.seek(0)
    return send_file(output, download_name="merged.pdf", as_attachment=True)