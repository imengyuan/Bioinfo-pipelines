#coding=utf-8
species_list = ['PPr', 'Pang', 'Pdel', 'Pfre', 'Plas', 'Pnig', 'Ptr', 'Ptre', 'pba', 'peu', 'pil', 'plau', 'pte']

f_result = open("/tmpdata/train128/snp/03.diversity/final_table.txt","w")


for i in species_list:
	f0 = open("/tmpdata/train128/snp/03.diversity/" +"00.list."+ i,"r")
	number_of_species=0
        line=f0.readline()
        while line:
                number_of_species+=1
                line=f0.readline()

	f1 = open("/tmpdata/train128/snp/03.diversity/" + i + ".Tajima.D","r")
	td_firstline = f1.readline()
	td_secondline = f1.readline()
	td_box = td_secondline.rstrip().split("\t")
	result_TD = td_box[3]
	f2 = open("/tmpdata/train128/snp/03.diversity/" + i +".windowed.pi","r")
	pi_firstline = f2.readline()
	pi_secondline = f2.readline()
	pi_box = pi_secondline.rstrip().split("\t")
	result_pi = pi_box[4]
	f3 = open("/tmpdata/train128/snp/03.diversity/" + i +".het","r")
	het_firstline = f3.readline()
	het_secondline = f3.readline()
	het_box = het_secondline.rstrip().split("\t")
	result_het = het_box[4]
	f4 = open("/tmpdata/train128/snp/03.diversity/" + i +".LROH","r")
	count = 0
	LROH_firstline = f4.readline()
	LROH_secondline = f4.readline()
	while LROH_secondline:
		LROH_box = LROH_secondline.rstrip().split("\t")
		count += float(LROH_box[3])
		LROH_secondline = f4.readline()
	LROH_result = count
	obj = [str(i),str(number_of_species),str(result_pi),str(result_TD),str(LROH_result),str(result_het)]
	out_string="\t".join(obj)
	f_result.write(out_string)
	f_result.write("\n")
	f1.close()
	f2.close()
	f3.close()
	f4.close()



f_result.close()

