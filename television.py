class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''this section gives the default values for the tv'''
        self.__status = False
        self.__muted = False
        self.__volume = 0
        self.__channel = 0

    def power(self):
        '''this section turns the tv on and off'''
        self.__status = not self.__status

    def mute(self):
        '''this will turn the volume all the way down'''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
       '''this is used to go up in the channels'''
       if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
               self.__channel += 1
            else:
               self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        ''' this is used for going down in channels'''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL


    def volume_up(self):
        '''to turn the volume up louder'''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1


    def volume_down(self):
        '''to turn the volume down lower'''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        return (f' Power = {self.__status}, '
                f' Channel = {self.__channel}'
                f' Volume = {0 if self.__muted else self.__volume}')