###ppr
smc++ vcf2smc scaffold37_cov106.vcf.bgzip.gz scaffold37_cov106.smc.gz scaffold37_cov106 Pop1:PPr01,PPr02,PPr03,PPr04,PPr05,PPr06,PPr07,PPr08,PPr09,PPr10

smc++ estimate -o ./ scaffold37_cov106.smc.gz

smc++ plot PPr.plot.pdf ./model.final.json

### Ptr
smc++ vcf2smc scaffold37_cov106.vcf.bgzip.gz Ptr.scaffold37_cov106.smc.gz scaffold37_cov106 Pop1:Ptr01,Ptr02,Ptr03,Ptr04,Ptr08,Ptr09,Ptr12,Ptr13,Ptr15,Ptr16
smc++ estimate -o ./ Ptr.scaffold37_cov106.smc.gz
smc++ plot Ptr.plot.pdf ./model.final.json

### peu
smc++ vcf2smc scaffold37_cov106.vcf.bgzip.gz peu.scaffold37_cov106.smc.gz scaffold37_cov106 Pop1:peu01,peu02,peu03,peu04,peu05,peu06,peu07,peu08,peu09,peu10
smc++ estimate -o ./ peu.scaffold37_cov106.smc.gz
smc++ plot peu.plot.pdf ./model.final.json

###pil
smc++ vcf2smc scaffold37_cov106.vcf.bgzip.gz pil.scaffold37_cov106.smc.gz scaffold37_cov106 Pop1:pil01,pil02,pil03,pil04,pil05,pil06,pil07,pil08,pil09,pil10,pil11,pil12,pil13,pil14,pil15,pil16
smc++ estimate -o ./ pil.scaffold37_cov106.smc.gz
smc++ plot pil.plot.pdf ./model.final.json