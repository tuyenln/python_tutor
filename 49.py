class Video:
	def __init__(self, title, link):
		self.title = title
		self.link  = link

class Playlist:
	def __init__(self, name, des, rate, videos):
		self.name = name
		self.des = des
		self.rate = rate
		self.videos = videos

def read_video():
	title = input("Enter title: ")
	link  = input("Enter link: ")
	video = Video(title, link)
	return video

def print_video(video):
	print("Video title: " + video.title , end="")
	print("Video link: " + video.link, end="")

def read_videos():
	videos = []
	total_video = input("Enter how many videos: ")
	total_video = int(total_video)
	for i in range(total_video):
		print("Enter video " + str(i+1))
		vid = read_video()
		videos.append(vid)

	return videos

def print_videos(videos):
	for i in range(len(videos)):
		print_video(videos[i])

def write_video_txt(video, file):
	file.write(video.title + "\n")
	file.write(video.link + "\n")

def write_videos_txt(videos, file):
	total = len(videos)
	file.write(str(total)+ "\n")
	for i in range(total):
		write_video_txt(videos[i], file)

def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_from_txt(file):
	videos = []
	# with open("data.txt", "r") as file:
	total = file.readline()
	for i in range(int(total)):
		video = read_video_from_txt(file)
		videos.append(video)

	return videos


def read_playlist():
	playlist_name = input("Enter playlist name: ")
	playlist_des  = input("Enter playlist description: ")
	playlist_rate  = input("Enter playlist rating(1-5): ")
	videos = read_videos()
	playlist = Playlist(playlist_name, playlist_des, playlist_rate, videos)
	return playlist

def write_playlist_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name + "\n")
		file.write(playlist.des + "\n")
		file.write(playlist.rate + "\n")
		write_videos_txt(playlist.videos, file)
	print("Write successfully playlist to txt")

def read_playlist_from_txt():
	with open("data.txt", "r") as file:
		playlist_name = file.readline();
		playlist_des = file.readline();
		playlist_rate = file.readline();
		playlist_videos = read_videos_from_txt(file)
	playlist = Playlist(playlist_name, playlist_des, playlist_rate, playlist_videos)
	return playlist

def print_playlist(playlist):
	print("Playlist Name " + playlist.name, end="")
	print("Playlist Description " + playlist.des , end="")
	print("Playlist Rating " + playlist.rate , end="")
	print_videos(playlist.videos)



def main():
	playlist = read_playlist()
	write_playlist_txt(playlist)
	playlist = read_playlist_from_txt()
	print_playlist(playlist)

main()