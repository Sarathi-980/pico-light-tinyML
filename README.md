# pico-light-tinyML
A tinyML demonstration project using Raspberry Pi Pico and a light sensor.

This project demonstrates complete tinyML workflow:
    collecting sensor data,
    training lightweight machine learning model in Python,
    deploying learned decision boudaries to a Raspberry Pi Pico for edge process

## Project Objective
The objective of this project is to classify light intensity into:
    DARK
    NORMAL
    BRIGHT
using lightweight model that can run directly on a microcontroller

### Hardware used
    Rasbperry Pi Pico
    Light Sensor Module
    Breadboard
    USB and jumper

### Software used
    MicrPython
    Python
    Pandas
    Scikit-learn
    Thonny IDE

### Model Training
    Decision tree classifier trained using scikit-learn.

    Training command:
        python training/model_train.py
        The trained model generates decision boundaries based on sensor data set.

        output:
        (.venv) sarazz001@Sarah:~/projects/pico-light-tinyML$ python training/model_train.py 
        |--- raw_adc <= 14250.00
        |   |--- class: DARK
        |--- raw_adc >  14250.00
        |   |--- raw_adc <= 45500.00
        |   |   |--- class: NORMAL
        |   |--- raw_adc >  45500.00
        |   |   |--- class: BRIGHT
        
### Edge deployment
    The learned decision boundaries are deployed to Rasbperry Pi Pico in a lightweight inference function in model.py.
    This approach eliminates cloud processing and enables real-time edge inference.