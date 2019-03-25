library(ggplot2)

rm(list=ls())
num_iters = 1000
d = data.frame(data=matrix(nrow = 2 * num_iters, ncol = 3))
colnames(d) = c('round', 'trt', 'guess')

for(i  in 1:num_iters){
  n = 70
  max_val = 2
  A = floor(runif(n, min = 1, max = max_val + 1))
  B = floor(runif(n, min = 1, max = max_val + 1))
  M = matrix(nrow = n, ncol = 2, data = c(A,B), byrow = T)
  
  first_check = 1
  second_check = 1
  
  first = nrow(M[M[,1] == first_check,])
  second = nrow(M[M[,2] == second_check,])
  both = nrow(M[M[,1] == first_check & M[,2] == second_check,])
  
  d[i * 2 - 1, 1] = floor((i+1) / 2)
  d[i * 2 - 1, 2] = 1
  d[i * 2 - 1, 3] = first * second / both
  d[i * 2, 1] = floor((i+1) / 2)
  d[i * 2, 2] = 2
  d[i * 2, 3] = (((second + 1) * (first + 1)) / (both + 1)) - 1
}

ggplot(d[d$trt==1,], aes(x=trt, y = guess, group=trt)) + 
  geom_boxplot() + 
  geom_hline(yintercept = n, color='green') + 
  ylab('Estimate') + xlab('')

