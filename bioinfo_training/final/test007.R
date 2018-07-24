library(ggplot2)
data1<-read.table("test006.out")
pdf("test007.pdf")
ggplot(data=data1,mapping=aes(x=data1$V1,y=data1$V2,fill=data1$V1,group=factor(1)))+
geom_bar(stat="identity",width=2)+
theme(axis.text=element_text(size=1),axis.title=element_text(size=5))+
labs(x = "motif",y = "count")
dev.off()