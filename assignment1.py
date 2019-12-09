import csv

def csv_process(filepath):
    movie = []
    with open(filepath,mode='r',encoding='utf-8',newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            movie.append(row)
            movie = sorted(movie, key=lambda x: (int(x[1]), x[0]))
    return movie, len(movie)



def print_menu():
    print('Menu:')
    print('L - List movies')
    print('A - Add new movie')
    print('W - Watch a movie')
    print('Q - Quit')


def main():
    """..."""
    print("Movies To Watch 1.0 - by <Your Name>")
    movie, num = csv_process('./movies.csv')

    #print information
    print('{} movies loaded'.format(num))
    print_menu()
    for i in range(len(movie)):
        for j in range(len(movie[0])):
            print(movie[i][j]+ ',', end=' ')
            if j == (len(movie[0])-1):
                print('\n')

    while(1):
        while(1):
            choice = input(">>> ").upper()
            if (choice != 'L') and (choice != 'W') and (choice != 'A') and (choice != 'Q'):
                print('Invalid menu choice')
                print_menu()
                continue
            else:
                break


        while (choice == "L"):
            num_w = 0
            num_u = 0
            for i in range(len(movie)):
                if movie[i][3]=='w':
                    num_w += 1
                    print('{0:10}.{4:3}{1:<36}-{2:>6} ({3:})'.format(i, movie[i][0], movie[i][1], movie[i][2], ' *'))
                if movie[i][3]=='u':
                    num_u += 1
                    print('{0:10}.{4:3}{1:<36}-{2:>6} ({3:})'.format(i, movie[i][0], movie[i][1], movie[i][2], ' '))

            print('{} movies watched, {} movies still to watch'.format(num_w, num_u))

            print_menu()
            break

        while (choice == "W"):
            flag = 0
            for i in range(len(movie)):
                if movie[i][3] == 'u':
                    flag = 1
            if flag == 0:
                print('No more movies to watch!')
                print_menu()
                break


            print('Enter the number of a movie to mark as watched')

            while(1):
                try:
                    choice_movie = int(input(">>> ").upper())
                except:
                    print('Invalid input; enter a valid number')
                    continue

                if choice_movie < 0:
                    print('Number must be >= 0')
                    continue

                if choice_movie > (num-1):
                    print('Invalid movie number')
                    continue

                if (choice_movie>=0) and (choice_movie<num):
                    if movie[choice_movie][3] == 'u':
                        movie[choice_movie][3] = 'w'
                        print('{} from {} watched'.format(movie[choice_movie][0], movie[choice_movie][1]))

                    if movie[choice_movie][3] == 'w':
                        print('You have already watched {}'.format(movie[choice_movie][0]))

                    print_menu()
                    break
                    break

                else:
                    print('No more movies to watch!')

                    print_menu()
                    break
            break

        while (choice == "A"):
            while(1):
                title = input("Title: ")
                if title == '':
                    print('Input can not be blank')
                    continue
                else:
                    break
            while(1):
                try:
                    year = int(input("year: "))
                except:
                    print('Invalid input; enter a valid number')
                    continue
                if year < 0:
                    print('Number must be >= 0')
                    continue
                else:
                    break
            while(1):
                category = input("Category: ")
                if category == '':
                    print('Input can not be blank')
                    continue
                else:
                    break

            print('{} {} from {} added to movie list'.format(title, category, year))
            movie.append([title, year, category, 'u'])


            print_menu()
            break

        while (choice == "Q"):
            movie_num = num
            csvFile = open("./movies.csv", "w")
            writer = csv.writer(csvFile)
            for i in range(len(movie)):
                writer.writerow(movie[i])
            csvFile.close()
            print('{} movies saved to movies.csv'.format(movie_num))
            print('Have a nice day :)')
            break
            break



if __name__ == '__main__':
    main()

