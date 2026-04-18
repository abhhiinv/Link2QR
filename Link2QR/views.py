import base64
from io import BytesIO

import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from django.shortcuts import render


def home(request):
    qr_code = None
    barcode_image = None
    qr_value = ""
    barcode_value = ""
    qr_error = None
    barcode_error = None
    active_section = request.GET.get("section", "qr")

    if request.method == "POST":
        active_section = request.POST.get("section", "qr")

        if active_section == "barcode":
            barcode_value = request.POST.get("barcode_value", "").strip()

            if not barcode_value:
                barcode_error = "Enter text or numbers to generate a barcode."
            else:
                barcode = Code128(barcode_value, writer=ImageWriter())
                buffer = BytesIO()
                barcode.write(buffer, options={"write_text": False})
                barcode_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
        else:
            active_section = "qr"
            qr_value = request.POST.get("qr_value", "").strip()

            if not qr_value:
                qr_error = "Enter text or a link to generate a QR code."
            else:
                qr = qrcode.QRCode(box_size=10, border=4)
                qr.add_data(qr_value)
                qr.make(fit=True)

                image = qr.make_image(fill_color="black", back_color="white")
                buffer = BytesIO()
                image.save(buffer, format="PNG")
                qr_code = base64.b64encode(buffer.getvalue()).decode("utf-8")

    if active_section not in {"qr", "barcode"}:
        active_section = "qr"

    return render(
        request,
        "home.html",
        {
            "active_section": active_section,
            "barcode_error": barcode_error,
            "barcode_image": barcode_image,
            "barcode_value": barcode_value,
            "qr_code": qr_code,
            "qr_error": qr_error,
            "qr_value": qr_value,
        },
    )
