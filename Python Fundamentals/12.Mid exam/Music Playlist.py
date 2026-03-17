songs = input().split()
n = int(input())
deleted_songs = []
for i in range(n):
    command = input().split(" * ")

    if command[0] == "Add Song":
        if command[1] not in songs:
            songs.append(command[1])
            print(f"{command[1]} successfully added")
    elif command[0] == "Delete Song":
        index = int(command[1])
        if len(songs) > index:
            deleted_songs.extend(songs[0:index])
            del songs[0:index]

            print(", ".join(deleted_songs) + " deleted")
    elif command[0] == "Shuffle Songs":
        first_index = int(command[1])
        second_index = int(command[2])
        if 0 <= first_index < len(songs) and 0 <= second_index < len(songs):
            songs[first_index], songs[second_index] = songs[second_index], songs[first_index]
            print(f"{songs[first_index]} is swapped with {songs[second_index]}")

    elif command[0] == "Insert":
        song = command[1]
        index = int(command[2])
        if 0 <= index < len(songs):
            if song not in songs:
                songs.insert(index, song)
                print(f"{song} successfully inserted")
            else:
                print("Song is already in the playlist")
        else:
            print("Index out of range")
    elif command[0] == "Sort":
        songs.sort(reverse=True)
    elif command[0] == "Play":
        print("Songs to Play:")
        print("\n".join(songs))
