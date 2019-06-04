#only import math
import math



def Runner(data):

    def run(data):
        print('je suis running')


        # MEAN
        n_num = [1, 2, 3, 4, 5]

        # create variable to hold number of items in list n_num
        n = len(n_num)
        # create variable to hold the sum of item in list n_num
        get_sum = sum(n_num)

        # divide sum by number of items in list = mean
        mean = get_sum / n

        print("Mean is: " + str(mean))


        # MEDIAN
        n_num = [1, 2, 3, 4, 5]
        n = len(n_num)
        n_num.sort()

        if n % 2 == 0:
            median1 = n_num[n // 2]
            median2 = n_num[n // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = n_num[n // 2]
        print("Median is: " + str(median))




 # quit()