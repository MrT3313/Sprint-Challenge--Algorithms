class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    # - 1 - # MOVEMENT OPTIONS
    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    # - 2 - # ACTUAL MOVEMENT
    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    # - 3 - # SWAP ITEMS
    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    # - 4 - # COMPARE ITEMS
    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    # - 5 - # CHECK LIGHT STATUS
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"
    
    # - 6 - # CHANGE LIGHT STATUS
    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    # - 7 - # SORT
    def sort(self):
        """
        Sort the robot's list.
        """

        debugCount = 0

        # Fill this out
        while self.light_is_on() == False:
            print('THIS IS THE LIST: ', self._list)

            # - !*! - # DEBUGGING
            if debugCount == 2:
                return self._list

            while self.can_move_right(): # YOU NEED TO CONTINUE WITH THIS SORTING PASS

                # Pick up first item
                self.swap_item()

                # Move Right
                self.move_right()

                # Compare
                if self.compare_item() == 1:

                    output = f''
                    output += f'-- SWAP -- '
                    output += f'ITEM IN HAND ({self._item}) with '
                    output += f'CHECK ITEM ({self._list[self._position]})'
                    print(output)

                    # Pick up item that is out of order
                    self.swap_item()
                    self.set_light_on() # Signify there was a swap during this loop

                    # Place item one position lower 
                    self.move_left()
                    self.swap_item()

                    # Move back to the right --> to set up another loop WHILE bot can still move right
                    self.move_right()

                if self.compare_item() == -1 or self.compare_item() == 0:
                    # print('-- DONT SWAP --')
                    # Leave item where you found it
                    self.move_left()
                    self.swap_item()

                    # Move back to the right --> to set up another loop WHILE bot can still move right
                    self.move_right()
                    

            # debugCount += 1

            if self.light_is_on() == True: # was there a swap === YES
                while self.can_move_left(): # YOU HAVE REACHED THE END AND NEED TO GET BACK TO THE BEGINNING BEFORE RESETTING LIGHT TO OFF 
                    self.move_left()

                self.set_light_off()


            else: # was there a swap === NO
                print('__FINAL LIST__ : ', self._list )
                return self._list
'''
Notes:
- use light as a check for > 0 swaps happening in the last pass => reset to off when starting a new pass


PseudoCode:

While LIGHT = OFF                       # list if NOT sorted
    1. Start @ left most item ==> array[0]
    2. Pick up item @ array[0]
    3. Move to right ==> array[1]
    
    4. USE METHOD: compare_item()
        return value => 1:                  # item in hand is > then check item
            ** NEED TO SWAP **

            USE METHOD: set_light_on()

            USE METHOD: swap_item()
            USE METHOD: move_left()
            USE METHOD: swap_item()
            USE METHOD: move_right()

        return value => -1 OR 0:             # item in hand is < then check item
            ** DONT SWAP **
            USE METHOD: move_left()
            USE METHOD: swap_item()
            USE METHOD: move_right()
'''

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92]
    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    # print(robot._list)