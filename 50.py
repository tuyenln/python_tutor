import webbrowser

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link  = link
		self.seen  = False

	def open(self):
		webbrowser.open(self.link)
		self.seen  = True

class Playlist:
	def __init__(self, name, des, rate, videos):
		self.name = name
		self.des = des
		self.rate = rate
		self.videos = videos

def read_video():
	title = input("Enter title: ") + "\n"
	link  = input("Enter link: ") + "\n"
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
		print("video : " + str(i+1))
		print_video(videos[i])

def write_video_txt(video, file):
	file.write(video.title)
	file.write(video.link)

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
	playlist_name = input("Enter playlist name: ") + "\n"
	playlist_des  = input("Enter playlist description: ") + "\n"
	playlist_rate  = input("Enter playlist rating(1-5): ") + "\n"
	videos = read_videos()
	playlist = Playlist(playlist_name, playlist_des, playlist_rate, videos)
	return playlist

def write_playlist_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name)
		file.write(playlist.des)
		file.write(playlist.rate)
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
	print("Playlist Name: " + playlist.name, end="")
	print("Playlist Description: " + playlist.des , end="")
	print("Playlist Rating: " + playlist.rate , end="")
	print_videos(playlist.videos)

def show_menu():
	print("Main Menu :")
	print("-----------------------------")
	print("| Option 1: Create playlist |")
	print("| Option 2: Show playlist   |")
	print("| Option 3: Play a video    |")
	print("| Option 4: Add a video     |")
	print("| Option 5: update playlist |")
	print("| Option 6: remove video    |")
	print("| Option 7: Save and Exit   |")
	print("-----------------------------")

def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(prompt)
	choice = int(choice)
	return choice

def play_video(playlist):
	print_videos(playlist.videos)
	total = len(playlist.videos)
	choice = select_in_range("Select a video (1," +str(total) + "): " , 1, total)
	print("Open video : " + playlist.videos[choice-1].title + " - " + playlist.videos[choice-1].link , end="")
	playlist.videos[choice-1].open()
	# webbrowser.open(playlist.videos[choice-1].link, new=2)

def add_video(playlist):
	print("Enter new video info:")
	new_title = input("Add your video title: ") + "\n"
	new_link = input("Add your video link: ") + "\n"
	new_video = Video(new_title, new_link)
	playlist.videos.append(new_video)
	return playlist

def update_playlist(playlist):
	print("Enter your playlist info:")
	print("1. Name")
	print("2. Description")
	print("3. Rating")

	choice = select_in_range("Please choose your update item (1-3): ", 1,3)
	if choice == 1:
		name = input("New playlist name: ") + "\n"
		playlist.name = name
		print("Update successfully")
		return playlist
	if choice == 2:
		des = input("New playlist description: ") + "\n"
		playlist.des = des
		print("Update successfully")
		return playlist
	if choice == 3:
		rate = str(select_in_range("Set your rating (1-5): ", 1,5)) + "\n"
		playlist.rate = rate
		print("Update successfully")
		return playlist

def remove_video(playlist):
	print_videos(playlist.videos)
	choice = select_in_range("Enter video to delete", 1, len(playlist.videos))
	# del playlist.videos[choice-1]
	new_list = []

	for i in range (len(playlist.videos)):
		if i == choice-1:
			continue
		new_list.append(playlist.videos[i])
	playlist.videos = new_list
	print("Delete successfully !")
	return playlist

def main():

	try:
		playlist = read_playlist_from_txt()
		print("Data load successfully")
	except:
		print("Welcome first time !")

	while True:
		show_menu()
		choice = select_in_range("Select an option (1-7):", 1, 7)
		if choice == 1:
			playlist = read_playlist()
			input("Press Enter to continue. \n")
		elif choice == 2:
			print_playlist(playlist)
			input("Press Enter to continue. \n")
		elif choice == 3:
			play_video(playlist)
			input("Press Enter to continue. \n")
		elif choice == 4:
			playlist = add_video(playlist)
			input("Press Enter to continue. \n")
		elif choice == 5:
			playlist = update_playlist(playlist)
			input("Press Enter to continue. \n")
		elif choice == 6:
			playlist = remove_video(playlist)
			input("Press Enter to continue. \n")
		elif choice == 7:
			write_playlist_txt(playlist)
			input("Press Enter to continue. \n")
			break

main()





