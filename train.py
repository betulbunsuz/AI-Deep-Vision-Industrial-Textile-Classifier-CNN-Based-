import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

def build_industrial_ai_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        layers.MaxPooling2D((2, 2)),

        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),

        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),

        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5), 
        layers.Dense(1, activation='sigmoid') 
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    return model

def prepare_data(data_path):
    train_datagen = ImageDataGenerator(
        rescale=1./255,          
        rotation_range=40,        
        width_shift_range=0.2,    
        height_shift_range=0.2,   
        shear_range=0.2,          
        zoom_range=0.2,          
        horizontal_flip=True,     
        fill_mode='nearest'
    )
  
    print(f"[INFO] Veriler {data_path} adresinden taranıyor...")

if __name__ == "__main__":
   
    textile_ai_model = build_industrial_ai_model()
    
    textile_ai_model.summary()
    
    print("\n[SUCCESS] AI Model mimarisi (CNN) başarıyla oluşturuldu.")
    print("[INFO] Model, endüstriyel kumaş sınıflandırması için eğitilmeye hazır.")
