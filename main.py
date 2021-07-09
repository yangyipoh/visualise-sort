import pygame
import math
import random


class VisualSort:
    def __init__(self, size, surface, speed):
        self.size = size
        self.surface = surface
        self.sleep_duration = speed
        self.array = [Element(1)] * size

        for i in range(self.size):
            self.array[i] = Element(i + 1)

        self.reset()

    def __str__(self):
        str_lst = [None] * (self.size + 2)
        str_lst[0] = '['
        for i in range(self.size - 1):
            str_lst[i + 1] = str(self.array[i].val) + ', '
        str_lst[self.size] = str(self.array[self.size - 1].val)
        str_lst[self.size + 1] = ']'
        return ''.join(str_lst)

    def quicksort(self):
        my_array = self.array
        self.quicksort_aux(my_array, 0, self.size-1)
        self.draw()

    def quicksort_aux(self, lst, lo, hi):
        if lo >= hi:
            if lo == hi:
                lst[lo].final = True
            return
        pivot = lst[hi]
        boundary = lo
        pointer = lo
        pivot.selected = True
        self.my_sleep()

        while pointer < hi:
            elem_comp = lst[pointer]
            elem_comp.selected = True
            self.my_sleep()
            if pivot < elem_comp:
                pointer += 1
            else:
                lst[pointer], lst[boundary] = lst[boundary], lst[pointer]
                pointer += 1
                boundary += 1
            elem_comp.selected = False
        lst[boundary], lst[hi] = lst[hi], lst[boundary]
        pivot.selected = False
        pivot.final = True
        self.my_sleep()
        self.quicksort_aux(lst, lo, boundary-1)
        self.quicksort_aux(lst, boundary+1, hi)

    def selection_sort(self):
        my_array = self.array
        for i in range(self.size):
            # find minimum element
            min_elem = my_array[i]
            min_idx = i
            min_elem.selected = True
            self.my_sleep()
            for j in range(i+1, self.size):
                my_array[j].selected = True
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
            self.my_sleep()

    def insertion_sort(self):
        lst = self.array
        for i in range(1, self.size):
            j = i
            while j > 0:
                lst[j].selected = True
                lst[j-1].selected = True
                self.my_sleep()
                if lst[j] < lst[j-1]:
                    lst[j], lst[j-1] = lst[j-1], lst[j]
                    lst[j].selected = False
                    lst[j - 1].selected = False
                    j -= 1
                else:
                    lst[j].selected = False
                    lst[j-1].selected = False
                    self.my_sleep()
                    break
                self.my_sleep()

    def reset(self):
        random.shuffle(self.array)
        for i in range(self.size):
            self.array[i].selected = False
            self.array[i].final = False
        self.draw()

    def my_sleep(self):
        self.draw()
        pygame.time.wait(self.sleep_duration)

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


class Element:
    def __init__(self, val):
        self.val = val
        self.final = False
        self.selected = False

    def __str__(self):
        return str(self.val)

    def __gt__(self, other):
        return self.val > other.val

    def __lt__(self, other):
        return self.val < other.val


# init, screen, title for pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Sorting Visualised')

no_elem = 15
my_time = 200
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
