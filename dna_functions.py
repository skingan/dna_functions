def count_kmers(seq,k):
    kmer_hist=dict()
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        if kmer in kmer_hist.keys():
            kmer_hist[kmer] += 1
        else:
            kmer_hist[kmer] = 1
    return(kmer_hist)
    
    
def all_seqs(length):
    bases=['A','C','G','T']
    if length < 1:
        return(print("length must be positive integer"))
    if length == 1:
        seqs=bases
        return(seqs)   
    else:
        seqs=[]
        for s in all_seqs(length-1):
            for b in bases:
                s1=s+b
                seqs.append(s1)
        return(seqs)   
