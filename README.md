# Smart-Device-Control-System

## About the Project

This project is a small and scalable system that handles different devices using OOP concept and python implimentaions. 

The system has two devices at first that are :
Light and Fan
these devices will inherit start() and stop() from the device class.
and we use a genral controller to operate the added devices and we can add new devices to the existing code too.

The oop concept used are:
Inheritance – Motor and Light inherit from the Device class.
Polymorphism – The controller can work with any device by calling the same start() and stop() methods.
Encapsulation – The ON/OFF state is stored inside the device and can only be checked using the provided method.

## Project Structure
Smart-Device-Control-System/

main.py
README.md
.gitignore

## Requirements
Python 3.x

## How to Run

Clone the repository:

git clone https://github.com/viswamanav/Smart-Device-Control-System.git

Go to the project folder:

cd Smart-Device-Control-System

Run the program:

python main.py

## Expected Output
Motor has started
Motor has stopped
Light switched on
Light switched off
