
# Major Depression Iventory (MDI) -- ICD-10/DSM-IV (2003)




import streamlit as st
import numpy as np
import pandas as pd



# Title
st.title('Major Depression Inventory ')

st.write("Major Depression Iventory (MDI) -- ICD-10/DSM-IV (2003)")


score = 0
#-------------------------------------------- 1  radio button
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]

st.write('## have you felt low in spirits or sad?')
r = st.radio('1', radioButton)
# st.write(  )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5


#-------------------------------------------- 2
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]
st.write('## have you lost interest in your daily activities?  ')
r = st.radio('2', radioButton)
# st.write(r )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5











#-------------------------------------------- 3
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]
#-------- questions 1-3: 4+ is diagnostic demarcation line
st.write('## have you felt lacking in energy and strength ?  ')
r = st.radio('3', radioButton)
# st.write(r )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5



#-------------------------------------------- 4
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]
#-------- questions 4-10.b : 3+ is diagnostic demarcation line
st.write('## have you felt less self-cofnident ? ')
r = st.radio('4', radioButton)
# st.write(r )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5



#-------------------------------------------- 5
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]
st.write('## have you had a bad conscience or feelings of guilt ?')
r = st.radio('5', radioButton)
# st.write(r )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5




#-------------------------------------------- 6
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]
st.write("## have you felt that life wasn't worth living ?")
r = st.radio("6", radioButton)
# st.write(r )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5




#-------------------------------------------- 7
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]
st.write("## have you had difficulty in concentrating (reading/watching) ?")
r = st.radio("7", radioButton)
# st.write(r )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5




#-------------------------------------------- 8.1
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]
st.write("## have you felt restless ?")
r = st.radio("8", radioButton)
# st.write(r )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5





#-------------------------------------------- 8.2
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]
st.write("## have you felt subdued or slowed down ?")
r = st.radio("9", radioButton)
# st.write(r )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5






#-------------------------------------------- 9
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]
st.write("## have you had trouble sleeping at night ?")
r = st.radio("10", radioButton)
# st.write(r )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5







#-------------------------------------------- 10.1
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]
st.write("## have you suffered from *reduced* appetite ?")
r = st.radio("11", radioButton)
# st.write(r )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5






#-------------------------------------------- 10.2
radioButton = ['none of the time',\
	'some of the time', \
	'slightly less than half the time',\
	'slightly more than half the time',\
	'most of the time',
	'all the time'
	]
st.write("## have you suffered from *increased* appetite ?")
r = st.radio("12", radioButton)
# st.write(r )
if r == radioButton[0]:
	st.write("you selected ", 1)
	score +=0
if r == radioButton[1]:
	st.write("you selected ", 2)
	score +=1
if r == radioButton[2]:
	st.write("you selected ", 3)
	score +=2
if r == radioButton[3]:
	st.write("you selected ", 4)
	score +=3
if r == radioButton[4]:
	st.write("you selected ", 5)
	score +=4
if r == radioButton[5]:
	st.write("you selected ", 6)
	score +=5

















if score <= 24:
	st.write("## you have a **mild** depression")
elif score == 25 and score <= 29:
	st.write("## you have **moderate** depression")
elif score >= 30:
	st.write("## you have **severe** depression")
else:
	st.write("## score value not recorded")

# ------------------------------------ score 
st.write("... your score: ", score)




#(item 1-10): = ___ + ___ + ___ + ___ + ___ =



#major depression if 5+ of 9 symptoms (items 4 and 5 combined) have been present in the past 2 weeks AND if symptom 1 or 2 are included in the 5 symptoms


# depression rating scale (severity): range 0-50 [question 8 and 10 use a or b only]
# mild depression = score 20-24
# moderate depression = score 25-29
# sever depression = score 30+. 



# depressionQuiz()
# score_card()



st.markdown('You should **_really_ consider** talking to someone for help mental health support')
