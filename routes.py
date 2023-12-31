from flask import Blueprint, request, jsonify
import io
from PyPDF2 import PdfReader


bp = Blueprint("routes", __name__)


@bp.route('/')
def hello_world():
    return 'Hello World!'


@bp.route('/predict', methods=['GET'])
def predict_get():
    return 'Hello, you called the predict GET method'


@bp.route('/predict', methods=['POST'])
def predict_post():
    data = request.json
    data["test"] = "ok"

    # Replace the following line with your model logic
    predictions = data  # todo:: replace with your own model
    return jsonify(predictions)


@bp.route('/receipts', methods=['GET'])
def get_receipts():
    receipts_data = [
        {
            "OrderId": 1,
            "CustomerId": 1,
            "CustomerName": "Elizabeth",
            "Total": "$30.00",
            "Date": "2021-02-01 08:30:00.000",
            "Items": [
                {
                    "Item": "Candle",
                    "ItemPrice": "$3.00",
                    "Quantity": "3"
                },
                {
                    "Item": "Book",
                    "ItemPrice": "$15.00",
                    "Quantity": "1"
                },
                {
                    "Item": "Pen",
                    "ItemPrice": "$0.75",
                    "Quantity": "1"
                },
                {
                    "Item": "Paper",
                    "ItemPrice": "$5.25",
                    "Quantity": "1"
                }
            ]
        },
        {
            "OrderId": 2,
            "CustomerId": 2,
            "CustomerName": "Alexander",
            "Total": "$52.50",
            "Date": "2021-02-02 10:00:00.000",
            "Items": [
                {
                    "Item": "Book",
                    "ItemPrice": "$15.00",
                    "Quantity": "1"
                },
                {
                    "Item": "Jar",
                    "ItemPrice": "$12.50",
                    "Quantity": "3"
                }
            ]
        },
        {
            "OrderId": 3,
            "CustomerId": 1,
            "CustomerName": "Elizabeth",
            "Total": "$6.00",
            "Date": "2021-02-02 12:46:00.000",
            "Items": [
                {
                    "Item": "Pen",
                    "ItemPrice": "$0.75",
                    "Quantity": "1"
                },
                {
                    "Item": "Paper",
                    "ItemPrice": "$5.25",
                    "Quantity": "1"
                }
            ]
        },
        {
            "OrderId": 4,
            "CustomerId": 3,
            "CustomerName": "Emira",
            "Total": "$30.50",
            "Date": "2021-02-03 15:25:00.000",
            "Items": [
                {
                    "Item": "Candle",
                    "ItemPrice": "$3.00",
                    "Quantity": "1"
                },
                {
                    "Item": "Book",
                    "ItemPrice": "$15.00",
                    "Quantity": "1"
                },
                {
                    "Item": "Jar",
                    "ItemPrice": "$12.50",
                    "Quantity": "1"
                }
            ]
        },
        {
            "OrderId": 5,
            "CustomerId": 4,
            "CustomerName": "LJ",
            "Total": "$36.00",
            "Date": "2021-02-04 18:50:00.000",
            "Items": [
                {
                    "Item": "Pen",
                    "ItemPrice": "$0.75",
                    "Quantity": "1"
                },
                {
                    "Item": "Book",
                    "ItemPrice": "$15.00",
                    "Quantity": "2"
                },
                {
                    "Item": "Paper",
                    "ItemPrice": "$5.25",
                    "Quantity": "1"
                }
            ]
        },
        {
            "OrderId": 6,
            "CustomerId": 5,
            "CustomerName": "Armand",
            "Total": "$52.50",
            "Date": "2021-02-04 08:05:00.000",
            "Items": [
                {
                    "Item": "Book",
                    "ItemPrice": "$15.00",
                    "Quantity": "1"
                },
                {
                    "Item": "Jar",
                    "ItemPrice": "$12.50",
                    "Quantity": "3"
                }
            ]
        },
        {
            "OrderId": 7,
            "CustomerId": 6,
            "CustomerName": "Elizabeth",
            "Total": "$30.50",
            "Date": "2021-02-06 17:30:00.000",
            "Items": [
                {
                    "Item": "Movie",
                    "ItemPrice": "$18.00",
                    "Quantity": "1"
                },
                {
                    "Item": "Jar",
                    "ItemPrice": "$12.50",
                    "Quantity": "1"
                }
            ]
        },
        {
            "OrderId": 8,
            "CustomerId": 3,
            "CustomerName": "Emira",
            "Total": "$18",
            "Date": "2021-02-08 16:30:00.000",
            "Items": [
                {
                    "Item": "Movie",
                    "ItemPrice": "$18.00",
                    "Quantity": "1"
                }
            ]
        }
    ]
    return jsonify(receipts_data)


@bp.route('/upload/pdf', methods=['POST'])
def upload_file():
    # Check if the POST request contains a file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty part without a filename
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    # Check if the file has a PDF extension
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'message': 'File must have a .pdf extension'}), 400

    # Read the content of the uploaded PDF file and extract text
    pdf_content = file.read()
    pdf_text = extract_text_from_pdf(pdf_content)

    # Process the extracted text into an array of strings (e.g., splitting by lines)
    # Modify this part based on your specific processing needs
    pdf_lines = pdf_text.split('\n')

    return jsonify({'message': 'PDF file processed successfully', 'lines': pdf_lines})

def extract_text_from_pdf(pdf_content):
    pdf_reader = PdfReader(io.BytesIO(pdf_content))
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
