import os
f2 = open("test007.out","w")

r="data<-data.frame(pre=c(113,134,123,145,123,234,145),now=c(123,145,136,178,113,167,220))​"+"barplot(data$now,col = "red4",beside = TRUE,axes = FALSE)"+"axis(1,seq(from=0.7,by=1.2,length.out=7),labels=c("zhou1","zhou2","zhou3","zhou4","zhou5","zhou6","zhou7"),tick = FALSE,cex.axis=0.75)​"


f = os.system(r)
f.write(f )
f2.close()