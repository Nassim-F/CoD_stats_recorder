from datetime import datetime
import easyocr


start_time = datetime.now()

reader = easyocr.Reader(['fr'])  # Spécifier la langue
result = reader.readtext('test_image/IMG_4632.JPG')

text_result = [detection[1] for detection in result]

print(text_result)
print(len(text_result))


end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))

