class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)

    @classmethod
    def show_hall_list(self):
        return self.__hall_list


class Hall(Star_Cinema):

    __hall_count = 0

    def __init__(self, rows, cols) -> None:
        self.seats = {}
        self.rows = rows
        self.cols = cols
        self.hall_no = self.__hall_count + 1
        self.__show_list = []
        self.entry_hall(self)
        super().__init__()

    def entry_show(self, id, movie_name, time):
        show_tuple = (id, movie_name, time)
        self.__show_list.append(show_tuple)
        self.seats[id] = [[0 for i in range(self.cols+1)]
                          for j in range(self.rows+1)]

    def book_seat(self, id, *seats_number_list):
        get_show = None
        for show in self.__show_list:
            if show[0] == id:
                get_show = show

        if get_show:
            for seat in seats_number_list:
                print(f"seat[0][0]---{seat[0][0]} seat[0][1]---{seat[0][1]}")
                if seat[0][0] >= self.rows or seat[0][0] <= 0 or self.rows or seat[0][1] >= self.cols or seat[0][1] <= 0:
                    print(
                        f"the seats of rows{seat[0][0]} and cols {seat[0][1]} valid")
                elif self.seats[id][seat[0][0]][seat[0][1]] == 1:
                    print(
                        f"the seats of rows{seat[0][0]} and cols {seat[0][1]} is not available")
                else:
                    self.seats[id][seat[0][0]][seat[0][1]] = 1
                    print(
                        f'Your seat {seat} is  booked for show {id}.Enjoy your show!!!!!!.')
        else:
            print(f"show with this {id} is wrong.please provide a right id")

    def view_show_list(self):
        for show in self.__show_list:
            print(f"SHOW_ID-{show[0]} MOVIE_NAME-{show[1]} DATE-{show[2]}")
        print('\n')

    def view_available_seats(self, id):
        get_show = None
        for show in self.__show_list:
            if show[0] == id:
                get_show = show

        if get_show:
            for i in range(self.rows):
                for j in range(self.cols):
                    print(f"{self.seats[id][i][j] }", end=" ")
                print("\n")
        else:
            print("It is not a valid show id")


star_cinema = Star_Cinema()

hall1 = Hall(5, 5)
hall1.entry_show(1, 'ROCKETRY', '01-11-23')
hall1.entry_show(2, 'PATHAN', '01-12-23')

while True:
    print("Options:\n")
    print("1: VIEW ALL SHOW")
    print("2: VIEW AVAILABLE TICKETS ")
    print("3: BOOK YOUR TICKET ")
    print("4: EXIT ")

    n = int(input("ENTER OPTION: "))
    hall = hall1
    if (n == 1):
        # TODO:view all show functionality implementation

        hall_list = star_cinema.show_hall_list()
        for hall in hall_list:
            print(hall.view_show_list())

        continue
    elif (n == 2):
        # TODO:view available seats functionality implementation
        showId = int(input("ENTER SHOW ID: "))
        # can show in matrix format
        print(hall1.view_available_seats(showId))
        continue
    elif (n == 3):
        showId = int(input("ENTER SHOW ID: "))
        ticketCount = int(input("Number Of Tickets?: "))
        ticket_list = []
        for i in range(ticketCount):
            rowNo = int(input("Enter Seat Row: "))
            colNo = int(input("Enter Seat Column: "))
            sitNumber = (rowNo, colNo)
            ticket_list.append(sitNumber)

        if len(ticket_list) > 0:
            hall1.book_seat(showId, ticket_list)
        else:
            print(f"you havn't select any sit number")

        continue
    elif (n == 4):
        break
    else:
        print("Please Give Right Instruction...")
