
print "Enter a temperature value (eg. 32F, 100C, etc.): \n";
$input = <STDIN>;
chomp($input);

if ($input =~m/^([+-]?[0-9]+)([CF])$/){
	$InputNum = $1;
	$type = $2;

	if($type eq "C"){
		$c_temperature = $InputNum;
		$f_temperature = ($c_temperature * 9 / 5) + 32;
	}
	else{
		$f_temperature = $InputNum;
		$c_temperature = ($f_temperature - 32) * 5 / 9;
	}

	print "%.2f C is %.2f F \n", $c_temperature, $f_temperature;
}
else{
	print "wrong input!\n"

}