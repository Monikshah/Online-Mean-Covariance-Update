import numpy as np

# example testcase
x = np.array([2., 7., 8]) # M1 = 0, C1 = 0, M and C are mean and covariance respectively 
y = np.array([3., 9., 9])
z = np.array([6., 2., 10])
w = np.array([5., 5., 4])

mat = [x,y,z,w]

def get_mean(prev_mean, curr_val, N):
    return ((N-1)*prev_mean + curr_val)/(N)
    
def get_variance(cov, prev_mean, curr_mean, curr_val):
    return cov + (curr_val - prev_mean)*(curr_val - curr_mean) 

def get_covar(prev_cov, prev_mean, curr_mean, curr_val, N):
    var = get_variance(prev_cov, prev_mean, curr_mean, curr_val)
    for i in range(len(curr_val)):
        for j in range(len(curr_val)):    
            if i != j and i < j:
                temp = prev_cov[i,j] + curr_val[i]*curr_val[j] - \
                N * curr_mean[i]* curr_mean[j] + \
                (N-1)*prev_mean[i]*prev_mean[j]
                var[i][j] = temp
            else:
                var[i][j] = var[j][i]            
    return var

# main function
# base case computation
N = 2
new_mat = np.stack((x, y), axis = 0)
mean = np.mean(new_mat, axis = 0)
cov = np.cov(new_mat.T, bias = True)*N

for i in range(2, len(mat)):
    N = i+1
    curr_mean = get_mean(mean, mat[i], N)
    curr_cov = get_covar(cov, mean, curr_mean, mat[i], N)
    mean = curr_mean
    cov = curr_cov
    
print(cov)
    
