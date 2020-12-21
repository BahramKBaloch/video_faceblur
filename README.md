# video_faceblur

Have you heard about Multi-task Cascaded Convolutional Neural Networks (MTCNN)?

It's called multi-task as it does two things:
1) Detects faces in an image
2) Outputs five landmarks(eyes(2), nose, mouth(2)) for each detected face.

The best thing about MTCNN is that it is available directly in PyPi
"$ pip install mtcnn"
https://pypi.org/project/mtcnn/


It is easy to use but not ideal for real-time use-cases.

Here a script showing how MTCNN can be used to detect and blur all faces detected in webcam/video. 
