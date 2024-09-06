import sys
sys.path.append('/Users/reuben204/Reuben/practice/sequence-merger/src/')

from Bio import SeqIO
from utils import reverse_complement
from merge import simple_merge




forward_id = 'TASNIA__16_Forward_Sample_B05'
reverse_id = 'TASNIA_16_Reverse_20240521_143911'

records = SeqIO.parse('./trimmed.fasta', 'fasta')
for r in records:
    if r.id == forward_id:
        print(r.id)
        left = str(r.seq)
    elif r.id == reverse_id:
        print(r.id)
        right = reverse_complement(r.seq)


consensus = simple_merge(left, right)
print()
print(f"consensus length - {len(consensus)}")
print(consensus)
