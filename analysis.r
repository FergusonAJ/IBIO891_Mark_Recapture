# Load packages
library(ggplot2)

# Load the data
setwd('~/Documents/School/SP19/Stats/MarkRecapture/sim')
d = read.csv('output/res.csv', header=T)

# Calculate via Lincoln Peterson Formula
d$lincolnPeterson = (d$M * d$C) / d$R
#Plot LP!
ggplot(d) + geom_histogram(data=d, aes(x=lincolnPeterson), binwidth = 4) + 
  geom_vline(aes(xintercept=256, color='Actual') ) + 
  geom_vline(aes(xintercept=mean(d$lincolnPeterson), color='Mean')) + 
  xlab('Estimate') + ylab('Frequency') + ggtitle('Population Size Estimates')
print('##################')
print('Lincoln Peterson')
print('Mean:')
print(mean(d$lincolnPeterson))
print('Standard Deviation:')
print(sd(d$lincolnPeterson))
ggsave(filename = 'hist.png', width = 4, height = 3, units = 'in')
