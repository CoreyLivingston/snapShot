# SnapShot

This is a sample AWS DeepLens project that makes use of IoT devices to trigger image capture & tagging for later use in machine learning model training.

## Why?

When it comes to machine learning, it's all about the data. Well trained models require large quantities of reliable data. After AWS Re:Invent 2017, I found myself wondering how to obtain large quantities of reliably tagged images for machine learning. There are existing data sets for machine learning (http://deeplearning.net/datasets/), but how can I automate the gathering of data about my daily life? Or perhaps a larger goal of encouraging the contribution of reliably tagged images to a central source.

This project was developed to encourage capturing accurately tagged images for machine learning based on input from IoT sensors.





## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites





Problem: To train a model, large quantities of input is needed.

Proposed Solution: Use IoT triggers to collect data for modeling.

Sample Use Case: We'd like to be able to use machine learning to tell if a basketball shot was successful. We'll use an IR sensor to determine successful shots.



## Components

* DeepLens
* AWS IoT
* MongooseOS

ESPRESSIF ESP32 DEVELOPMENT BOARD - https://www.adafruit.com/product/3269
ENCLOSED PIEZO ELEMENT - https://www.adafruit.com/product/1739
IR Break Beam Sensor - https://www.adafruit.com/product/2167

#HOWTO deeplens

* Greengrass IoT Device trigger image save
* DeepLens Play sound based on [image recognition?][iot device?]
* DeepLens gif maker


What is snapshot?

components?

PArts list:




### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Corey Livingston**


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc





My Notes:
  Step 1: Ship a photo to S3 based on MQTT message - we can use the IoT Console
  Step 2: Use an IoT device to send the MQTT message via greengrass
  Step 3: Multi Sensors trigger different photos
  Step 4: Multi Sensors trigger storage of a serries of photos
  Step 5: Alexa triggers gif generator
