# Converts a giza A3 format file into alg file
# note that the target string appears first in the giza format file and then the source

while(<>) {
    $s=<>;
    chop($s);
    @swords=split(' ',$s);
    $t=<>;
    chop($t);
    @twords=split(/\}\)/,$t);
    %nullwords=();
    GetNullWords($twords[0],\%nullwords);
    $firstnonnull=GetFirstNonNull($#swords,\%nullwords);
    for($i=1;$i<$#twords;$i++) {
	$res="";
	@rest=();
	@oldrest=();
	$twords[$i]=~s/^[ ]*//; 
	($w,$d,@oldrest)=split(/ /,$twords[$i]);
	AdjustMapswithNulls(\@oldrest,\%nullwords,\@rest,$firstnonnull);
#	print "$w " . join(' ',@oldrest). "#" . join(' ',@rest) ."\n";
	for($j=0;$j<=$#rest;$j++) {
	    if ($res eq "") {
#		$res=$swords[$rest[$j]-1] . ":" . ($rest[$j]-$i);
		$res=$swords[$rest[$j]-1];
	    }
	    else {
		$res=~s/:[-]?\d+$//;
#		$res="$res;$swords[$rest[$j]-1]" . ":" . ($rest[$j]-$i);
		$res="$res;$swords[$rest[$j]-1]";
	    }
	}

	if ($res eq "") {
	    $res="%EPS%";
	}

	$bilang[$i]="$res" . "_" . $w;
    }
    print join(' ',@bilang) . "\n";
    @bilang=();
}
sub GetNullWords{
    my ($l,$h)=@_;
    my ($w,$d,@rest)=split(' ',$l);
    my ($j);
    for($j=0;$j<=$#rest;$j++) {
	$$h{$rest[$j]} = 1;
    }
}

sub GetFirstNonNull {
    my ($wlen,$nulls) = @_;
    my ($j);
    for($j=1;$j<=$wlen+1;$j++) {
	if (!defined $$nulls{$j}) {
	    return $j;
	}
    }
    return 1;
}

sub AdjustMapswithNulls {
# if there is a map with elements (i) and i+1 is mapped to NULL, then change the map to be (i,i+1).
    my ($map,$nullwords,$newmap,$firstnonnull) = @_;
    my ($i,$j,$n);
    my ($k) = 0;
    return if ($#{$map}<0);
    for($j=0;$j<=$#{$map};$j++) {
	# special case when the first word is null, attach it to the second word
	if ($$map[$j] == $firstnonnull) {
	    for($n=1;$n<$firstnonnull;$n++){
		$$newmap[$k++]=$n;
	    }
	}
	$$newmap[$k++]=$$map[$j];
	for($n=1;defined $$nullwords{$$map[$j]+$n};$n++) {
	    $$newmap[$k++]=$$map[$j]+$n;
	}
    }
}

sub OldAdjustMapswithNulls{
# if there is a map with elements (i,i+2) and i+1 is mapped to NULL, then change the map to be (i,i+1,i+2).
    my ($map,$nullwords,$newmap) = @_;
    my ($i,$j);
    my ($k) = 0;

    return if ($#{$map}<0);
    if ($#{$map} == 0) {
	$$newmap[$k++]=$$map[0];
    }
    else {
	for($i=1;$i<=$#{$map};$i++) {
	    if ($$map[$i]-$$map[$i-1] > 1){
		for($j=$$map[$i-1]+1;$j<$$map[$i];$j++) {
		    if (defined $$nullwords{$j}){
			$$newmap[$k++]=$j;
		    }
		}
	    }
	    else {
		$$newmap[$k++]=$$map[$i-1];
	    }
	}
	$$newmap[$k]=$$map[$#{$map}];
    }
}
