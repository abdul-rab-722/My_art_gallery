import imutils
import cv2

def transfer_style(file_path,fil):
    fil=fil[17:-4]
    fil='.\\models\\'+fil+'.t7'
    net = cv2.dnn.readNetFromTorch(fil)

    img = cv2.imread(file_path)
    img = imutils.resize(img, width=600)
    (h, w) = img.shape[:2]

    blob = cv2.dnn.blobFromImage(img, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)
    net.setInput(blob)
    styled_img = net.forward()

    styled_img = styled_img.reshape((3, styled_img.shape[2], styled_img.shape[3]))
    styled_img[0]+= 103.939
    styled_img[1]+= 116.779
    styled_img[2]+= 123.680
    styled_img/= 255.0
    styled_img = styled_img.transpose(1, 2, 0)

    return styled_img
