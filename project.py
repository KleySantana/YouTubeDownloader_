import sys
from pytube import YouTube


def main():
    link = input("Enter link to download: ").strip()
    title, resolutions = processing(link)

    # Promt the user for their desired video resolution
    res = get_resolution(resolutions)

    confirmation = input(
        f"\n{title} - {res[1]} (Aprox. {round(res[2])} Mb)\nAre you sure you want to download it? (Yes/No) ").strip().lower()
    match confirmation:
        case "yes" | "y":
            pass
        case "no" | "n":
            main()
        case _:
            sys.exit("Invalid answer")

    if download(link, res):
        print("\nSuccessful Download")


def processing(link):
    """create a YouTube object and information about it"""
    try:
        item = YouTube(link)
    except:
        raise ValueError("Invalid YouTube link format")

    # Get all of the available resolutions and its respective mb sizes
    resolutions = {}
    for stream in item.streams:
        if stream.mime_type == "video/mp4":
            resolutions[stream.itag] = [stream.resolution, stream.filesize_mb]
    title = item.title
    sorted_resolutions = dict(sorted(resolutions.items(), key=lambda x: int(x[1][0][:-1])))

    return title, sorted_resolutions


def get_resolution(resolutions):
    print("\n--- Resolutions available: ---\n")

    i = 1
    res_ids = []
    for res_id, (res, size) in resolutions.items():
        print(f"{i}. {res} - Aprox. {round(size)} Mb")
        i += 1
        res_ids.append([res_id, res, size])
    choice = ask_res()

    return res_ids[int(choice) - 1]


def ask_res(default=""):
    if default:
        return default
    else:
        return input("\nChoose a resolution: ")


def download(link, chosen):
    """handles the downloading"""

    # Create an YouTube object with the chosen video
    try:
        video = YouTube(link, on_progress_callback=progress)
        video = video.streams.get_by_itag(chosen[0])
        video.download()
        return True
    except:
        sys.exit("Error. Try again later.")


def progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_complete = (bytes_downloaded / total_size) * 100
    sys.stdout.write("\rDownloading: {:.2f}%".format(percent_complete))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
