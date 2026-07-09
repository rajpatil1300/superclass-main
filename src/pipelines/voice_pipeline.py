from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import io
import librosa
import streamlit as st

@st.cache_resource
def get_voice_encoder():
    return VoiceEncoder()

def get_voice_embedding(audio_bytes):
    try:
        encoder = get_voice_encoder() 

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        wav = preprocess_wav(audio)
        embedding = encoder.embed_utterance(wav)
        return embedding.tolist()
    except Exception as e:
        st.error(f'Voice recognition error: {e}')
        return None

def identify_speaker(new_embedding, candidates_dict, threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return None, 0.0
  
    best_sid = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dict.items():
        if stored_embedding:
            similarity = np.dot(new_embedding, stored_embedding)
            if similarity > best_score:
                best_score = similarity
                best_sid = sid
                
    if best_score >= threshold:
        return best_sid, best_score
    
    return None, best_score
  

def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.65):
    try:
        encoder = get_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        segments = librosa.effects.split(audio, top_db=30)

        identified_results = {}

        for start, end in segments:
            if (end - start) < sr * 0.5:
                continue
            
            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            embedding = encoder.embed_utterance(wav)


            sid, score = identify_speaker(embedding, candidates_dict, threshold)

            if sid:
                if sid not in identified_results or score > identified_results[sid]:
                    identified_results[sid] = score

        return identified_results
    except Exception as e:
        st.error(f'Bulk process error: {e}')
        return {}
    

def process_bulk_audio(audio_bytes, candidates_dict):
    """
    Analyzes classroom audio and matches voices to enrolled students.
    
    Args:
        audio_bytes (bytes): The raw audio recorded from Streamlit.
        candidates_dict (dict): Dictionary mapping {student_id: voice_embedding}.
        
    Returns:
        dict: A mapping of {student_id: confidence_score}.
    """
    detected_scores = {}
    
    # =====================================================================
    # TODO: YOUR AI LOGIC GOES HERE
    # Process `audio_bytes`, extract features, and compare them against 
    # the embeddings in `candidates_dict`.
    # =====================================================================
    
    # ---------------------------------------------------------------------
    # DUMMY LOGIC (Remove this once your AI is ready):
    # This temporarily marks any student who has a voice profile as "Present" 
    # (score 1.0) just so your app works and doesn't crash right now.
    # ---------------------------------------------------------------------
    for student_id, embedding in candidates_dict.items():
        if embedding:
            detected_scores[student_id] = 1.0  # Present
        else:
            detected_scores[student_id] = 0.0  # Absent
            
    return detected_scores