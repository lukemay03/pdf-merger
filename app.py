from flask import Flask, request, send_file
from PyPDF2 import PdfMerger
import io
import os

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)