import face_recognition
from PIL import Image, ImageDraw


# LOADING IMAGES AND FACE ENCODING
barrie_image = face_recognition.load_image_file('./pictures/known/Barrie.png')
barrie_face_encoding = face_recognition.face_encodings(barrie_image)[0]

gerrie_image = face_recognition.load_image_file('./pictures/known/Gerrie.png') 
gerrie_face_encoding = face_recognition.face_encodings(gerrie_image)[0]

richard_image = face_recognition.load_image_file('./pictures/known/Richard.png')
richard_face_encoding = face_recognition.face_encodings(richard_image)[0]

rikket_image = face_recognition.load_image_file('./pictures/known/Rikket.png')
rikket_face_encoding = face_recognition.face_encodings(rikket_image)[0]

robbie_image = face_recognition.load_image_file('./pictures/known/Robbie.png')
robbie_face_encoding = face_recognition.face_encodings(robbie_image)[0]



# CREATE ARRAY OF ENCODINGS AND NAMES
known_face_encodings = [
	barrie_face_encoding,
	gerrie_face_encoding,
	richard_face_encoding,
	rikket_face_encoding,
	robbie_face_encoding,
]


known_face_names = [
	'Barrie',
	'Gerrie',
	'Richard',
	'Rikket',
	'Robbie',
]


# LOAD TEST IMAGE
test_image = face_recognition.load_image_file('./pictures/unknown/newkids.jpg')


# FIND FACES INSIDE TEST IMAGE
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)


# CONVERTING TO PIL FORMAT
pil_image = Image.fromarray(test_image)


# INSTACE FOR IMAGEDRAW
draw = ImageDraw.Draw(pil_image)


# LOOP TROUGH FACES IN TEST IMAGE
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
	matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

	for i in matches:
		print(i)

	# IF MATCH
	if True in matches:
		first_match_index = matches.index(True)
		name = known_face_names[first_match_index]

	# IF NOT MATCH
	else:
		name = 'Unknown Person'


	# DRAW BOX
	draw.rectangle(((left, top), (right, bottom)), outline=(255,0,0))


	# DRAW TEXT AND RECTANGLE
	text_width, text_height = draw.textsize(name)
	draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(255,0,0), outline=(255,0,0))


	# DRAW TEXT INSIDE RECTANGLE
	draw.text((left + 5, bottom - text_height - 5), name, fill=(255,255,255,255))


# RECOMMANDED TO DO
del draw 

# SHOW IMAGE
pil_image.show()