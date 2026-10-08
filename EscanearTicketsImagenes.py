import cv2
import os


def detectQR(imagePath):
    img = cv2.imread(imagePath)
    detector = cv2.wechat_qrcode_WeChatQRCode()
    textos, _ = detector.detectAndDecode(img)
    return textos

def obtenerCampos(codigo):
    campos = codigo[0].split("=")
    fecha = f"{campos[2][6:]}/{campos[2][4:6]}/{campos[2][:4]}"
    aut = campos[3]
    pedido = campos[4]
    id = campos[5]
    costo = float(campos[6].split(" ")[0].replace(",", "."))
    return fecha, aut, pedido, id, costo


PATH = "./codigos"
total = 0
tickets = os.listdir(PATH)
if tickets:
    for ticket in tickets:
        print(f"Ticket: {ticket}")
        codigoQR = detectQR(f"{PATH}/{ticket}")
        if (codigoQR == ()):
            print(f"Escaneo fallido")
            print("----------------------------")
            continue
        fecha, aut, pedido, id, costo = obtenerCampos(codigoQR)
        total += costo
        print(f"Escaneo exitoso")
        print("----------------------------")

print(f"Total: {total}€")
cv2.waitKey(0)
cv2.destroyAllWindows()