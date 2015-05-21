# script to convert a bilang format to the stagger format
$eos="...EOS...//...EOS...//...EOS...";
if ($#ARGV<1) {
    print STDERR "Usage: $0 ngram\n";
    exit;
}

$ngram=shift;
open(F, "|perl btformatter.mt $ngram");
while(<>) {
    chop;
    s/\_/\/\//g;
    @l=split;
    for($i=0;$i<=$#l;$i++) {
	($s,$t) = split("//",$l[$i]);
	if ($s=~/;/){
	    @sw=split(';',$s);
	    foreach $ws (@sw[0..$#sw-1]) {
		print F "$ws//NIL//%EPS%\n";
	    }
	    print F "$sw[$#sw]//NIL//$t\n";
	}
	else{
	    print F "$s//NIL//$t\n";
	}
    }
    print F "$eos\n$eos\n";
}
close F;

