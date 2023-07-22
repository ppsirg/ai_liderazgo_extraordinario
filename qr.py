"""
generate a python command line script that create a qr code image 
whith a url encoded on it and assign that qr image a name. 
both name and url must be given as input and collected with 
argparse lib
"""
import argparse
import qrcode


def create_qr_code(name, url):
    # Generate the QR code image
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    # Save the QR code image with the given name
    qr_img.save(f"{name}.png")
    print(f"QR code image '{name}.png' created successfully!")


if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description="Generate a QR code image with a URL encoded on it."
    )
    # Add the arguments
    parser.add_argument("name", type=str, help="Name for the QR code image")
    parser.add_argument("url", type=str, help="URL to encode on the QR code image")
    # Parse the arguments
    args = parser.parse_args()
    # Create the QR code image
    create_qr_code(args.name, args.url)
