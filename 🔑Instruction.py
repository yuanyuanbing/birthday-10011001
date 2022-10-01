# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:26:56 2022

@author: bingbing
"""

import streamlit as st

st.set_page_config(
    page_title = "Birthday Gift Exam 2022",
    page_icon = "🎊"
)

st.markdown(""" <style> .font {
font-size:50px ; font-family: 'Cooper Black'; color: #FF9633; text-align: center;} 
</style> """, unsafe_allow_html = True)
st.markdown(""" <style> .font1 {
font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
</style> """, unsafe_allow_html = True)

st.balloons()

st.write(':birthday: ' * 28)
st.markdown('<p class = "font">Birthday Gift Examination</p><p class="font"> Birthday Year 2022</p>', unsafe_allow_html=True)
st.write(':birthday: ' * 28)
st.markdown('<p class = "font1">Instruction: </p><p class="font1">To get a gift,\
			you need to answer 5 questions for each part in the left.</p>\
			<p class = "font1">You will only pass the exam if you see balloons when finishing each part.</p> \
			<p class = "font1">You perhaps have forever to complete the exam, but if that is the case, \
			the exam designer will cry very loudly.</p >', unsafe_allow_html= True)
st.write(':birthday: ' * 28)


		




