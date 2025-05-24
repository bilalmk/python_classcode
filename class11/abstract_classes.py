from abc import ABC, abstractmethod


class Electronics(ABC):
    @abstractmethod
    def on(self):
        print("device turn on")

    @abstractmethod
    def off(self):
        print("device turn off")

    def work(self):
        print("device is working")


class TV(Electronics):
    def on(self):
        print("tv turn on")

    def off(self):
        print("tv turned off")
        
    def tv_work(self):
        print("watch movie")


class Radio(Electronics):
    def radio_start(self):
        print("radio turn on")

    def on(self):
        print("radio turn on")
    def off(self):
        print("radio turned off")


tv = TV()
radio = Radio()

tv.on()
