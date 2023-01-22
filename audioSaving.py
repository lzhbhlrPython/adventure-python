import wave
import struct

def encode(file_path, audio_path):
    # read binary file and convert to bytes
    with open(file_path, 'rb') as f:
        data = f.read()
    bytes_data = bytearray(data)

    # create wave file and set parameters
    wav_file = wave.open(audio_path, 'w')
    wav_file.setsampwidth(2)
    wav_file.setnchannels(1)
    wav_file.setframerate(44100)

    # convert bytes to audio samples and write to wave file
    for byte in bytes_data:
        sample = struct.pack('h', byte)
        wav_file.writeframesraw(sample)

    wav_file.close()

def decode(audio_path, file_path):
    # read wave file and get audio samples
    wav_file = wave.open(audio_path, 'r')
    samples = wav_file.readframes(wav_file.getnframes())

    # convert samples to bytes and write to binary file
    bytes_data = bytearray()
    for i in range(0, len(samples), 2):
        byte = struct.unpack('h', samples[i:i+2])[0]
        bytes_data.append(byte)

    with open(file_path, 'wb') as f:
        f.write(bytes_data)

    wav_file.close()

encode("LICENSE", "audio.wav")
decode("audio.wav", "LICENSE2")