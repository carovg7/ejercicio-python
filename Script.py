from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

# Se debe de cambiar a la dirección del nuevo archivo .gbk o .fasta a leer
filename = "/home/carolina/carovg7/data/m_cold.fasta"

def summarize_contents(filename):
	lista = []
	lista = os.path.split(filename)
	cadena = " "
	cadena = ("\nfile: "+ lista[1] + "\npath: " + lista[0])
	File_Extension = []
	File_Extension = os.path.splitext(filename)
	if(File_Extension[1]==".gbk"):
		type_file="genbank"
	else:
		type_file="fasta"
		pass
	records = list(SeqIO.parse(filename, type_file))
	cadena += ("\nnum_records: " + str(len(records)))
	cadena += ("\nrecord(s): ")
	for seq_record in SeqIO.parse(filename, type_file):
		cadena += ("\n- id: " + str(seq_record.id))
		cadena += ("\nname: " + seq_record.name)
		cadena += ("\ndescription: " + str(seq_record.description))
	return cadena
if __name__=="__main__":
	resultado = summarize_contents(filename)
	print(resultado)

#///////////////////////////////////////////////////////////////////////
from Bio.Seq import Seq

secuencia1 = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
secuencia2 = Seq("GACGTACCTATGTATAGCGATACGTTAGCTAC")

def concatenate_and_get_reverse_of_complement(secuencia1, secuencia2):
    secuencia = secuencia1 + secuencia2
    rev_com = secuencia.reverse_complement()
    return rev_com
    print(rev_com)
concatenate_and_get_reverse_of_complement(secuencia1, secuencia2)

#/////////////////////////////////////////////////////////////////////
from Bio.Seq import Seq

cadena = "ATGTCACTTACTTACTCACAGTCTTAA"
def print_protein_and_stop_codon_using_standard_table(cadena):
    secuencia = Seq(cadena)
    diccionario = {}
    mrna = secuencia.transcribe()
    diccionario['mRNA'] = mrna
    for i in range(len(secuencia)):
            if((secuencia[i*3:i*3+3] == 'ATG') or (secuencia[i*3:i*3+3] == 'TTG') or (secuencia[i*3:i*3+3] == 'CTG')):
                proteins = secuencia[i*3:].translate(to_stop = True)
                diccionario['Proteins'] = proteins

                for j in range(len(secuencia)):
                    if((secuencia[j*3:j*3+3] == 'TAG') or (secuencia[j*3:j*3+3] == 'TAA') or (secuencia[j*3:j*3+3] == 'TGA')):
                        diccionario['Stop codon'] = secuencia[j*3:j*3+3]
                        break

            if(i+1 == len(secuencia)):
                break
    return diccionario
r = print_protein_and_stop_codon_using_standard_table(cadena)
print(r)

#////////////////////////////////////////////////////////////////
