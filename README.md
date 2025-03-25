<div align="center">

# 🎵 STFT5000: A High-Resolution STFT Audio Dataset for AI Research  

📌 **Hosted on Amazon S3:** [STFT5000 Dataset](http://stft5000-0.s3-website-ap-southeast-1.amazonaws.com/)  

🌍 **A dataset of 10,000+ STFT-transformed multilingual audio files for AI research.**  
📊 **Optimized for speech processing, pattern analysis, and deep learning applications.**  

![AWS](https://img.shields.io/badge/AWS-S3-orange?style=for-the-badge&logo=amazonaws&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-%23F7931E.svg?style=for-the-badge&logo=pytorch&logoColor=white)  

</div>

---

## 📖 Overview  
**STFT5000** is a **high-resolution database** of **Short-Time Fourier Transform (STFT) spectrograms** derived from multilingual audio samples. Designed for **AI research, speech processing, and frequency-based machine learning tasks**, it provides a structured repository of **10,000+ spectrograms** optimized for feature extraction and deep learning applications.  

### 🔹 Key Features  
✅ **10,000+ Frequency-Transformed Audio Files**  
✅ **Multilingual Speech & Audio Samples (~10 hours)**  
✅ **Short-Time Fourier Transform (STFT) Spectrograms**  
✅ **Raw & Normalized Versions for AI Applications**  
✅ **Publicly Hosted on AWS S3 for Easy Access**  

---

## 📂 Dataset Structure  
- **raw_spectrograms/** → Original STFT-transformed spectrograms from multilingual speech samples.  
- **normalized_spectrograms/** → Spectrograms processed with normalization for enhanced AI training.

---

## 🚀 Data Generation Process  

1️⃣ **Audio Collection:** Gathered 5,000+ multilingual speech samples (~10 hours).  
2️⃣ **Preprocessing:** Applied noise reduction and standardization.  
3️⃣ **STFT Transformation:** Converted waveforms into **time-frequency representations**.  
4️⃣ **Normalization:** Processed 5,000+ spectrograms to optimize feature extraction.  
5️⃣ **AWS Pipeline:** Stored all processed data on **Amazon S3** for public access.  

---

## 📊 Applications  

🔹 **Speech Recognition & Audio Processing**  
🔹 **AI & Machine Learning Research**  
🔹 **Music Information Retrieval**  
🔹 **Speaker Identification & Speech Synthesis**  
🔹 **Pattern Analysis in Frequency-Domain AI Models**  

---

## 🌐 Accessing the Dataset  

📌 **Publicly available on Amazon S3**:  
[STFT5000 Dataset](http://stft5000-0.s3-website-ap-southeast-1.amazonaws.com/)  

### 🛠️ Download via AWS CLI  

```bash
aws s3 sync s3://stft5000-0 ./STFT5000 --no-sign-request

