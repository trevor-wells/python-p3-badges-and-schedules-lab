def badge_maker(name):
    return (f'Hello, my name is {name}.')

def batch_badge_creator(names):
    badges = [badge_maker(name) for name in names]
    return badges

def assign_rooms(names):
    rooms = [f'Hello, {name}! You\'ll be assigned to room {index + 1}!' for index, name in enumerate(names)]
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)
