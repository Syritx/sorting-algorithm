def sort_numbers(nums):

    temp = len(nums)
    difference = 0

    for check in range(len(nums)):
        minimum = nums[check]
        n_id = 0

        for checking in range(temp):
            for x in range(temp):
                if nums[x+difference] < minimum:
                    minimum = nums[x+difference]
                    n_id = x+difference
        
        if (check == 0): nums[n_id-1] = nums[check]
        else: nums[n_id] = nums[check]

        nums[check] = minimum

        temp -= 1;
        difference += 1;

    for i in range(len(nums)-1):
        if i == 0: nums.remove(nums[i])
        print(nums[i])

numbers = [10,1000,1083,10,2489,324,4327,0,234,-192,-3773,-42723,8213,-2137,-123,183]
sort_numbers(numbers)
