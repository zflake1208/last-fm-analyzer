from apiClients import album

print("Enter album: ")
alb = input()
print("Enter artist: ")
artist = input()

query = album.get_info(artist, alb)
print(query)