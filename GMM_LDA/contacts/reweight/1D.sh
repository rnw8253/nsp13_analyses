Emax=1
T=300
binx=0.01
cutoff=100000

nDists=$(cat "weights.dat" | awk '{ print NF; exit}')
echo $nDists
for i in $(seq 1 $nDists)
do
    for j in $(seq 1 4)
    do
        echo $i $j
        awk -v awkvar="$i" '{print ($awkvar)}' "dists.$j.dat" > test.dat
        python3 PyReweighting-1D.py -input test.dat -T $T -disc $binx -Emax $Emax -cutoff $cutoff -job amdweight_CE -weight weights.$j.dat | tee -a reweight_variable.log
        mv pmf-c2-test.dat.xvg distributions/pmf.$j.$i.dat
    done
done
rm *.xvg
rm test.dat
