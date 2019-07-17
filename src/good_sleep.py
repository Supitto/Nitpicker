import math
from PIL import Image

def generate_distance_matrix(image1_path, image2_path):
  #opening images
  image1 = Image.open(image1_path)
  image2 = Image.open(image2_path)
  #loading images rgb
  pixels_from_image1 = image1.load()
  pixels_from_image2 = image2.load()
  #getting image size
  (image1_w, image1_h) = image1.size
  (image2_w, image2_h) = image2.size
  #sanity checks
  if image1_w != image2_w:
    pass
  if image1_h != image2_h:
    pass
  distance_matrix = []
  for x in range(image1_w):
    distance_matrix.append([])
    for y in range(image1_h):
      image1_r, image1_g, image1_b = pixels_from_image1[x,y]
      image2_r, image2_g, image2_b = pixels_from_image2[x,y]
      dr = (image1_r - image2_r)**2
      dg = (image1_g - image2_g)**2
      db = (image1_b - image2_b)**2
      distance = math.sqrt(dr + dg + db)
      distance_matrix[-1].append(distance)
  return distance_matrix

def create_image_from_distance_matrix(distance_matrix, new_image_path):
  #creating a image
  w = len(distance_matrix)
  h = len(distance_matrix[0])
  end_image = Image.new('RGB', (w, h), color = (255, 255, 255))
  end_image_pixels = end_image.load()
  for x in range(w):
    for y in range(h):
      c = int(distance_matrix[x][y] * 0.57)
      end_image_pixels[x,y] = (c,c,c)
  end_image.save("new_image_path.jpg")

def apply_distance_matrix_on_image(image_path, new_image_path, distance_matrix, filter = (255,255,255), fator_de_realce=1):
  (fr, fg, fb) = filter
  image = Image.open(image_path)
  image_pixels = image.load()
  dr = (fr/440) * fator_de_realce
  dg = (fg/440) * fator_de_realce
  db = (fb/440) * fator_de_realce
  (w, h) = image.size
  for x in range(w):
    for y in range(h):
      (r, g, b) = image_pixels[x,y]
      dmr = int(dr * distance_matrix[x][y])
      dmg = int(dg * distance_matrix[x][y])
      dmb = int(db * distance_matrix[x][y])
      nr = min(r + dmr, 255)
      ng = min(g + dmg, 255)
      nb = min(b + dmb, 255)
      image_pixels[x,y] = (nr, ng, nb)
  image.save(new_image_path)

