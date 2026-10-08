import cv2
import os


def detectQR(detector, img):
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
ultimo = ()
detector = cv2.wechat_qrcode_WeChatQRCode()
cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    codigoQR = detectQR(detector, frame)
    print(codigoQR)

    if codigoQR != ultimo:
        fecha, aut, pedido, id, costo = obtenerCampos(codigoQR)
        total += costo
        print(f"Escaneo exitoso")
        print(f"Ticket: {id}")
        print(f"-----------------------------")
        ultimo = codigoQR

    cv2.imshow("Lector QR (q para salir)", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

print(f"Total: {total}€")
cv2.waitKey(0)
cv2.destroyAllWindows()