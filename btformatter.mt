$eos="EOS";
$bos="BOS";
if ($#ARGV<0) {
print "Usage: $0 contextsize file\n" ;
exit;
}

$context=shift;
while(<>) {
  chop;
  s/:/_COLON_/g;
  s/%/_PERCENTAGE_/g;
  s/,/_COMMA_/g;
  s/\./_PERIOD_/g;
  s/\?/_QMARK_/g;
  
  if ($_ =~/EOS/) {
    if ($line ne "") {
      @words=split(' ',$line);
      for($i=0;$i<=$#words;$i++) {
	@w=split('/',$words[$i]);
	for($j=0;$j<=$#w-4;$j++) {
	  $w[$j]=~s/,/COMMA/g;
	  $w[$j]=~s/\./PERIOD/g;
	  if ($j==0) {
	    $word[$i]= $w[$j];
	  }
	  else {
	    $word[$i].="/$w[$j]";
	  }
	  $w[$j+2]=~s/^,$/COMMA/g;
	  $w[$j+2]=~s/\./PERIOD/g;
	  $w[$j+4]=~s/,/COMMA/g;
	  $w[$j+4]=~s/\./PERIOD/g;
	  $pos[$i]=$w[$j+2];
	  $stag[$i]=$w[$j+4];
	}
      }
      for($i=0;$i<=$#words;$i++) {
	for ($j=$i-$context;$j<=$i+$context;$j++) {
	  if ($j<0) {
	    print "$bos,";
	  }
	  elsif ($j>$#words) {
	    print "$eos,";
	  }
	  elsif ($j==$i) {
            print "$word[$j],";
          }	  
	  elsif ($j<$i) {
	    print "$word[$j],";

	  }
	  elsif ($j>$i) {
	    print "$word[$j],";
	  }
	}
	$orthofeats=GetOrthoFeats($word[$i]);
#	print "$word[$i],$pos[$i],$orthofeats,$stag[$i].\n"
	$ctxt=GetContext(\@stag,$i);
#	print "$orthofeats,$ctxt,$stag[$i].\n"
	print "$orthofeats,$stag[$i].\n"
      }
      $line="";
      @w=();
      @words=();
      @pos=();
      @stags=();
    }
  }
  else {
    $line.= " $_";
  }
}

sub GetContext {
    my ($stag,$i) =@_;
    return "BOS,BOS" if ($i==0);
    return "BOS,$$stag[$i-1]" if ($i==1);
    return "$$stag[$i-2],$$stag[$i-1]";
}

sub GetOrthoFeats {
    my ($w) = @_;
    my ($res) = "";

    if ($w =~ /^[A-Z]/) {
       $res="1,";
    }   
    else {
	$res="0,";
    }
    
    if ($w =~ /^[0-9]/) {
       $res.="1,";
    }   
    else {
	$res.="0,";
    }
    
    if ($w =~ /\-/) {
       $res.="1,";
    }   
    else {
	$res.="0,";
    }

    $l[$c_pref]=
    $l[$c_suf]=substr($l[$c_lex],-3);


    $res.=substr($w,0,3) .",";
    $res.=substr($w,-3);

    return $res;
}
