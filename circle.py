class Person(object):

    def __init__(self, num):
        self.num = num
        self.left_hand = None
        self.right_hand = None

    def __next__(self):
        return self.left_hand

    def quit(self):
        self.right_hand.left_hand = self.left_hand
        self.left_hand.right_hand = self.right_hand

    def is_last(self):

        return True if self.num == self.left_hand.num else False


class Circle(object):

    def __init__(self, num_of_personnel):
        self.root = None
        self.num_of_personnel = num_of_personnel
        self.create_circle()

    def create_circle(self):
        self.root = Person(1)

        cursor = self.root
        for i in range(1, self.num_of_personnel):
            cursor.left_hand = Person(i + 1)
            cursor.left_hand.right_hand = cursor
            cursor = next(cursor)

        cursor.left_hand = self.root
        self.root.right_hand = cursor

    def goto_start_point(self, start_num: int) -> Person:
        cursor = self.root
        if not isinstance(start_num, int):
            raise TypeError
        if start_num < 1 or start_num > self.num_of_personnel:
            raise

        while cursor.num != start_num:
            cursor = next(cursor)

        return cursor

    def start_num_off(self, interval:int, start_from=1) -> Person:
        cursor = self.goto_start_point(start_from)

        while not cursor.is_last():

            i = 1
            while i < interval:
                print('No. {}'.format(cursor.num))
                cursor = next(cursor)
                i += 1

            print('No.{} quit'.format(cursor.num))
            cursor.quit()
            cursor = next(cursor)

        return cursor


if __name__ == '__main__':

    total = 10
    interval = 3

    game = Circle(total)
    last_personnel = game.start_num_off(interval)
    print('last person is: {}'.format(last_personnel.num))

# if __name__ == '__main__':
#     people = [Person(i + 1) for i in range(total)]
#
#     for i in range(total - 1):
#         people[i].next_person = people[i + 1]
#         people[i + 1].prev_person = people[i]
#     people[-1].next_person = people[0]
#     people[0].prev_person = people[-1]
#
#     current = people[0]
#
#     while not current.is_last():
#
#         i = 1
#         while i < interval:
#             print('No. {}'.format(current.num))
#             current = current.next_person
#             i += 1
#
#         print('current: {}'.format(current.num))
#         current.quit()
#         current = current.next_person
#
#     print('last person is: {}'.format(current.num))