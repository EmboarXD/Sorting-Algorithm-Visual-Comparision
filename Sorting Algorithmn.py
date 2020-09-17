import random
import time
##import turtle
import cv2
import numpy as np

##turtle.tracer(0,0)
DRAW = True
ARRAYSIZE = 100
MAX_VALUE = 100
REPEAT_AMOUNT = 1

def draw_list(alist, clear, update):
    image = np.zeros((MAX_VALUE, ARRAYSIZE), np.uint8)
    for x in range(len(alist)):
        image[MAX_VALUE - alist[x], x] = 255
        if update:
            cv2.imshow('image', image)
            cv2.waitKey(1)
    cv2.imshow('image', image)
    cv2.waitKey(1)
    if clear:
        image = np.zeros((MAX_VALUE, ARRAYSIZE), np.uint8)
##    for x in range(len(alist)):
##        turtle.penup()
##        turtle.goto(x, alist[x])
##        turtle.pendown()
##        turtle.forward(1)
##        if update:
##           turtle.update() 
##    turtle.update()
##    if clear:
##        turtle.clear()

def merge(list_a, list_b):
    global iteration_count
    list_c = []
    iteration_count += 1
    while len(list_a) > 0  and len(list_b) > 0:
        #print(list_a, list_b)
        if list_a[0] < list_b[0]:
            list_c.append(list_a.pop(0))
        else:
            list_c.append(list_b.pop(0))
    if list_a == []:
        list_c += list_b
    else:
        list_c += list_a
    #print("merged list is", list_c)
    return list_c


def merge_sort(unsorted):
    global iteration_count
    if DRAW:
        draw_list(unsorted, False, True)
    if len(unsorted) < 2:
        return unsorted
    else:
        #print("splits are", unsorted[:len(unsorted)//2], unsorted[len(unsorted)//2:])
        front = merge_sort(unsorted[:len(unsorted)//2])
        back = merge_sort(unsorted[len(unsorted)//2:])
    return merge(front, back)

def bubble_sort(unsorted):
    swapped = True
    iteration_count = 0
    while swapped:
        iteration_count += 1
        swapped = False
        for x in range(len(unsorted)):
            try:
                if unsorted[x] > unsorted[x+1]:
                    temp = unsorted[x+1]
                    unsorted[x+1] = unsorted[x]
                    unsorted[x] = temp
                    swapped = True
                    if DRAW:
                        draw_list(unsorted, True, False)
            except:
                pass
    return unsorted, iteration_count

def sort(array):
    global iteration_count
    iteration_count += 1

    if DRAW:
        draw_list(array, False, True)

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

def insertionSort(a):
    global iteration_count
    # for every element in our array
    for index in range(1, len(a)):
        iteration_count += 1
        current = a[index]
        position = index
        while position > 0 and a[position-1] > current:
            a[position] = a[position-1]
            if DRAW:
                draw_list(a, True, False)
            position -= 1

        a[position] = current

    return a

def cocktail(a):
    global iteration_count
    for i in range(len(a)//2):
        iteration_count += 1
        swap = False
        for j in range(1+i, len(a)-i):
            # test whether the two elements are in the wrong order
            if a[j] < a[j-1]:
                # let the two elements change places
                a[j], a[j-1] = a[j-1], a[j]
                swap = True
                if DRAW:
                    draw_list(a, True, False)
        # we can exit the outer loop here if no swaps occurred.
        if not swap:
            break
        swap = False
        for j in range(len(a)-i-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swap = True
                if DRAW:
                    draw_list(a, True, False)
        if not swap:
            break
    return a

iteration_counts = []
times_taken = []
for x in range(REPEAT_AMOUNT):
    st = time.time()
    my_list = [random.randrange(1, MAX_VALUE, 1) for i in range(ARRAYSIZE)]
    my_list, iteration_count =  bubble_sort(my_list)
    iteration_counts.append(iteration_count)
    et = time.time()
    tt = et-st
    times_taken.append(tt)

print("Bubble: Takes an average of " + str(sum(iteration_counts)/len(iteration_counts)) + " iterations over the span of " + str(sum(times_taken)/len(times_taken)) + " seconds for an unsorted list of " + str(len(my_list)) + " items")

##turtle.clear()

iteration_counts = []
times_taken = []
for x in range(REPEAT_AMOUNT):
    iteration_count = 0
    st = time.time()
    my_list = [random.randrange(1, MAX_VALUE, 1) for i in range(ARRAYSIZE)]
    my_list = merge_sort(my_list)
    iteration_counts.append(iteration_count)
    et = time.time()
    tt = et-st
    times_taken.append(tt)

print("Merge: Takes an average of " + str(sum(iteration_counts)/len(iteration_counts)) + " iterations over the span of " + str(sum(times_taken)/len(times_taken)) + " seconds for an unsorted list of " + str(len(my_list)) + " items")

##turtle.clear()

iteration_counts = []
times_taken = []
for x in range(REPEAT_AMOUNT):
    iteration_count = 0
    st = time.time()
    my_list = [random.randrange(1, MAX_VALUE, 1) for i in range(ARRAYSIZE)]
    my_list = sort(my_list)
    iteration_counts.append(iteration_count)
    et = time.time()
    tt = et-st
    times_taken.append(tt)

print("Quicksort: Takes an average of " + str(sum(iteration_counts)/len(iteration_counts)) + " iterations over the span of " + str(sum(times_taken)/len(times_taken)) + " seconds for an unsorted list of " + str(len(my_list)) + " items")

##turtle.clear()

iteration_counts = []
times_taken = []
for x in range(REPEAT_AMOUNT):
    iteration_count = 0
    st = time.time()
    my_list = [random.randrange(1, MAX_VALUE, 1) for i in range(ARRAYSIZE)]
    my_list = insertionSort(my_list)
    iteration_counts.append(iteration_count)
    et = time.time()
    tt = et-st
    times_taken.append(tt)

print("Insertion: Takes an average of " + str(sum(iteration_counts)/len(iteration_counts)) + " iterations over the span of " + str(sum(times_taken)/len(times_taken)) + " seconds for an unsorted list of " + str(len(my_list)) + " items")

##turtle.clear()

iteration_counts = []
times_taken = []
for x in range(REPEAT_AMOUNT):
    iteration_count = 0
    st = time.time()
    my_list = [random.randrange(1, MAX_VALUE, 1) for i in range(ARRAYSIZE)]
    my_list = cocktail(my_list)
    iteration_counts.append(iteration_count)
    et = time.time()
    tt = et-st
    times_taken.append(tt)

print("Cocktail: Takes an average of " + str(sum(iteration_counts)/len(iteration_counts)) + " iterations over the span of " + str(sum(times_taken)/len(times_taken)) + " seconds for an unsorted list of " + str(len(my_list)) + " items")

