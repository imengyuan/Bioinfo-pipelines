for i in /data/part2/00.bam/*bam;do samtools depth $i > ${i##*/}.depth;done
for i in *depth;do python3 avg_depth.py $i;done
for i in *sh;do sh $i;done