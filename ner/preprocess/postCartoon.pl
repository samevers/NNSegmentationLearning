#!/usr/bin/perl

## ȥ���Ƿ�����Ƶʵ���ע
while(my $line = <>)
{
	chomp $line;
	my @arr = ($line =~ /#_#(.*?)#_#/g);
	foreach my $a(@arr)
	{
		my $tmp = $a;
		$tmp =~ s/(��)+//g;
		if(length($tmp) < 4)
		{
			$line =~ s/#_#$a#_#/$a/g;
		}
		#print $a.", ";
	}
	#print "\n";

	print $line."\n";
}
