import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="QR Code Generator 🔳")

st.title("📱 QR Code Generator")
st.write("Enter text, URL, or anything else to generate a QR code.")

data = st.text_input("Enter text or URL:")

if data:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert image to BytesIO
    buf = BytesIO()
    img.save(buf)
    buf.seek(0)

    st.image(img, caption="Generated QR Code", use_column_width=False)
    st.download_button("⬇️ Download QR Code", buf, file_name="qr.png", mime="image/png")
