import simpleaudio

wav_obj = simpleaudio.WaveObject.from_wave_file("suisei_amayakasi_trim.wav")
play_obj = wav_obj.play()
play_obj.wait_done()
