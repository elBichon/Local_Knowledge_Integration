# Local_Knowledge_Integration

###### Local Knowledge Integration is a suite of different image processing tools (face detection, color detection, classification...) that perform analysis on a video stream coming from an ip camera for a cisco internal innovation contest.
![alt text](https://raw.githubusercontent.com/elBichon/Local_Knowledge_Integration/master/test.png)
## Motivation: 
The project is to extract as much info as possible from a livestream through a portable interface (android smartphone) that can be reused for later purposes or for direct action and analysis given a certain set of triggers
## Tech/Frameworks used:
- [keras](https://keras.io/)
- [opencv](https://opencv.org/)
- [dlib](http://dlib.net/)
- [python](https://github.com/opencv/opencv/tree/master/data/haarcascades)

## Project Structure:
- tets_dlib.py
- utils.py

## Features:
- [x] Interfacing with android ip webcam on smartphone through python
- [x] Creating a picture for each of the detected boxes
- [x] For the face picture make it go through a cnn to extract emotion
- [x] Counting number of persons going through (in case of a building apply recognition for people going in and out)
- [ ] Correction of parralax
- [ ] Extracting age
- [ ] Extracting gender
- [ ] 5_o_Clock_Shadow
- [ ] Arched_Eyebrows 
- [ ] Bags_Under_Eyes
- [ ] Bald
- [ ] Bangs 
- [ ] Big_Lips 
- [ ] Big_Nose 
- [ ] Black_Hair 
- [ ] Blond_Hair
- [ ] Brown_Hair 
- [ ] Bushy_Eyebrows 
- [ ] Chubby
- [ ] Double_Chin  
- [ ] Eyeglasses 
- [ ] Goatee
- [ ] Gray_Hair 
- [ ] Heavy_Makeup 
- [ ] High_Cheekbones
- [ ] Mouth_Slightly_Open 
- [ ] Mustache
- [ ] Narrow_Eyes 
- [ ] No_Beard    
- [ ] Oval_Face 
- [ ] Pale_Skin 
- [ ] Pointy_Nose 
- [ ] Receding_Hairline
- [ ] Rosy_Cheeks
- [ ] Sideburns
- [ ] Smiling
- [ ] Tone analysis
- [ ] Text to speech
- [ ] Novelty detection
- [ ] Real time insight and actions given certain triggers
- [ ] Post time analysis

## Workflow:
1. Connecting to the ip webcam through your local network

## How to use:

