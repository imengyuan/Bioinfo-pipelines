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