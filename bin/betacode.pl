#!/usr/bin/perl
use strict;
use warnings;
use Encode::BetaCode qw(beta_decode beta_encode);

my ($filename) = @ARGV;
open(my $fh, '<', $filename)
    or die "Could not open file '$filename' $!";

while (my $row = <$fh>) {
    print beta_decode('greek_punct', $row);
}
