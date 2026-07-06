from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime

#Getting user input
def get_user_input():
    print("-------INVOICE GENERATOR-------")
    business_name=input("Enter Business name: ")
    customer_name=input("Enter Customer name: ")
    invoice_no=input("Enter Invoice no.: ")

    #Product details
    product=input("Enter Product Name: ")
    price=int(input("Enter Product Price: "))
    quantity=int(input("Enter Quantity: "))

    return {
        "business_name": business_name,
        "customer_name": customer_name,
        "invoice_no": invoice_no,
        "product": product,
        "quantity": quantity,
        "price": price
    }

#Calculating total amount
def calculate_total(quantity,price,gst_percent=0):
    sub_total=quantity*price
    gst_amount=(sub_total*gst_percent)/100
    grand_total=sub_total+gst_amount
    return sub_total,gst_amount,grand_total

#Displaying the invoice
def display_invoice(data,sub_total,gst_amount,grand_total):
    print("\n-------INVOICE-------")
    print(f"BUSINESS NAME:{data['business_name']}\n")
    print(f"CUSTOMER NAME:{data['customer_name']}\n")
    print(f"INVOICE NO:{data['invoice_no']}\n")
    print(f"DATE:{datetime.now().strftime("%d/%m/%Y")}\n")
    print("\n-------PRODUCT DETAILS-------")
    print(f"PRODUCT:{data['product']}\n")
    print(f"PRICE:{data['price']}\n")
    print(f"QUANTITY:{data['quantity']}\n")
    print("\n-------AMOUNT-------")
    print(f"SUB TOTAL:{sub_total}\n")
    print(f"GST AMOUNT:{gst_amount}\n")
    print(f"GRAND TOTAL:{grand_total}\n")

#Generating pdf
def generate_pdf(data, sub_total, gst_amount, grand_total):
    file_name = f"invoices/Invoice_{data['invoice_no']}.pdf"
    pdf = canvas.Canvas(file_name, pagesize=A4)

    pdf.rect(30, 40, 535, 770)

    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(297, 790, "INVOICE")

    pdf.line(50, 785, 545, 785)

    pdf.setFont("Helvetica-Bold", 12)

    pdf.drawString(50, 750, f"Business Name : {data['business_name']}")
    pdf.drawString(50, 730, f"Customer Name : {data['customer_name']}")

    pdf.drawRightString(545, 750, f"Invoice No : {data['invoice_no']}")
    pdf.drawRightString(545, 730, f"Date : {datetime.now().strftime('%d/%m/%Y')}")

    pdf.line(50, 680, 545, 680)

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(60, 660, "Product")
    pdf.drawString(230, 660, "Quantity")
    pdf.drawString(330, 660, "Price")
    pdf.drawString(450, 660, "Total")

    pdf.line(50, 650, 545, 650)
    pdf.line(200, 680, 200, 615)
    pdf.line(300, 680, 300, 615)
    pdf.line(420, 680, 420, 615)

    total = data["quantity"] * data["price"]

    pdf.setFont("Helvetica", 12)

    pdf.drawString(60, 630, data["product"])
    pdf.drawString(245, 630, str(data["quantity"]))
    pdf.drawString(335, 630, f"Rs.{data['price']:.2f}")
    pdf.drawString(450, 630, f"Rs.{total:.2f}")

    pdf.line(50, 615, 545, 615)

    pdf.rect(320, 450, 220, 110)

    pdf.setFont("Helvetica-Bold", 12)

    pdf.drawString(345, 545, f"Subtotal : Rs.{sub_total:.2f}")
    pdf.drawString(345, 525, f"GST (20%) : Rs.{gst_amount:.2f}")

    pdf.line(340, 510, 520, 510)

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(345, 490, f"Grand Total : Rs.{grand_total:.2f}")

    pdf.line(50, 120, 545, 120)

    pdf.setFont("Helvetica-Oblique", 11)
    pdf.drawCentredString(297, 100, "Thank you for your purchase! ")

    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(297, 82, "We are happy to have you with us.")

    pdf.drawCentredString(297, 64, "Crafter using Python by Gopi")
    pdf.line(390, 160, 530, 160)
    pdf.drawString(405, 145, "Authorized Signature")

    pdf.save()
#Main function
def main():
    data=get_user_input()
    sub_total,gst_amount,grand_total=calculate_total(data["quantity"],data["price"],20)
    display_invoice(data,sub_total,gst_amount,grand_total)
    generate_pdf(data,sub_total,gst_amount,grand_total)


if __name__=="__main__":
    main()




