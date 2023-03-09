import click
#import pyaudio
import wave
import os

from playsound import playsound
@click.command()
@click.option("-t", default=1, help="Number of greetings.")
@click.option("-c", default=1, help="Number of greetings.")
def hello(t,c):
    if t == 1:
        playsound("code.wav")
    elif t == 2:
        playsound("audio.mp3")
    elif t == 3:
        chunk = 1024 # Запись кусками по 1024 сэмпла
        sample_format = pyaudio.paInt16 # 16 бит на выборку
        channels = 2
        rate = 44100 # Запись со скоростью 44100 выборок(samples) в секунду
        seconds = 5
        filename = "code"+str(c)+".wav"
        p = pyaudio.PyAudio() # Создать интерфейс для PortAudio

        print('Recording...')

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=rate,
                        frames_per_buffer=chunk,
                        input_device_index=1, # индекс устройства с которого будет идти запись звука 
                        input=True)

        frames = [] # Инициализировать массив для хранения кадров

        # Хранить данные в блоках в течение 3 секунд
        for i in range(0, int(rate / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Остановить и закрыть поток
        stream.stop_stream()
        stream.close()
        # Завершить интерфейс PortAudio
        p.terminate()

        print('Finished recording!')

        # Сохранить записанные данные в виде файла WAV
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        os.system("mkdir data"+str(c)+"")
        os.system("move "+filename+" data"+str(c)+"/"+filename+"")
    elif t == 4:
        chunk = 1024 # Запись кусками по 1024 сэмпла
        sample_format = pyaudio.paInt16 # 16 бит на выборку
        channels = 2
        rate = 44100 # Запись со скоростью 44100 выборок(samples) в секунду
        seconds = 5
        filename = "reading"+str(c)+".wav"
        p = pyaudio.PyAudio() # Создать интерфейс для PortAudio

        print('Recording...')

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=rate,
                        frames_per_buffer=chunk,
                        input_device_index=1, # индекс устройства с которого будет идти запись звука 
                        input=True)

        frames = [] # Инициализировать массив для хранения кадров

        # Хранить данные в блоках в течение 3 секунд
        for i in range(0, int(rate / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Остановить и закрыть поток
        stream.stop_stream()
        stream.close()
        # Завершить интерфейс PortAudio
        p.terminate()

        print('Finished recording!')

        # Сохранить записанные данные в виде файла WAV
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        os.system("mkdir data"+str(c)+"")
        os.system("move "+filename+" data"+str(c)+"/"+filename+"")
    elif t == 5:
        chunk = 1024 # Запись кусками по 1024 сэмпла
        sample_format = pyaudio.paInt16 # 16 бит на выборку
        channels = 2
        rate = 44100 # Запись со скоростью 44100 выборок(samples) в секунду
        seconds = 5
        filename = "picture"+str(c)+".wav"
        p = pyaudio.PyAudio() # Создать интерфейс для PortAudio

        print('Recording...')

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=rate,
                        frames_per_buffer=chunk,
                        input_device_index=1, # индекс устройства с которого будет идти запись звука 
                        input=True)

        frames = [] # Инициализировать массив для хранения кадров

        # Хранить данные в блоках в течение 3 секунд
        for i in range(0, int(rate / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Остановить и закрыть поток
        stream.stop_stream()
        stream.close()
        # Завершить интерфейс PortAudio
        p.terminate()

        print('Finished recording!')

        # Сохранить записанные данные в виде файла WAV
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        os.system("mkdir data"+str(c)+"")
        os.system("move "+filename+" data"+str(c)+"/"+filename+"")
    

if __name__ == '__main__':
    hello()