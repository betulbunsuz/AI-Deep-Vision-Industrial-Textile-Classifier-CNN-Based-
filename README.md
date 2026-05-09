# AI-Deep-Vision-Industrial-Textile-Classifier-CNN-Based-
🧠 AI-Deep-Vision: Industrial Textile Classifier (CNN Based)
Bu proje, tekstil endüstrisinde kalite kontrol süreçlerini otomatize etmek amacıyla geliştirilmiş bir Yapay Zeka çalışmasıdır. Projenin temel odağı, derin öğrenme algoritmalarını kullanarak kumaş yapılarını (örneğin: Örme ve Dokuma) yüksek doğrulukla sınıflandırmaktır.

🚀 Proje Hakkında
Geleneksel kalite kontrol süreçleri insan hatasına açıktır. Bu projede kullanılan Evrişimli Sinir Ağları (CNN) mimarisi, kumaş desenlerini mikroskobik düzeyde analiz ederek manuel denetimin yerine geçebilecek dijital bir alternatif sunar. Bu çalışma, Sanayi 4.0 ve akıllı fabrikalar için bir prototip niteliğindedir.

🛠️ Yapay Zeka Mimarisi ve Teknoloji
Projenin kalbinde, görsel verilerden özellik çıkarımı (feature extraction) yapan çok katmanlı bir derin öğrenme modeli yer almaktadır:

Mimari: Convolutional Neural Networks (CNN)

Katmanlar: Özellik belirleme için Conv2D ve MaxPooling katmanları, sınıflandırma için ise Dense ve Dropout katmanları kullanılmıştır.

Kütüphaneler: Python, TensorFlow, Keras, OpenCV ve NumPy.

Veri Artırma (Data Augmentation): Modelin farklı ışık ve açılarda da çalışabilmesi için döndürme, yakınlaştırma ve yatay çevirme teknikleri uygulanmıştır.

├── train.py/                 # CNN model mimarisi ve eğitim kodları (Python)
├── orme.jpeg-dokuma.jpeg/             # Örme ve Dokuma kumaş örnek görselleri (Örnekler)
├── models/              # Eğitilmiş model dosyaları (.h5)
|---requirements.txt      # Kütüphaneler
└── README.md            # Proje dökümantasyonu
📊 Performans ve Sonuçlar
Yapılan testlerde model, test veri seti üzerinde %92 doğruluk (accuracy) oranına ulaşmıştır. Sonuçlar, karmaşıklık matrisi (confusion matrix) üzerinden analiz edilerek endüstriyel kararlarda güvenilirlik sağlanmıştır.

💻 Kurulum
Depoyu klonlayın: git clone [https://github.com/kullaniciadi/AI-Deep-Vision-Textile.git](https://github.com/betulbunsuz/AI-Deep-Vision-Textile.git)

Gerekli kütüphaneleri yükleyin: pip install -r requirements.txt

Eğitimi başlatın: python src/train.py

Proje eğitimi için kullanılan geniş veri seti, boyut kısıtlamaları nedeniyle repoya dahil edilmemiştir. Klasör içinde örnek teşkil etmesi amacıyla sınırlı sayıda görsel bulunmaktadır.
