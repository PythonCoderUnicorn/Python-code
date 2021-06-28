
# Streamlit Bio DNA 

# import libraries 
import pandas as pd 
import streamlit as st 
import altair as alt 
import matplotlib.pyplot as plt

# page title
st.write("""
# DNA Nucleotide Counter App
This app counts the base pairs in the nucleotide. 

**Nucleic acids** consist of a chain of linked units called nucleotides. 
Nucleotide letters are A C G and T representing the four DNA strands – adenine cytosine guanine thymine. 

Each nucleotide consists of three subunits: 
- a phosphate group 
- a sugar  
- deoxyribose  

These three units make up the backbone of the nucleic acid strand 
and attached to the sugar is one of a set of nucleobases.

DNA sequencing is the process of determining the 
sequence of nucleotides (As Ts Cs and Gs) in a piece of DNA.
Regions of DNA up to about 900 base pairs in length are 
routinely sequenced using a method called Sanger sequencing 
or the chain termination method.
""")

# text input 
st.header('DNA sequence')

seq = "A A A A A A A T A A A G A A A C A A T T A A T G A A T C A A G G A A G C A A C C A T  A T T C A T G G A T G C A T C C A G G G A G G C A G C C A C C C T T T T T T T G T T T C T T G G T T G C T T C C T G G G T G G C T G C C T AAA G G G G G G G C G G C C G C C C C C C C"


st.write(seq)




def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')), 
        ('T', seq.count('T')), 
        ('G', seq.count('G')), 
        ('C', seq.count('C')) ])
    return d

X = DNA_nucleotide_count(seq)


# output
st.subheader('Count output')

st.write('A', str(X['A']) +  ' Adenine')
st.write('T', str(X['T']) +  ' Thymine')
st.write('G', str(X['G']) +  ' Guanine')
st.write('C', str(X['C']) + ' Cytosine')


# dataframe
st.subheader('Data Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.dataframe(df)

# display data
st.subheader('Data Visualization')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
# make bars wider
p = p.properties(width= alt.Step(70))

st.write(p)