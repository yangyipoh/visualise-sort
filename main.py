import pygame
import math
import random
import argparse

WINDOW_SIZE = (800, 600)
NO_OF_ELEM = 15
SPEED = 100

'''
VisualSort Class

This class contains the sorting algorithms as well as the drawing for pygame
'''
class VisualSort:
    '''
    Initialisation process

    size: number of elements to be sorted
    surface: pygame surface
    speed: delay (in miliseconds) between comparisons
    unit_test: used for unit testing
    '''
    def __init__(self, surface, size=15, speed=200, unit_test=False):
        # save input variable
        self.size = size
        self.surface = surface
        self.sleep_duration = speed
        self.unit_test= unit_test

        # create array to be sorted
        self.array = [Element(i+1) for i in range(size)]

        # shuffle the array
        self.reset()

    '''
    Debugging sorting algorithm by printing the elements in the array
    '''
    def __str__(self):
        str_lst = [None] * (self.size + 2)  # "[" + "number of elements" + "]" = self.size + 2
        
        # first string = [
        str_lst[0] = '['

        # element 1...n-1 = ('number' + ',')
        for i in range(self.size - 1):
            str_lst[i + 1] = str(self.array[i].val) + ', '
        
        # last element = ('number')
        str_lst[self.size] = str(self.array[self.size - 1].val)

        # last string = ]
        str_lst[self.size + 1] = ']'

        return ''.join(str_lst)

    '''
    sorting self.array using quicksort
    '''
    def quicksort(self):
        self.quicksort_aux(self.array, 0, self.size-1)
        if not self.unit_test:
            self.draw()

    '''
    auxiliary function for quicksort
    '''
    def quicksort_aux(self, lst, lo, hi):
        # if pointers contain 0 (base case) 
        if lo >= hi:
            if lo == hi:
                lst[lo].final = True
            return
        
        # set pivot (element to be compared to)
        pivot = lst[hi]
        boundary = lo   # < pivot | > pivot 
        pointer = lo    # element selected
        pivot.selected = True
        if not self.unit_test:
            self.my_sleep()

        # increment all the elements between lo and hi
        while pointer < hi:
            elem_comp = lst[pointer]
            elem_comp.selected = True
            if not self.unit_test:
                self.my_sleep()

            # selected element > pivot --> selected element is at the correct side of the boundary
            if pivot < elem_comp:
                pointer += 1
            # selected element < pivot --> selected element is at the wrong side of the boundary
            else:
                lst[pointer], lst[boundary] = lst[boundary], lst[pointer]
                pointer += 1
                boundary += 1
            elem_comp.selected = False
        
        # swap boundary with pivot
        lst[boundary], lst[hi] = lst[hi], lst[boundary]
        pivot.selected = False
        pivot.final = True
        if not self.unit_test:
            self.my_sleep()

        # sort elements in the boundary
        self.quicksort_aux(lst, lo, boundary-1)
        self.quicksort_aux(lst, boundary+1, hi)

    '''
    sorting self.array using selection_sort
    '''
    def selection_sort(self):
        my_array = self.array
        for i in range(self.size):
            # find minimum element
            min_elem = my_array[i]
            min_idx = i
            min_elem.selected = True
            if not self.unit_test:
                self.my_sleep()
            for j in range(i+1, self.size):
                my_array[j].selected = True
                if not self.unit_test:
                    self.my_sleep()
                if min_elem > my_array[j]:
                    min_elem.selected = False
                    min_elem = my_array[j]
                    min_idx = j
                else:
                    my_array[j].selected = False
            
            # swap min_elem
            my_array[i], my_array[min_idx] = my_array[min_idx], my_array[i]
            my_array[i].final = True
            my_array[i].selected = False
            if not self.unit_test:
                self.my_sleep()
        
        if not self.unit_test:
            self.draw()

    '''
    sorting self.array using insertion_sort
    '''
    def insertion_sort(self):
        lst = self.array
        for i in range(1, self.size):
            # start pointer at the right
            j = i
            while j > 0:
                lst[j].selected = True
                lst[j-1].selected = True
                if not self.unit_test:
                    self.my_sleep()
                # if adjacent pointers are not in order, swap them
                if lst[j] < lst[j-1]:
                    lst[j], lst[j-1] = lst[j-1], lst[j]
                    lst[j].selected = False
                    lst[j - 1].selected = False
                    j -= 1
                # if adjacent pointers are in order, we can terminate early (for this iteration)
                else:
                    lst[j].selected = False
                    lst[j-1].selected = False
                    if not self.unit_test:
                        self.my_sleep()
                    break
                if not self.unit_test:
                    self.my_sleep()
        
        for i in range(self.size):
            self.array[i].selected = False
            self.array[i].final = True
        
        if not self.unit_test:
            self.draw()

    '''
    sorting self.array using bubble_sort
    '''
    def bubble_sort(self):
        lst = self.array
        for i in range(self.size-1):
            for j in range(self.size-i-1):
                lst[j].selected = True
                lst[j+1].selected = True
                if not self.unit_test:
                    self.my_sleep()
                
                # if element on left is greater than element on right, swap them
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                lst[j].selected = False
                lst[j+1].selected = False
                if not self.unit_test:
                    self.my_sleep()
            
            # final element is in the correct place
            lst[j+1].final=True
            if not self.unit_test:
                self.my_sleep()
        
        lst[0].final = True
        if not self.unit_test:
            self.draw()

    '''
    sorting self.array using merge_sort
    '''
    def merge_sort(self):
        self.merge_sort_aux(self.array, 0, self.size)
        for i in range(self.size):
            self.array[i].selected = False
            self.array[i].final = True
        
        if not self.unit_test:
            self.draw()
    
    '''
    auxialiry function for merge sort
    '''
    def merge_sort_aux(self, lst, lo, hi):
        # base case --> lst[lo..hi] contains 0 or 1 element (lst[lo..hi] is sorted)
        if lo >= (hi-1):
            return

        # find the midpoint of the lst to split
        mid = (lo+hi)//2
        
        # sort left and right list
        self.merge_sort_aux(lst, lo, mid)
        self.merge_sort_aux(lst, mid, hi)

        # merge the sorted list
        self.merge(lst, lo, mid, hi)
    
    '''
    in-place merging of 2 sorted list

    the merged list is placed on the left hand side of both lists
    '''
    def merge(self, lst, lo, mid, hi):
        ptr1 = lo       # points to the first element in the first list
        ptr2 = mid      # points to the first element in the second list
        while ptr1 < mid and ptr2 < hi:
            tmp1_select = lst[ptr1]
            tmp2_select = lst[ptr2]
            tmp1_select.selected = True
            tmp2_select.selected = True
            if not self.unit_test:
                self.my_sleep()
            
            # if lst[ptr1] is at the correct position, increment ptr1 to add to merged list
            if lst[ptr1] < lst[ptr2]:
                ptr1 += 1
            # if lst[ptr2] needs to merge with the merged list
            else:
                temp = lst[ptr2]                    # temporarily save lst[ptr2]
                lst[ptr1+1:mid+1] = lst[ptr1:mid]   # shift contents in first list by 1 place
                lst[ptr1] = temp                    # readd lst[ptr2]
                ptr1 += 1                           # increment ptr1 and mid as list is shifted by 1 place
                mid += 1
                ptr2 += 1                           # increment ptr2 as element is added to merged list
            
            tmp1_select.selected = False
            tmp2_select.selected = False
            if not self.unit_test:
                self.my_sleep()

    '''
    function to shuffle the elements in array
    '''
    def reset(self):
        # randomly shuffle the array
        random.shuffle(self.array)

        # reset the visual aspect of the elements
        for i in range(self.size):
            self.array[i].selected = False
            self.array[i].final = False
        
        # update the screen
        if not self.unit_test:
            self.draw()

    '''
    function to test if self.array is sorted (purely for debugging)
    '''
    def _is_sorted(self):
        for i in range(self.size):
            if self.array[i].val != i+1:
                return False
        return True
    
    '''
    function to pause the program
    '''
    def my_sleep(self):
        self.draw()
        pygame.time.wait(self.sleep_duration)

    '''
    draw the array elements onto the screen
    '''
    def draw(self):
        # define colours
        white = (255, 255, 255)
        green = (0, 255, 0)
        red = (255, 0, 0)

        # black the screen
        screen.fill((0, 0, 0))

        # get array and size
        size = self.size
        my_array = self.array

        # calculate width and max_height
        max_height = 540
        width = math.floor(740 / self.size)
        x_start = 30
        y_start = 570

        # draw each rectangle
        for i in range(size):
            my_elem = my_array[i]
            height = max_height * (my_elem.val / self.size)
            y_pos = y_start - height
            x_pos = x_start + width * i
            if my_elem.selected:
                colour = red
            elif my_elem.final:
                colour = green
            else:
                colour = white
            pygame.draw.rect(self.surface, colour, pygame.Rect(x_pos, y_pos, width, height))

        pygame.display.update()


'''
Element Class

This class contains the elements to be sorted
'''
class Element:
    '''
    Initialisation process

    val: value of the element
    is_final: is the current value in it's final position (for visual purpose)
    is_selected: is the current value being selected (for visual purpose)
    '''
    def __init__(self, val, is_final=False, is_selected=False):
        self.val = val
        self.final = is_final
        self.selected = is_selected

    '''
    print the current value
    '''
    def __str__(self):
        return str(self.val)

    def __gt__(self, other):
        return self.val > other.val

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser(description='Change parameters for the program')
    parser.add_argument('-elem', '--elements', metavar='', type=int, default=15, help='Number of elements to be sorted')
    parser.add_argument('-spd', '--speed', metavar='', type=int, default=200, help='Speed of comparisons in milliseconds')

    args = parser.parse_args()

    NO_OF_ELEM = args.elements
    SPEED = args.speed

    # init, screen, title for pygame
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Sorting Visualisation')

    x = VisualSort(screen, size=NO_OF_ELEM, speed=SPEED)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_1:
                x.selection_sort()
            elif event.type == pygame.KEYUP and event.key == pygame.K_2:
                x.insertion_sort()
            elif event.type == pygame.KEYUP and event.key == pygame.K_3:
                x.quicksort()
            elif event.type == pygame.KEYUP and event.key == pygame.K_4:
                x.bubble_sort()
            elif event.type == pygame.KEYUP and event.key == pygame.K_5:
                x.merge_sort()
            elif event.type == pygame.KEYUP and event.key == pygame.K_r:
                x.reset()
