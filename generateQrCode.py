import argparse
import qrcode

# Initialize ArgumentParser
parser = argparse.ArgumentParser(description='Generate QR code')

# Add argument for QR code content
parser.add_argument('-m', '--message', nargs='+', help='Content for QR code')

# Parse arguments
args = parser.parse_args()

# Concatenate the argument values into a single string
qrcode_content = ' '.join(args.message)

# Check if the content is provided
if qrcode_content:
    # Generate QR code
    qr = qrcode.make(qrcode_content)
    
    # Save QR code as image
    qr.save("qrcode.png")
    print("QR code generated successfully.")
else:
    print("No message provided for QR code generation.")
