import cv2
image=cv2.imread("solar-system.jpg")

cv2.putText(image,"Sun",(20,200),cv2.FONT_HERSHEY_DUPLEX ,1,(255,255,255))

cv2.putText(image,"Mercury",(100,200),cv2.FONT_HERSHEY_DUPLEX ,0.5,(255,255,255))

cv2.putText(image,"Venus",(200,200),cv2.FONT_HERSHEY_DUPLEX ,0.5,(255,255,255))

cv2.putText(image,"Earth",(300,200),cv2.FONT_HERSHEY_DUPLEX ,0.5,(255,255,255))

cv2.putText(image,"Mars",(400,200),cv2.FONT_HERSHEY_DUPLEX ,0.5,(255,255,255))

cv2.putText(image,"Jupiter",(550,200),cv2.FONT_HERSHEY_DUPLEX ,0.5,(255,255,255))

cv2.putText(image,"Saturn",(750,200),cv2.FONT_HERSHEY_DUPLEX ,0.5,(255,255,255))

cv2.putText(image,"Uranus",(950,200),cv2.FONT_HERSHEY_DUPLEX ,0.5,(0,0,0))

cv2.putText(image,"Neptune",(1150,200),cv2.FONT_HERSHEY_DUPLEX ,0.5,(255,255,255))

cv2.imwrite("solar-system with name.jpg",image)

cv2.imshow("solar-system",image)

cv2.waitKey(0)

