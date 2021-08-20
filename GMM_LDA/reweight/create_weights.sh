
rm rna_weights.dat
touch rna_weights.dat



replicates=( 1 2 3 4 5 6 )
for rep in "${replicates[@]}"
do
    echo $rep
    for i in $(seq 1 40);
    do
        if [ $i -lt 10 ]
        then
            ip=00$i
        elif [ $i -lt 100 ]
        then
            ip=0$i
        else
            ip=$i
        fi
        awk 'NR%2==1' rna_cov_2/run0$rep/weight/nsp13_cov_2_rna.solv.gamd_weights.$ip.log | awk 'NR%1 == 0 {print ($8+$7)/(0.001987*300)" " $2 " " ($8+$7)}' >> rna_weights.dat
    done
done

rm rna_atp_weights.dat
touch rna_atp_weights.dat

replicates=( 1 2 3 )
for rep in "${replicates[@]}"
do
    echo $rep
    for i in $(seq 1 40);
    do
        if [ $i -lt 10 ]
        then
            ip=00$i
        elif [ $i -lt 100 ]
        then
            ip=0$i
        else
            ip=$i
        fi
        awk 'NR%2==1' rna_atp_cov_2/run0$rep/weight/nsp13_cov_2_atp_rna.solv.gamd_weights.$ip.log | awk 'NR%1 == 0 {print ($8+$7)/(0.001987*300)" " $2 " " ($8+$7)}' >> rna_atp_weights.dat
    done
done
