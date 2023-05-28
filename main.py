from pytube import YouTube
MAX_LENGTH = 100

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
        print("Download is completed successfully\n")
    except:
        print("An error has occurred")
        print("Download is not completed!")

def main():
    var = []
    banyak = int(input("Masukkan banyak: "))

    for i in range(banyak):
        print("Masukkan url ke", i+1, ": ", end="")
        string = input()
        var.append(string)
  	
    for string in var:
        print(string)
        print("Downloading...")
        Download(string)

if __name__ == "__main__":
    main()
