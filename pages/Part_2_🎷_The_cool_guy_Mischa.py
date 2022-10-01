# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:30:35 2022

@author: bingbing
"""

import streamlit as st

st.set_page_config(page_title = "02. Part 2 ", page_icon = "🎷")

st.markdown(""" <style> .font {
font-size:25px ; font-family: 'Cooper Black'; color: #30318A;} 
</style> """, unsafe_allow_html = True)
st.markdown(""" <style> .font1 {
font-size:25px ; font-family: 'Cooper Black'; color: #FF9633;} 
</style> """, unsafe_allow_html = True)
st.markdown(""" <style> .font2 {
font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
</style> """, unsafe_allow_html = True)

st.markdown('<p class = "font1"> Welcome to Part_2.</p> \
			<p>✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨</p>\
			<p class = "font1">This part includes 2 MCQs and 3 Multi - select Questions.</p>\
			<p class = "font1">Rules in Part_1 also applies here !! 🙂</p>', unsafe_allow_html = True)

with st.form(key = 'form1'):
	st.markdown('<p class = "font"> 1. Guess which month of summer (northern hemisphere seasons) is Bingbing\'s birthday in. </p>', unsafe_allow_html = True)
	bir = st.radio('', ('December', 'Thirteember', 'June'), index = 0)
	st.write('\n')
	
	submit = st.form_submit_button(label = 'Submit')
	if submit:
		if bir == 'December':
			st.error(' Give you one more chance.', icon = '❌')
		elif bir == 'Thirteember':
			st.error(' OK...... One more chance......', icon = '❌')
		else:
			st.success('Correct!', icon="😎")
			
with st.form(key = 'form2'):
	st.markdown('<p class = "font"> 2. By any chance, do you know what day Oct.1st is in China ? </p>', unsafe_allow_html = True)
	day = st.radio('', ('A normal day', 'National day', 'I don\'t care. It\'s someone\'s birthday'), index = 0)
	st.write('\n')

	submit = st.form_submit_button(label = 'Submit')
	if submit:
		if day == 'A normal day':
			st.warning(' The day has nothing different from other days, but it\'s still has a special meaning.', icon = '😊')
		elif day == 'National day':
			st.success(' Correct! Normally citizens will have a 7-days holiday.', icon = '😁')
		else:
			st.warning(' Don\'t worry...... If I go back, \
			  I promise that you will receive one more \
				  \'Happy Birthday\' from far eastern Asia on every Oct.1st.', icon = '😉')
			

st.markdown('<p class = "font"> 3. Use THREE most suitable song titles from UT to decribe Bingbing. </p>', unsafe_allow_html = True)
st.write('\n')
st.write('\n')
angel = st.checkbox('Angel(s)')
toxic = st.checkbox('Toxic')
candy = st.checkbox('Candy')
complicated = st.checkbox('Complicated')
st.write('\n')

if angel:
	st.success(' Glad to see you got to choose one of the correct answers !', icon = '😇')
if toxic:
	st.success(' Correct. Because the person in the question is just as cute as sexy as charming as etc.......', icon = '🔥')
if candy:
	st.success(' Review: the person in the question can be really SWEET.', icon = '🍬')
if complicated:
	st.warning(' Hmmmmm, this topic is subject to be furtherly investigated.' , icon = '👀')


st.markdown('<p class = "font"> 4. Guess which ones of the following are Bingbing has done/ experienced before ?</p>', unsafe_allow_html = True)
st.write('\n')
st.write('\n')
poem = st.checkbox('She wrote a Mao Zedong\'s poem on the answer sheet in an algorithm exam.')
travel = st.checkbox('She travelled alone in a city where is 1000 KM from her home city.')
pass_out = st.checkbox('She passed out and totally lost consciousness.')
married = st.checkbox('She actually has got married once.')
st.write('\n')

if poem:
	st.success('Once upon a time, she was just very bold to do something insane...... \
			which was not wise at all, because her lecturer was pissed off and gave her a fail grade.' , icon = '😅')
if travel:
	st.success('Yes! She went to Wuhan alone in the autumn of 2018, and in the beginging of 2019, the first Covid case was found there.\
			It was quite a lonely journey, but there were still some moments that she enjoyed.', icon = '🐾')
if pass_out:
	st.success('She has passed out 3 times during her undergraduate years.\
			Well, if she has to pass out again (slight possibility), what she plans is to call you before carrying on that whole faint thing :neutral_face:.\
				So don\'t forget to pick up, or else she can\'t move to the next step ! ', icon = '🙄')
if married:
	st.error('Noo ! No way ! Error ! False !', icon = '❌')


st.markdown('<p class = "font"> 5. What kind of birthday gift do you like ? (You are not gonna\
		 check all the boxes right? ...... )</p>', unsafe_allow_html = True)
st.write('\n')
st.write('\n')
keyboard = st.checkbox('mechanical keyboard')
perfume = st.checkbox('parfum')
ukulele = st.checkbox('a three-head ukulele')
anything = st.checkbox('anything that Bingbing gives')
st.write('\n')

if keyboard:
	st.success(' Good choice! not until I buy myself one hahahaha. I envy your iMac very much btw !!', icon = '⌨')
if perfume:
	st.success(' I don\'t think you like these things, but I do have a veeery tiiiny sample from the store, \
			they somehow just sent me a parfum for men...... Even if you are not into them, I still think that \
			suits you, because its name is \'SAUVAGE ELIXIR\'.', icon = '🎭')
if ukulele:
	st.success(' I also wanna see what does an ukulele with three heads look like. If it really exists, please inform \
			me...... and I will consider making it a gift. If it\'s too expensive, I would thoroughly do some\
				stealing plans and carry out them......', icon = '🎶')
if anything:
	st.success(' Nothing much. This option is soooooooo right !!!', icon = '💯')
	

if anything and ((poem or travel or pass_out) and (not married)) and ((angel and toxic and candy) and (not complicated)) and day =='National day' and bir == 'June':
	st.balloons()
	st.markdown('<p class = "font2">Congratulations! You passed ! Contact Bingbing to get your present !</p>', unsafe_allow_html = True)
