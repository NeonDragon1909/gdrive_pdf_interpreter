from reportlab.pdfgen.canvas import Canvas

def word_by_word(canvas, text):

	for line in text[3]:

		for word in line[1][0][1]:

			t = canvas.beginText()

			t.setTextRenderMode(3) 
			t.setFont("Helvetica", float(word[0][2]-2))
			t.setTextOrigin(float(word[0][1]), (float(text[2]) - float(word[0][0]) - (72*float(word[0][2])/96)))
			t.setHorizScale(float(word[0][3]) / canvas.stringWidth(word[1], "Helvetica", float(word[0][2])-2) * 100)
			t.textOut(word[1])

			canvas.drawText(t)

#  WIP. Could be better than drawing text word by word.

#def line_by_line(canvas, text):
#	for line in text[3]:
#		words = line[1][0][1]
#
#		for i in range(len(words)):
#			word_start = words[i][0][1]
#			
#			if (i == 0) or (segment_start == 0):
#				string = ""
#				segment_start = word_start
#				t = canvas.beginText()
#				t.setTextRenderMode(0)
#				t.setTextOrigin(float(words[i][0][1]), (float(text[2]) - float(words[i][0][0]) - (72*float(words[i][0][2])/96)))
#				t.setFont("Helvetica", float(words[i][0][2]-2))
#
#			string = string + words[i][1] + " "
#			try:
#				if ((words[i+1][0][1] - words[i][0][1] - words[i][0][3]) < 5):
#					segment_length = words[i][0][1] - words[i][0][3] - segment_start
#					t.setHorizScale(float(segment_length) / canvas.stringWidth(string, "Helvetica", float(words[i][0][2])-2) * 100)
#					t.textOut(string)
#					canvas.drawText(t)
#			
#			except: 
#				segment_length = words[i][0][1] - words[i][0][3] - segment_start
#				t.setHorizScale(float(segment_length) / canvas.stringWidth(string, "Helvetica", float(words[i][0][2])-2) * 100)
#				t.textOut(string)
#				canvas.drawText(t)

def to_pdf( img, json, pdf):

	canvas = Canvas(pdf, pagesize=(float(json[1]), float(json[2])), pageCompression=1)
	
	canvas.drawInlineImage(img, 0, 0, width=float(json[1]), height=float(json[2]))

	word_by_word(canvas, json)

	canvas.showPage()
	canvas.save()
