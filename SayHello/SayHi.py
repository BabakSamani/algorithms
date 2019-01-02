import os


def main():
    # First get the list of available voices in the machine
    # os.system("say -v ? >> voices.txt")
    voice_list_file = open("voices.txt", 'r')
    # Read the text file contains the voices
    with voice_list_file as input_file:
        voices = input_file.readlines()

    for v in voices:
        voice_detail = v.split('#')
        person_lang = voice_detail[0].split()
        person = person_lang[0]
        lang = person_lang[1]
        os.system("echo 'Hello' in " + lang)
        os.system('say -v "' + person + '" "Hello" -o recording.aiff')


if __name__ == "__main__":
    main()
