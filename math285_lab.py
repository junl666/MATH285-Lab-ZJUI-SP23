# This file has been taken place by math285_lab.ipynb
import math
from matplotlib import pyplot as plt

def func(t, y):
    return (y - t ** 2) * (y ** 2 - t)
    # return y             # for test
    # return math.cos(t)


class NumericalSols:
    def __init__(self, y_0, step, lower_bound, upper_bound, method_num):
        self.t_0 = 0
        self.y_0 = y_0
        assert(lower_bound <= 0 and upper_bound >= 0)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.step = step
        self.t_all = []
        self.y_all = []
        self.method_num = method_num
        if method_num == 0:
            self.eulerMethod()
        elif method_num == 1:
            self.impEuler()
        elif method_num == 2:
            self.runge4ndMethod()
        elif method_num == 3:
            self.linearMulStep()
        else:
            raise NotImplementedError

    # method_num: 0
    def eulerMethod(self):
        # less than 0
        i = 1
        y_n = t_n = 0
        while t_n >= self.lower_bound:
            if i == 1:
                i = 0
                y_n = self.y_0
                t_n = self.t_0
            self.y_all.insert(0, y_n)
            self.t_all.insert(0, t_n)
            y_n = y_n + func(t_n, y_n) * (-self.step)
            t_n = t_n + (-self.step)
        
        # larger than 0   
        i = 1
        y_n = t_n = 0
        while t_n <= self.upper_bound:
            if i == 1:
                i = 0
                y_n = self.y_0
                t_n = self.t_0
            self.y_all.append(y_n)
            self.t_all.append(t_n)

            y_n = y_n + func(t_n, y_n) * self.step
            t_n = t_n + self.step

    # 1
    def impEuler(self):
        i = 1
        y_n = t_n = 0
        while t_n >= self.lower_bound:
            if i == 1:
                i = 0
                y_n = self.y_0
                t_n = self.t_0
            self.y_all.insert(0, y_n)
            self.t_all.insert(0, t_n)
            y_n_euler = y_n + func(t_n, y_n) * (-self.step)    # improved from Euler Method
            y_n = y_n + 0.5 * (-self.step) * (func(t_n, y_n) + func(t_n + (-self.step), y_n_euler))
            t_n = t_n + (-self.step)
        
        i = 1
        y_n = t_n = 0
        while t_n <= self.upper_bound:
            if i == 1:
                i = 0
                y_n = self.y_0
                t_n = self.t_0
            self.y_all.append(y_n)
            self.t_all.append(t_n)

            y_n_euler = y_n + func(t_n, y_n) * self.step    # improved from Euler Method
            y_n = y_n + 0.5 * self.step * (func(t_n, y_n) + func(t_n + self.step, y_n_euler))
            t_n = t_n + self.step
    
    # 2
    def runge4ndMethod(self):
        pass
    
    # 3
    def linearMulStep(self):
        pass
    
    # 4 
    def powerSeries(self):
        pass


def testDiffMethods(y_0, step, lower_bound, upper_bound):
    """
    Test different methods according to the given parameters by drawing plots.
    """
    euler_meth = NumericalSols(y_0, step, lower_bound, upper_bound, 0)
    plt.plot(euler_meth.t_all, euler_meth.y_all, c="green", label="Euler method")
    
    im_eu_meth = NumericalSols(y_0, step, lower_bound, upper_bound, 1)
    plt.plot(im_eu_meth.t_all, im_eu_meth.y_all, c="red", label="Improve Euler method")
    
    ## pewer series test for IVP1
    # power_se = [0.25 * x**4 for x in im_eu_meth.t_all]
    # plt.plot(im_eu_meth.t_all, power_se, c="blue", label="power")

def testDiffSteps(y_0, lower_bound, upper_bound, method_num):
    """
    Test one method with different steps by drawing plots.
    """
    pass

def main():
    fig=plt.figure(num=1,figsize=(5,12))
    plt.xlabel('t', fontsize=19)
    plt.ylabel('y', fontsize=19)
    
    ax1 = fig.add_subplot(311)
    ax1.set_title("311")
    testDiffMethods(1, 0.1, -0.5, 0.5)
    
    ax2 = fig.add_subplot(312)
    ax2.set_title("312")
    testDiffMethods(1, 0.05, -0.5, 0.5)
    
    ax3 = fig.add_subplot(313)
    ax3.set_title("313")
    testDiffMethods(1, 0.01, -0.5, 0.5)
    
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
