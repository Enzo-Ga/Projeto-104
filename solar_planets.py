import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sol",
            (100, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0, 0, 255)
            )
cv2.putText(img,
            "Mercurio",
            (110, 245),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 255)
            )
cv2.putText(img,
            "Venus",
            (190, 255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 255)
            )
cv2.putText(img,
            "Terra",
            (290, 260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 255)
            )
cv2.putText(img,
            "Lua",
            (325, 150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 255)
            )
cv2.putText(img,
            "Marte",
            (375, 255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 255)
            )
cv2.putText(img,
            "Jupiter",
            (575, 375),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 255)
            )
cv2.putText(img,
            "Saturno",
            (765, 285),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 255)
            )
cv2.putText(img,
            "Urano",
            (970, 285),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 255)
            )
cv2.putText(img,
            "Netuno",
            (1115, 285),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 255)
            )

cv2.imshow("Resultado", img)
cv2.waitKey(0)
cv2.imread("Solar_systemwithname.jpg", img)
