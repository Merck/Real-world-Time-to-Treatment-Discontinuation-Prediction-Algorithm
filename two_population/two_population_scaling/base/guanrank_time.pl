#!/usr/bin/perl
#
%date=();
%status=();
open FILE, "gs_train.dat" or die;
while ($line=<FILE>){
    chomp $line;
    @table=split "\t", $line;
    $date{$table[0]}=$table[1];
    $status{$table[0]}=$table[2];
}
close FILE;


open CURVE, ">death_curve.txt" or die;

@dates=sort{$date{$a}<=>$date{$b}}keys%date;
$old_total=scalar(@dates);
$old_pid=shift @dates;
$old_date=$date{$old_pid};
$total=$old_total;
$original_live_ratio=1;
if ($status{$old_pid}==1){
    $death_count++;
}
$total--;
print CURVE "0\t1\n";
$curve{$old_date}=$original_live_ratio;
while (@dates){
    $pid=shift @dates;
    $new_date=$date{$pid};
    if ($new_date==$old_date){
        if ($status{$pid}==1){
            $death_count++;
        }
        $total--;
    }else{
        $current_live_ratio=1-$death_count/($total+$death_count);
        $original_live_ratio=$current_live_ratio*$original_live_ratio;
        print CURVE "$old_date\t$original_live_ratio\n";
        $curve{$old_date}=$original_live_ratio;
        $death_count=0;
        $old_total=$total;
        $old_date=$new_date;
#        if ($death{$pid}==1){
        if ($status{$pid}==1){
            $death_count++;
        }
        $total--;
    }
}
$curent_live_ratio=1-$death_count/($old_total+$death_count);
$original_live_ratio=$curent_live_ratio*$original_live_ratio;
$curve{$old_date}=$original_live_ratio;
print CURVE "$old_date\t$original_live_ratio\n";
close CURVE;


open GS_VAL, "gs_val.dat" or die;
open NEW, ">gs_val_exptime.dat" or die;
while ($line=<GS_VAL>){
    chomp $line;
    @table=split "\t", $line;
    if ($table[2]==1){
        print NEW "$table[0]\t$table[1]\n";
    }else{
        $this_time=$table[1];
        $ratio=1;
        @dates=sort{$date{$a}<=>$date{$b}}keys%date;
        $old_pid=shift @dates;
        while (@dates){
            $old_date=$date{$old_pid};
            $new_pid=shift @dates;
            $new_date=$date{$new_pid};
           # print "$table[1]\t$old_date\t$new_date\t$date{$pid}\t$this_time\n";
            if ($old_date>=$table[1]){
                if ($ratio==1){
                    $ratio=$curve{$old_date}; # the ratio to be divided.
                }
                $this_time=$this_time+$curve{$old_date}*($new_date-$old_date)/$ratio;

            }else{
            }
            $old_pid=$new_pid;
        }
        print NEW "$table[0]\t$this_time\n";
    }
}

            
