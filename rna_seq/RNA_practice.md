# RNA pipeline

## Assembly: Trinity
### install
```
	Simply add:

	export TRINITY_HOME=/usr/local/bin
	to your ~/.bashrc file.


	and run trinity via:  $TRINITY_HOME/Trinity
```

```
Trinity --seqType fq --max_memory 4G --CPU 1 --samples_file ../sample.txt --SS_lib_type RF >trinity.log 2>trinity.err &
```

HeracleumL_D478-ZX02-T03_good_1.fq.gz
HeracleumL_D478-ZX02-T03_good_2.fq.gz
重新命名为good_1.fq.gz good_2.fq.gz

Trinity --seqType fq --left reads_1.fq --right reads_2.fq --CPU 6 --max_memory 4G

/usr/local/bin/Trinity


mac
gawk
mawk
nawk

  File "/usr/local/bin/sort", line 7, in <module>
    from sort import cli



Trinity --seqType fq --left good_1.fq --right good_2.fq --CPU 6 --max_memory 4G

echo 'export PATH="/usr/local/opt/llvm/bin:$PATH"' >> ~/.bash_profile


## tencent

Trinity --seqType fq --left good_1.fq --right good_2.fq --CPU 1 --max_memory 2G






