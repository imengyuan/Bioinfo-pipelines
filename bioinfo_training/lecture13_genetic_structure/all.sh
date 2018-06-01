for file in ./00.list.*;do /data/part2/software/vcftools_0.1.12b/bin/vcftools --gzvcf scaffold37_cov106.vcf.gz --out ${file#*.} --window-pi 3023989 --keep $file;done

for file in ./00.list.*;do /data/part2/software/vcftools_0.1.12b/bin/vcftools --gzvcf scaffold37_cov106.vcf.gz --out ${file#*.} --TajimaD 3023989 --keep $file;done

for file in ./00.list.*;do /data/part2/software/vcftools_0.1.12b/bin/vcftools --gzvcf scaffold37_cov106.vcf.gz --out ${file#*.} --LROH --chr scaffold37_cov106  --keep $file;done

for file in ./00.list.*;do /data/part2/software/vcftools_0.1.12b/bin/vcftools --gzvcf scaffold37_cov106.vcf.gz --out ${file#*.} --het  --keep $file;done
