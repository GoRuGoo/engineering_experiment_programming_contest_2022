import simpleaudio


def make_sound(file_path: str) -> None:
    if type(file_path) != str:
        raise ValueError("Enter the string path of the audio file")
    wav_object = simpleaudio.WaveObject.from_wave_file(file_path)
    play_object = wav_object.play()
    play_object.wait_done()
