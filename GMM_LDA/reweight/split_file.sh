
file="../lda/lda.dat"
file2="../lda/labels.dat"
filename1=rna_weights.dat
filename2=rna_atp_weights.dat

num1=$(wc -l $filename1 | awk '{print $1}')
num2=$(wc -l $filename2 | awk '{print $1}')

head -n $num1 $file > test.lda.dat
awk 'NR%1==0' test.lda.dat | awk ' {print $1 " " $2}' > rna.lda.dat

head -n $num1 $file2 > test.lda.dat
awk 'NR%1==0' test.lda.dat | awk ' {print $1 " " $2}' > rna.labels.dat

tail -n $num2 $file > test.lda.dat
awk 'NR%1==0' test.lda.dat | awk ' {print $1 " " $2}' > rna_atp.lda.dat

tail -n $num2 $file2 > test.lda.dat
awk 'NR%1==0' test.lda.dat | awk ' {print $1 " " $2}' > rna_atp.labels.dat

rm test.lda.dat

