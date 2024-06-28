from pydub import AudioSegment
f="output.mp3"
# Open the sound file
sound = AudioSegment.from_mp3(f)

# Play the sound
sound.play()