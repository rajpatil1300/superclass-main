import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st

@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()
    
    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )
    
    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )
    
    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1) 
    
    encodings = []
    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1)
        encodings.append(np.array(face_descriptor))
        
    return encodings

@st.cache_resource
def get_trained_model():
    X = []
    Y = []
    
    from src.database.db import get_all_students
    student_db = get_all_students()

    if student_db:
        for student in student_db:
            embedding = student.get('face_embedding')
            if embedding:
                X.append(np.array(embedding))
                Y.append(student.get('student_id'))

  
    if len(X) == 0:
        return None
        
  
    unique_students = set(Y)
    clf = None
    
    if len(unique_students) > 1:
        clf = SVC(kernel='linear', probability=True, class_weight='balanced')
        clf.fit(X, Y)

    # Fixed variable casing
    return {'clf': clf, 'X': X, 'Y': Y}

def train_classifier():
    # It is safer to clear just the model cache rather than the whole app cache,
    # otherwise you have to reload the heavy dlib models every time someone registers.
    get_trained_model.clear() 
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)
    detected_student = {}
    model_data = get_trained_model()

    # If no model data exists, no one is registered yet
    if not model_data:
        return detected_student, [], len(encodings)
        
    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['Y']
    
    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        predicted_id = None
        
        # If we have 2+ students, use the SVM. If only 1, default to that 1 student.
        if clf is not None and len(all_students) >= 2:
            predicted_id = int(clf.predict([encoding])[0])
        else:
            predicted_id = int(all_students[0])

        student_embedding = X_train[y_train.index(predicted_id)]
        
     
        best_match_score = np.linalg.norm(student_embedding - encoding)
        
        resemblance_threshold = 0.60 
        
        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True

    return detected_student, all_students, len(encodings)