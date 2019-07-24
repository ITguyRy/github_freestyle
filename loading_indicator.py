#Ung, Ryan
#Loading indicator replicating https://www.youtube.com/watch?v=bG-IDLfKIoo

# importing time module just to slow down the code by a little.
import time


def counter():
    count = 0
    dots = ['.', '..','...','....']
    #starting at -1 to grab index 0 in the list at the end of first iteration
    dots_count = -1
    #100 is our goal we will loop til that is met
    while 100 > count:
        count+=1
        time.sleep(0.1)
        dots_count=dots_count+1
        #we only want to grab uptil index 3 so we will reset at 4 here
        if dots_count == 4:
            dots_count = -1
        else:
            print("{}% complete. loading{}".format(count, dots[dots_count]))


def main():
    counter()
    print('100% complete. loading.')
    print('loading complete.')
if __name__ == '__main__':
    main()
