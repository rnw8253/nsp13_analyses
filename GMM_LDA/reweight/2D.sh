Emax=0
T=300
binx=0.50
biny=0.50
cutoff=50

python3 PyReweighting-2D.py -input rna.lda.dat -T $T -Emax $Emax -cutoff $cutoff -discX $binx -discY $biny -job amdweight_CE -weight rna_weights.dat | tee -a reweight_variable.log
mv pmf-c2-rna.lda.dat.xvg pmf-c2.rna.lda.clust.dat
rm *.xvg

python3 PyReweighting-2D.py -input rna_atp.lda.dat -T $T -Emax $Emax -cutoff $cutoff -discX $binx -discY $biny -job amdweight_CE -weight rna_atp_weights.dat | tee -a reweight_variable.log
mv pmf-c2-rna_atp.lda.dat.xvg pmf-c2.rna_atp.lda.clust.dat
rm *.xvg
