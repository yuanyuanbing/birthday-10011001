import streamlit as st
from PIL import Image

		
st.set_page_config(page_title = "01. Part 1 ", page_icon = "📖")
image1 = Image.open('1.jpg')
image2 = Image.open('2.jpg')
image3 = Image.open('3.jpg')
	
st.markdown(""" <style> .font {
font-size:25px ; font-family: 'Cooper Black'; color: #30318A;} 
</style> """, unsafe_allow_html = True)
st.markdown(""" <style> .font1 {
font-size:25px ; font-family: 'Cooper Black'; color: #FF9633;} 
</style> """, unsafe_allow_html = True)
st.markdown(""" <style> .font2 {
font-size:20px ; font-family: 'Cooper Black'; color: #30318A;} 
</style> """, unsafe_allow_html = True)
st.markdown(""" <style> .font3 {
font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
</style> """, unsafe_allow_html = True)

st.markdown("""
			""")

st.markdown('<p class = "font1"> Welcome to Part_1.</p> \
			<p>✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨</p>\
			<p class = "font1">This part includes 5 MCQs. When you submit each answer, a message box \
			will appear, the green one indicates correct, the red one stands for wrong, and I don\'t know how to explain the yellow one properly.</p>\
			<p class = "font1">You are encouraged to try every option ! But DON\'T try to test my code, because it may be very fragile.</p>\
			<p>✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨</p>\
			<p class = "font1">Only go to Part_2 when balloons show up ! </p>', unsafe_allow_html = True)
	
with st.form(key = 'form1'):
	st.markdown('<p class = "font"> 1. What is the module code for Programming for Analytics ?</p>', unsafe_allow_html = True)
	code = st.radio('', ('MIS4110', 'MIS41110', 'MIS1001'), index = 0, key = 'code')
	st.write('\n')

	submit = st.form_submit_button(label = 'Submit')
	if submit:
		if code == 'MIS41110':
			st.success('You remember ! What a relief !', icon = "✔")
		elif code == 'MIS1001':
			st.error('You only remember your birthday......', icon = '😭' )
		else:
			st.error('Professor, pay attention to details !', icon = '❌')

with st.form(key = 'form2'):
	st.markdown('<p class = "font"> 2. What is the decimal number for \'0000 1001\' ?</p>', unsafe_allow_html = True)
	decimal = st.radio('', ('1000', '1', '9'), index = 0, key = 'decimal')
	st.write('\n')
	
	submit = st.form_submit_button(label = 'Submit')
	if submit:
		if decimal == '9':
			st.success('Professor, you can not be more intelligent !', icon = "👏")
		else:
			st.error('I know, it\'s complicated, take your time.', icon = '❌')
		
with st.form(key = 'form3'):
	st.markdown('<p class = "font"> 3. What is the full name of KNN ?</p>', unsafe_allow_html = True)
	KNN = st.radio('', ('k Nutty Nuts', 'k Nearest Neighbours', 'k Nicest Nachoes'), index = 0, key = 'KNN')
	st.write('\n')
	
	submit = st.form_submit_button(label = 'Submit')
	if submit:
		if KNN == 'k Nearest Neighbours':
			st.success('Whose professor is this knowledgeable ? :heart_eyes: Oh, mine. ', icon = "✔")
		else:
			st.error('How about getting something to eat !', icon = '❌')
			

with st.form(key = 'form4'):
	st.markdown('<p class = "font"> 4. Which one is your assistant ?</p>', unsafe_allow_html = True)
	col1, col2, col3 = st.columns(3)
	with col1:
		st.image(image1, caption = 'A. The sweet girl')
	with col2:
		st.image(image2, caption = 'B. The elegant women')
	with col3:
		st.image(image3, caption = 'C. The vampire')
	assis = st.radio('', ('A', 'B', 'C', 'all of them'), index = 0)
	st.write('\n')	
	
	submit = st.form_submit_button(label = 'Submit')
	if submit:
		if assis == 'all of them':
			st.success('True. But how comes you have so many assistants ??', icon = "😒")
		elif assis == 'A':
			st.warning('Indeed, you have a sweet one, but still, choose one more time !', icon = '🎀')
		elif assis == 'B':
			st.warning('I think you do have an elegant one, but not the right answer !', icon = '🤨')
		elif assis == 'C':
			st.warning('I can\'t believe you have a vampire as an assistant ......', icon = '😱')

with st.form(key = 'form5'):
	st.markdown('<p class = "font"> 5. Does she have a chance to pursue a PHD with you ?</p>\
			 <p class = "font2">Don\'t worry, just choose, she never believes men\'s promise easily 🙄.</p>', unsafe_allow_html = True)
	phd = st.radio('', ('No', 'YES', 'A YES as large as the galaxy'), index = 0)
	st.write('\n')
	
	submit = submit = st.form_submit_button(label = 'Submit')
	if submit:
		if phd == 'No':
			st.error('Dangerous option ! Choose another right away !', icon = '❗' )
		elif phd == 'YES':
			st.warning('Neither (NOT False) nor (NOT True). Choose again !', icon = '⚠')
		else:
			st.success('While True: (indentation) print(\'he\')', icon = '👻')

if phd == 'A YES as large as the galaxy' and assis == 'all of them' and KNN == 'k Nearest Neighbours' and decimal == '9' and code == 'MIS41110':
	st.balloons( )
	st.markdown('<p class = "font3">Good job, professor! Please go to Part_2 !<p>', unsafe_allow_html = True)
