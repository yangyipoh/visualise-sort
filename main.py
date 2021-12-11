import pygame
import math
import random

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
    def __init__(self, size, surface, speed, unit_test=False):
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
        self.draw()

    '''
    sorting self.array using bubble_sort
    '''
    def bubble_sort(self):
        pass

    def merge_sort(self):
        pass

    def radix_sort(self):
        pass

    def cocktail_shaker_sort(self):
        pass

    def bogo_sort(self):
        pass

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
        self.draw()

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


# init, screen, title for pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Sorting Visualisation')

no_elem = 15
my_time = 50
x = VisualSort(no_elem, screen, my_time)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_1:
            x.selection_sort()
        elif event.type == pygame.KEYUP and event.key == pygame.K_2:
            x.insertion_sort()
        elif event.type == pygame.KEYUP and event.key == pygame.K_3:
            x.quicksort()
        elif event.type == pygame.KEYUP and event.key == pygame.K_0:
            x.reset()
