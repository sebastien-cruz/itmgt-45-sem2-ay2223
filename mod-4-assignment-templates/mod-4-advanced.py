'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    social_graph = {
    "@bongolpoc": {"first_name": "Joselito",
                   "last_name": "Olpoc",
                   "following": []
                   },
    "@joaquin": {"first_name": "Joaquin",
                 "last_name": "Gonzales",
                 "following": ["@chums", "@jobenilagan"]
                 },
    "@chums": {"first_name": "Matthew",
               "last_name": "Uy",
               "following": ["@bongolpoc", "@miketan", "@rudyang", "@joeilagan"]
               },
    "@jobenilagan": {"first_name": "Joben",
                     "last_name": "Ilagan",
                     "following": ["@eeebeee", "@joeilagan", "@chums", "@joaquin"]
                     },
    "@joeilagan": {"first_name": "Joe",
                   "last_name": "Ilagan",
                   "following": ["@eeebeee", "@jobenilagan", "@chums"]
                   },
    "@eeebeee": {"first_name": "Elizabeth",
                 "last_name": "Ilagan",
                 "following": ["@jobenilagan", "@joeilagan"]
                 },
}
    if from_member not in social_graph or to_member not in social_graph:
        return "no relationship"
    elif to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        
        return "no relationship"


#Tic Tac Toe List below 


board = [     [         ['X','X','O'],
         ['O','X','O'],
         ['O','','X']
    ],
     [         ['X','X','O'],
         ['O','X','O'],
         ['','O','X']
     ],
     [         ['O','X','O'],
         ['','O','X'],
         ['X','X','O']
     ],
     [         ['X','X','X'],
         ['O','X','O'],
         ['O','','O']
     ],
     [         ['X','X','O'],
         ['O','X','O'],
         ['X','','O']
     ],
     [         ['X','X','O'],
         ['O','X','O'],
         ['X','','']
     ],
     [         ['X','X','O',''],
         ['O','X','O','O'],
         ['X','','','O'],
         ['O','X','','']
     ]
    ]
def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    #Call the function >>>tic_tac_toe(board[0])
    for row in board:
        if len(set(row)) == 1 and row[0] != '':
            return row[0]

    for col in range(len(board)):
        column_values = []
        for row in range(len(board)):
            column_values.append(board[row][col])
        if len(set(column_values)) == 1 and column_values[0] != '':
            return column_values[0]

    diagonal1_values = []
    diagonal2_values = []
    for i in range(len(board)):
        diagonal1_values.append(board[i][i])
        diagonal2_values.append(board[i][len(board)-i-1])
    if len(set(diagonal1_values)) == 1 and diagonal1_values[0] != '':
        return diagonal1_values[0]
    if len(set(diagonal2_values)) == 1 and diagonal2_values[0] != '':
        return diagonal2_values[0]

    return 'NO WINNER'


    

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    #Call the function using eta(first_stop, second_stop, legs)
    total_travel_time = 0
    found_first_stop = False

    for leg, leg_data in route_map.items():
        if leg[0] == first_stop:
            found_first_stop = True
            total_travel_time += leg_data['travel_time_mins']
            if leg[1] == second_stop:
                return total_travel_time
        elif found_first_stop and leg[1] == second_stop:
            total_travel_time += leg_data['travel_time_mins']
            return total_travel_time




# Sample data for ETA
legs = {
    ("upd", "admu"): {
        "travel_time_mins": 10
    },
    ("admu", "dlsu"): {
        "travel_time_mins": 35
    },
    ("dlsu", "upd"): {
        "travel_time_mins": 55
    }
}
