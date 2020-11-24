from PIL import Image, ImageDraw, ImageFont

def idGenerator(dictionary):
    image = Image.new('RGB', (1100, 850), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('arial.ttf', size=45)

    (x, y) = (50, 50)
    company = "Indian Insittute Of Information Technology"
    color = 'rgb(255, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=50)
    draw.text((x, y), company, fill=color, font=font)

    (x, y) = (600, 125)
    message = str('ID : ' + str(dictionary['roll number']))
    color = 'rgb(0, 255, 0)'  
    font = ImageFont.truetype('arial.ttf', size=60)
    draw.text((x, y), message, fill=color, font=font)
    
    (x, y) = (50, 250)
    message = dictionary['name']
    message = str('Name : ' + str(message))
    color = 'rgb(0, 0, 255)'  
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), message, fill=color, font=font)
    
    (x, y) = (50, 350)
    message = 'Gender : ' + str(dictionary['gender'])
    color = 'rgb(0, 0, 0)' 
    draw.text((x, y), message, fill=color, font=font)
    
    (x, y) = (50, 450)
    message = 'Department : '+str(dictionary['department'])
    color = 'rgb(0, 0, 0)'  
    draw.text((x, y), message, fill=color, font=font)
    
    (x, y) = (50, 550)
    message = 'Email Id : ' + str(dictionary['email'])
    color = 'rgb(0, 0, 0)'  
    draw.text((x, y), message, fill=color, font=font)
    
    (x, y) = (50, 650)
    message = 'Address : ' + str(dictionary['address'])
    color = 'rgb(0, 0, 0)'  
    draw.text((x, y), message, fill=color, font=font)
    
    image.save(str('StaffID\\' + dictionary['name'] + '.png'))
    
    til = Image.open('StaffID\\' + dictionary['name'] + '.png')
    im = Image.open(r'Assets\blankDP.png')  
    til.paste(im, (750, 280))
    til.save('StaffID\\' + dictionary['name'] + '.png')
