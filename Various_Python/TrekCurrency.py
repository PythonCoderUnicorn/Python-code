
# Trek Currency converter
# Zane Dax
# July 7 2021


import numpy as np
import streamlit as st
import pandas as pd
import scipy






# Title
st.title('Star Trek Currency Exchange')


x = np.random.randint(1,30, 5)
# print(x)
st.write(x[0],x[1],x[2],x[3],x[4])




# --------- currency convert
base = 1.00

UFP = base + 0.33
currencyTObase = base / UFP # buy 1 unit of base from currency_1

Ferengi = base + 0.146
baseToFerengi = base / Ferengi

Cardassian = 2005
CardTObase = base / Cardassian

Bajoran = 6.38
BajoranTObase = base / Bajoran




# 1 USD = 6.32 Kuna, 1 Kuna = 0.16
# 1 USD = 5.93 Cedi ,1 Cedi = 0.17

st.markdown("## Convert currency to ")

# selectbox
currencyOption_1 = st.selectbox(
    "What currency do want to convert to ?",
    ['UFP','Ferengi','Cardassian','Bajoran','Klingon','Vulcan']
)
# st.write('You selected: ', currencyOption_1)

if currencyOption_1 == "UFP":
    st.write(" 1 UFP costs from base",UFP)
if currencyOption_1 =="Ferengi":
    st.write(" 1 Ferengi unit from base costs", Ferengi)
if currencyOption_1 =="Cardassian":
    st.write(" 1 Cardassian unit from base costs", Cardassian)
if currencyOption_1 =="Bajoran":
    st.write(" 1 Bajoran unit from base costs", Bajoran)


#------------- selectbox
st.markdown("## Convert currency from ")
currencyOption_2 = st.selectbox(
    "What currency do want to convert from ?",
    ['UFP','Ferengi','Cardassian','Bajoran','Klingon','Vulcan']
)
# st.write('You selected: ', currencyOption_2)

if currencyOption_2 == "UFP":
    st.write(" from UFP currency to base ", round(currencyTObase,3))
if currencyOption_2 =="Ferengi":
    st.write(" from Ferengi currency to base", round(baseToFerengi,3))
if currencyOption_2 =="Cardassian":
    st.write(" from Cardassian to base", round(CardTObase,4))
if currencyOption_2 == "Bajoran":
    st.write(" from 1 Bajoran to base", round(BajoranTObase,3))



# you want 1,500 euros, and want to know what it costs in USD. 
# Multiply 1,500 by 1.146 to get 1,719 USD
# number input
st.title("Currency Converter")
number = st.number_input('Enter quantity of currency')

money_units = number * Ferengi
st.write(round(number,2)," UFP coins costs", round(money_units,3)," in Ferengi currency")

money_units = number * Cardassian
st.write(round(number,2)," UFP coins costs", round(money_units,3)," in Cardassian currency")

money_units = number * Bajoran
st.write(round(number,2)," UFP coins costs", round(money_units,3)," in Bajoran currency")


#  interactive widgets
# if st.button("Convert", help='Click here'):
#     st.write("Submitted")
# else:
#     st.write("")


#  radio button
radioButton = ['Federation','Ferengi','Klingon','Vulcan']
b = st.radio('Pick one Radio Button', radioButton)

if b =="Ferengi":
    st.write(f" **{round(money_units,3)}** Ferengi to 1 UFP")



# trek_stocks = pd.DataFrame(
#     np.random.randint(1e6,5e8,(10,10)),
#     {Planet: ['one', 'two','three','four','five','six','seven','eight','nine','ten']},
#     columns=['TSX','ASX','BSX',
#              'RSX','REX','VMX.V',
#              'BNXR','CRXM','DRX.L', 
#              'ENTX'],
#     # index=[1,11]
#    )


beverages = pd.Series({
    'Organia Crush': 6.7,
    'Risa Tequila Splash': 7.3,
    'Trill Swill': 4.5,
    'Barzan Man': 8.8,
    'Ardana Banana': 7.8,
    'Remus Rum Drum': 9.6,
    'Arrithean Gin Mint': 8.5,
    'Karemma Berry Punch': 9.9,
    'Dosi Tula-Mosh': 7.5,
    'Brax the Max': 5.5
    })

st.dataframe(beverages)

item = beverages[0]
st.write(f" the price is {item}")








st.multiselect('Multiselect', [1,2,3])

# st.select_slider('Slide to select', options=[1,5,'20'])

t = st.time_input('Time entry')
st.write(f" Stardate entered {t}")


st.color_picker('Pick a color')

check = st.checkbox('Check me out')
if check == True:
    st.write("*check*")

check1 = st.checkbox('Read Terms & Conditions')
check2 = st.checkbox('Registered for Conference')
check3 = st.checkbox('Booked accommodations')
if check1 and check2 and check3 == True:
    st.write(" All set")