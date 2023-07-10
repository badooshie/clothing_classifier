# clothing_classifier
An application that will take a picture and use ML and AI to identify the clothing and the style.

Input will be a picture of a loose article of clothing or clothing on a person.  The application will the idenitify the clothing and recognize what that clothing is and its style.

Starting point: 
 - will try to first classify only top and bottom such as shirt/jacket (top) and pants/shorts (bottom).  Later will try to expand to accessores such as belts/shoes/hats/jewelry and such.
 - the user will be able to take an image with thier mobile phone or upload an image and have analyzed.
 - will start with python code that can do the classsifyting then wrap ito a web app for use on mobile devices
 - out put should be something like: "This is a red short sleeve v-neck shirt top, with white and black plaid shorts"
 - Later will try to implement recomendations such as: "This is a red short sleeve, this can be used with [inserts style and color] style, and goes well with [inserts style and color] pants


Research List:
 - research clothing styles, get simple list of tops and bottoms
 - research classifier to use. looking at sklearn SVC, sklearn CNN, pytorch, or tensorflow.
 - research how to incorperate python into web-app

Coding Tasks:
 - figure out structure of coding project
 - break down project into small tasks
 - documentation

Checklist:
1. Define the problem. Specify types of clothing and to what accuracy we are aiming to achieve.
2. Gather and preprocess data. Either search for an existing dataset to modify or create out own. Normalize the images (resize, augment, format).
   - get more images
   - start a small database file (csv file) and label each image. the feaures will be color, pattern and type.
4. Choose ML framework (Research sckit-learn SVC or CNN, pytorch, and tensorflow.
5. Split dataset for training, validation and testing. Train the mode, validate to tune hyperparameters, and testing to validate final performance.
6. Implement model on unseen testing data. Evaluate model on metrics such as accuracy prevision and recall.  Need to research which metrics to use here. (f1 score?)
7. Integrate into web-app.  Needs research on what to use her.  Possibly python's django web framework







