# import the opencv library 
import cv2 
import mtcnn
import matplotlib.pyplot as plt

# define a video capture object 
vid = cv2.VideoCapture(0) #cv2.VideoCapture('any_video_file.mp4')
detector = mtcnn.MTCNN()
color = (255, 0, 0) 
thickness = 2
i=0
max_face_per_frame = 1
zoom_level = 50
while (True): 
	if i%45 != 0: # processing 1 in 45th frame only.
		continue
	# Capture the video frame 
	# by frame 
	ret, frame = vid.read() 
	faces = []
	faces = detector.detect_faces(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) #cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	# plot each box
	for result in faces[:max_face_per_frame]:
		# get coordinates
		x, y, width, height = result['box']
		# create the shape
		frame = cv2.rectangle(frame, (x,y), (x+width, y+height), color, thickness) 
		#BLur face
		frame[y:y+height, x:x+width] = cv2.blur(frame[y:y+height, x:x+width] , (50,50))
	# Display the resulting frame 
	cv2.imshow('frame', frame) 
	# the 'q' button is set as the 
	# quitting button you may use any 
	# desired button of your choice 
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
