

<p align="center">
<img src="guardian.png" width=500>

2019 AngelHack Hackathon - Seattle, WA - July 2019

### Motivation
According to FBI statistics, violent crime in the Seattle area is currently over 65% higher than the national average. Over 61% of women regularly take steps to avoid being sexually assaulted according to YouGov surveys. How can we take steps to make people feel safe and secure?

#### Team
* Abhi Banerjee
* Diane Chiang
* Earl Jay Caoile
* Brandon Yu
* Adrienne Lim

### Our Project
Guardian is your personal emergency broadcast system that allows you to send text alerts to your closest friends & family with your location and a link to a live video broadcast during a dangerous encounter. It uses the Agora RTC platform in conjunction with Machine Learning & Deep Learning modules in AWS and Keras to provide a platform for multimodal sentiment analysis for legal cadence.

### Unique Features
* Facial Expression Sentiment Analysis via AWS Rekognition
* Real-time video broadcasting to your friends & family
* Video to Audio via ffmpeg (Python)
* Audio to Text via AWS Transcribe
* Text Sentiment Classifer using RNN via Keras (Python)

### Links
- Presentation Slides: http://bit.ly/2XLF4id
- GitHub: https://github.com/drunkONdata/guardian

### Future Work
* Validate multimodal sentiment models with labeled datasets to establish baseline accuracy
* Deploy "Descrete" mode to broadcast audio or video
* Utilize AWS Kinesis module to handle live video & audio streams
* Leverage Amazon Comprehend for Text Sentiment Analysis
* Real-time transcription with Amazon Transcribe
