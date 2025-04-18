# AI Voice AutoLihgt System

## Repo Structure

```
    ├── docs                                   # Contains documents.
    ├── research                               # Contains pre-research experiments.
    ├── source                                 # Contains project source code.
    │   ├── modules                                # Contains custom dependencies.  
    │   ├── main.py                                # main file.
    └── README.MD                              # Readme Content.
```

## 01 Introduction

This is an automated lighting control system that operates automatically and is powered by Arduino and Artificial Intelligence. It utilizes AI technology to recognize speech and automate lighting operations. The system uses the Firmata protocol to enable Python to communicate with Arduino, thereby turning on LEDs with the help of speech recognition technology.

![Circuit Diagram](docs/media/0-banner-image.png)

## 02 Technology Stack

### 2.1 Hardware Stack

- Arduino UNO
- LED: Red, Green, Blue
- Full Bread Board
- Jumper Wires

### 2.2 Software Stack

- Python 3.8.5 (Recommended)
- Arduino IDE (Framework)
- SpeechRecognition
- PyAudio
- PyFirmata

## 03 Setup

### 3.1 Hardware Setup

![Circuit Diagram](docs/media/1-circuit-diagram.png)

| LEDs          | Pin No  |
| ------------- | ------- |
| **RED LED**   | Pin: 13 |
| **Green LED** | Pin: 12 |
| **Blue LED**  | Pin: 11 |

### 3.2 Firmware Setup

Setting up the Arduino firmware is necessary to enable communication between Python and Arduino. The Firmata protocol establishes serial communication between a Python script and an Arduino.

To upload Firmata, open Arduino IDE and choose the correct COM port and **File -> Examples -> Firmata -> StandardFirmata -> Upload to Arduino UNO Board**.

![Firmware Setup](docs/media/2-firmware-setup.png)

**Note:** After uploading StandardFirmata to the Arduino Board, Python can be used to program it.

### 3.3 Setup Software

We will now install the necessary tools to gain access to the Arduino Board. This project utilizes essential libraries, including Speech Recognition and PyFirmata. We need to install all the required dependencies on the development computer.

- **Step 01:** Install Python

  ```
  Ver: 3.8.5 is Recommended (www.python.org)
  ```

- **Step 02:** Navigate to the specified location in CMD/Terminal.

  ```
  ai-speech-autolight-system/docs/requirements.txt
  ```

- **Step 03:** Execute the given command to install all dependencies.

  ```
  pip install -r requirements.txt
  ```

## 04 Usage

- **Source Directory:**

  ```
  ai-speech-autolight-system\source\main.py
  ```

### 4.1 Setps to run

- **Step 01:** Connect the Arduino to the development computer.

- **Step 02:** Modify the script to reflect the appropriate COM port.

  ![Change COM Port](docs/media/3-change-com-port.png)

- **Step 03:** Run app.

  ```
  python source/main.py
  ```

### 4.2 Output

[4-demo-video.webm](https://github.com/gunarakulangunaretnam/ai-speech-autolight-system/assets/45822509/9ef5b3f7-ffd7-4c2d-92b6-1e402a64fe6d)


# Contact

### 🌐 Website:
[![Visit](https://img.shields.io/badge/Visit%3A%20www.mpowerr.com-%23007ACC?style=flat&logo=google-chrome&logoColor=white&labelWidth=200)](https://www.mpowerr.com)

---

### 📱 Social Media:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/mpowerr-info)
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/mpowerr.info)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/mpowerr.info)
[![X (Twitter)](https://img.shields.io/badge/X-%231DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/MpowerrInfo)
[![TikTok](https://img.shields.io/badge/TikTok-%23000000?style=for-the-badge&logo=tiktok&logoColor=white)](https://www.tiktok.com/@mpowerr.info)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@mpowerrinfo)

---
